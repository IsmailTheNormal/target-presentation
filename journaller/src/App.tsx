import React, { useState, useEffect, useRef, useMemo } from 'react';
import { ClassData, Student, Category } from './types/gradebook';
import { INITIAL_CLASSES } from './utils/sampleData';
import { Header } from './components/Header';
import { GradebookTable } from './components/GradebookTable';
import { StudentAnalyticsModal } from './components/StudentAnalyticsModal';
import { GoogleSheetsModal } from './components/GoogleSheetsModal';
import { CategorySettingsModal } from './components/CategorySettingsModal';
import { AddStudentModal } from './components/AddStudentModal';
import { BulkAddStudentsModal } from './components/BulkAddStudentsModal';
import { ClassSettingsModal } from './components/ClassSettingsModal';
import { calculateStudentOverallStats } from './utils/calculations';
import { 
  getSavedWebhookUrl, 
  getAutoSyncEnabled, 
  syncClassToGoogleSheets, 
  SyncStatus 
} from './utils/googleSheetsSync';
import { 
  Sparkles, 
  HelpCircle, 
  TrendingUp, 
  Users, 
  FileSpreadsheet, 
  Layers,
  ClipboardPaste,
  Trash2,
  RefreshCw,
  CheckCircle2,
  Radio
} from 'lucide-react';

const STORAGE_KEY = 'journaller_teacher_gradebook_data_v1';

export function App() {
  const [classes, setClasses] = useState<ClassData[]>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        return JSON.parse(saved);
      }
    } catch (e) {
      console.error('Failed to load classes from localStorage', e);
    }
    return INITIAL_CLASSES;
  });

  const [currentClassId, setCurrentClassId] = useState<string>(() => {
    return classes[0]?.id || 'class-1';
  });

  // Google Sheets Continuous Sync State
  const [syncStatus, setSyncStatus] = useState<SyncStatus>(() => {
    const url = getSavedWebhookUrl();
    return url ? 'connected' : 'disconnected';
  });
  const [syncMessage, setSyncMessage] = useState<string>('');
  const [lastSyncTime, setLastSyncTime] = useState<Date | null>(null);

  // Modals state
  const [selectedStudentForAnalytics, setSelectedStudentForAnalytics] = useState<Student | null>(null);
  const [isGoogleSheetsModalOpen, setIsGoogleSheetsModalOpen] = useState(false);
  const [isCategoriesModalOpen, setIsCategoriesModalOpen] = useState(false);
  const [isAddStudentModalOpen, setIsAddStudentModalOpen] = useState(false);
  const [isBulkAddModalOpen, setIsBulkAddModalOpen] = useState(false);
  const [isAddClassModalOpen, setIsAddClassModalOpen] = useState(false);

  const isInitialMount = useRef(true);
  const syncTimeoutRef = useRef<any>(null);

  const currentClass = classes.find((c) => c.id === currentClassId) || classes[0];

  // Continuous Auto-Sync & Local Storage persistence
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(classes));
    } catch (e) {
      console.error('Failed to save to localStorage', e);
    }

    // Skip auto-sync on initial page render
    if (isInitialMount.current) {
      isInitialMount.current = false;
      return;
    }

    const webhookUrl = getSavedWebhookUrl();
    const autoSyncEnabled = getAutoSyncEnabled();

    if (!webhookUrl || !autoSyncEnabled) {
      setSyncStatus(webhookUrl ? 'connected' : 'disconnected');
      return;
    }

    // Indicate syncing
    setSyncStatus('syncing');
    setSyncMessage('Saving changes to Google Sheet...');

    if (syncTimeoutRef.current) {
      clearTimeout(syncTimeoutRef.current);
    }

    // Debounce real-time updates by 750ms
    syncTimeoutRef.current = setTimeout(async () => {
      const res = await syncClassToGoogleSheets(currentClass, webhookUrl);
      if (res.success) {
        setSyncStatus('synced');
        setSyncMessage(res.message);
        setLastSyncTime(res.timestamp);
      } else {
        setSyncStatus('error');
        setSyncMessage(res.message);
      }
    }, 750);

    return () => {
      if (syncTimeoutRef.current) clearTimeout(syncTimeoutRef.current);
    };
  }, [classes, currentClassId]);

  // Grade updates per lesson & category
  const handleUpdateGrade = (
    studentId: string,
    lessonId: string,
    categoryId: string,
    value: number | undefined
  ) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;

        const updatedGrades = { ...cls.grades };
        if (!updatedGrades[studentId]) updatedGrades[studentId] = {};
        if (!updatedGrades[studentId][lessonId]) updatedGrades[studentId][lessonId] = {};

        if (value === undefined) {
          delete updatedGrades[studentId][lessonId][categoryId];
        } else {
          updatedGrades[studentId][lessonId][categoryId] = value;
        }

        return {
          ...cls,
          grades: updatedGrades,
        };
      })
    );
  };

  const handleAddLesson = (monthId: string) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;
        const monthLessons = cls.lessons.filter((l) => l.monthId === monthId);
        const nextNum = monthLessons.length + 1;
        const newLesson = {
          id: `${monthId}-l${Date.now()}`,
          monthId,
          dayNumber: nextNum,
          date: `Day ${nextNum}`,
          title: `Day ${nextNum}`,
        };
        return {
          ...cls,
          lessons: [...cls.lessons, newLesson],
        };
      })
    );
  };

  // Student management
  const handleAddStudent = (newStudent: Student) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;
        return {
          ...cls,
          students: [...cls.students, newStudent],
        };
      })
    );
  };

  const handleBulkAddStudents = (newStudents: Student[]) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;
        return {
          ...cls,
          students: [...cls.students, ...newStudents],
        };
      })
    );
  };

  const handleDeleteStudent = (studentId: string) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;
        const updatedGrades = { ...cls.grades };
        delete updatedGrades[studentId];
        return {
          ...cls,
          students: cls.students.filter((s) => s.id !== studentId),
          grades: updatedGrades,
        };
      })
    );
  };

  const handleClearStudents = () => {
    if (window.confirm(`Clear all students from "${currentClass.name}" to start with a fresh blank roster?`)) {
      setClasses((prevClasses) =>
        prevClasses.map((cls) => {
          if (cls.id !== currentClass.id) return cls;
          return {
            ...cls,
            students: [],
            grades: {},
          };
        })
      );
    }
  };

  // Category management
  const handleSaveCategories = (updatedCategories: Category[]) => {
    setClasses((prevClasses) =>
      prevClasses.map((cls) => {
        if (cls.id !== currentClass.id) return cls;
        return {
          ...cls,
          categories: updatedCategories,
        };
      })
    );
  };

  // Class management
  const handleAddClass = (newClass: ClassData) => {
    setClasses((prev) => [...prev, newClass]);
    setCurrentClassId(newClass.id);
  };

  const handleImportClass = (importedClass: ClassData) => {
    setClasses((prev) => {
      const idx = prev.findIndex((c) => c.id === importedClass.id);
      if (idx >= 0) {
        const next = [...prev];
        next[idx] = importedClass;
        return next;
      }
      return [...prev, importedClass];
    });
    setCurrentClassId(importedClass.id);
  };

  // Navigation in Student Analytics Modal
  const handleNavigateStudent = (direction: 'prev' | 'next') => {
    if (!selectedStudentForAnalytics || !currentClass) return;
    const currentIndex = currentClass.students.findIndex(
      (s) => s.id === selectedStudentForAnalytics.id
    );
    if (currentIndex === -1) return;

    let newIndex = direction === 'next' ? currentIndex + 1 : currentIndex - 1;
    if (newIndex >= currentClass.students.length) newIndex = 0;
    if (newIndex < 0) newIndex = currentClass.students.length - 1;

    setSelectedStudentForAnalytics(currentClass.students[newIndex]);
  };

  // Class average calculations
  const classStats = currentClass ? currentClass.students.map((s) => calculateStudentOverallStats(s, currentClass)) : [];
  const overallAverage = classStats.length > 0
    ? Math.round((classStats.reduce((sum, s) => sum + s.overallAveragePercentage, 0) / classStats.length) * 10) / 10
    : 0;

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans">
      {/* Top Navigation Bar with Live Sync Status */}
      <Header
        classes={classes}
        currentClassId={currentClassId}
        onSelectClass={setCurrentClassId}
        onOpenAddClass={() => setIsAddClassModalOpen(true)}
        onOpenAddStudent={() => setIsAddStudentModalOpen(true)}
        onOpenBulkAddStudents={() => setIsBulkAddModalOpen(true)}
        onOpenCategories={() => setIsCategoriesModalOpen(true)}
        onOpenGoogleSheets={() => setIsGoogleSheetsModalOpen(true)}
        onImportClass={handleImportClass}
        overallAverage={overallAverage}
        syncStatus={syncStatus}
        syncMessage={syncMessage}
        lastSyncTime={lastSyncTime}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-[1700px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
        
        {/* Banner with Google Sheets continuous sync indicator */}
        <div className="bg-gradient-to-r from-indigo-900 via-indigo-800 to-slate-900 rounded-3xl p-6 text-white shadow-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-6 relative overflow-hidden">
          <div className="absolute right-0 top-0 translate-x-10 -translate-y-10 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>

          <div className="space-y-1.5 z-10 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>
                {syncStatus === 'synced'
                  ? 'Continuously saving to Google Sheets in real-time'
                  : syncStatus === 'syncing'
                  ? 'Saving changes to Google Sheets...'
                  : syncStatus === 'error'
                  ? 'Google Sheets Sync Error (Click to re-test)'
                  : 'Google Sheets Auto-Sync Ready'}
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-black tracking-tight text-white">
              {currentClass.name}
            </h2>
            <p className="text-xs sm:text-sm text-indigo-200">
              Students in rows &bull; Click month headers to smoothly expand/collapse categories &bull; Click any student to view their <strong>performance gain/drop graph</strong>.
            </p>
          </div>

          <div className="flex items-center gap-3 z-10 flex-wrap">
            <button
              onClick={() => setIsGoogleSheetsModalOpen(true)}
              className="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold px-4 py-2.5 rounded-xl text-xs shadow-lg shadow-emerald-500/20 transition"
            >
              <FileSpreadsheet className="w-4 h-4 text-slate-950" />
              <span>
                {syncStatus === 'synced'
                  ? 'Google Sheets Connected 🟢'
                  : 'Configure Google Sheet Sync'}
              </span>
            </button>
            <button
              onClick={() => setIsBulkAddModalOpen(true)}
              className="flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white font-semibold px-4 py-2.5 rounded-xl text-xs border border-white/20 transition"
            >
              <ClipboardPaste className="w-4 h-4 text-indigo-300" />
              <span>Paste Class Roster</span>
            </button>
            {currentClass.students.length > 0 && (
              <button
                onClick={handleClearStudents}
                className="flex items-center gap-1.5 bg-rose-500/20 hover:bg-rose-500/30 text-rose-200 font-semibold px-3 py-2.5 rounded-xl text-xs border border-rose-500/30 transition"
                title="Clear students to start blank"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Clear List</span>
              </button>
            )}
          </div>
        </div>

        {/* Main Gradebook Grid with Horizontal Expansion & Smooth Animations */}
        <GradebookTable
          classData={currentClass}
          onUpdateGrade={handleUpdateGrade}
          onSelectStudentForAnalytics={(student) => setSelectedStudentForAnalytics(student)}
          onDeleteStudent={handleDeleteStudent}
          onAddLesson={handleAddLesson}
        />

        {/* Quick Tips Footer */}
        <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-4 text-xs text-slate-600">
          <div className="flex items-center gap-2">
            <HelpCircle className="w-4 h-4 text-indigo-600 shrink-0" />
            <span>
              <strong>Continuous Saving:</strong> All marks and roster edits save automatically to your Google Sheet without manual copy-pasting. Click any student row to view their <strong>gain/drop trajectory line graph</strong>!
            </span>
          </div>

          <div className="flex items-center gap-4 text-slate-400">
            <span>Real-time Auto-Sync</span>
            <span>&bull;</span>
            <span>Local Backup Active</span>
          </div>
        </div>

      </main>

      {/* Modals */}
      {selectedStudentForAnalytics && (
        <StudentAnalyticsModal
          student={selectedStudentForAnalytics}
          classData={currentClass}
          onClose={() => setSelectedStudentForAnalytics(null)}
          onNavigateStudent={handleNavigateStudent}
        />
      )}

      {isGoogleSheetsModalOpen && (
        <GoogleSheetsModal
          classData={currentClass}
          onClose={() => setIsGoogleSheetsModalOpen(false)}
          onSyncSuccess={(time) => {
            setSyncStatus('synced');
            setLastSyncTime(time);
          }}
        />
      )}

      {isCategoriesModalOpen && (
        <CategorySettingsModal
          categories={currentClass.categories}
          onSaveCategories={handleSaveCategories}
          onClose={() => setIsCategoriesModalOpen(false)}
        />
      )}

      {isAddStudentModalOpen && (
        <AddStudentModal
          onAddStudent={handleAddStudent}
          onClose={() => setIsAddStudentModalOpen(false)}
          nextRollNumber={currentClass.students.length + 1}
        />
      )}

      {isBulkAddModalOpen && (
        <BulkAddStudentsModal
          onAddStudents={handleBulkAddStudents}
          onClose={() => setIsBulkAddModalOpen(false)}
          existingCount={currentClass.students.length}
        />
      )}

      {isAddClassModalOpen && (
        <ClassSettingsModal
          onAddClass={handleAddClass}
          onClose={() => setIsAddClassModalOpen(false)}
        />
      )}
    </div>
  );
}
export default App;
