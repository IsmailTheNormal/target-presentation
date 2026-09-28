import React, { useRef } from 'react';
import { 
  FileSpreadsheet, 
  Upload, 
  Download, 
  Plus, 
  Users, 
  GraduationCap, 
  TrendingUp, 
  BookOpen,
  SlidersHorizontal,
  ChevronDown,
  UserPlus,
  ClipboardPaste,
  RefreshCw,
  CheckCircle2,
  AlertTriangle,
  Radio
} from 'lucide-react';
import { ClassData } from '../types/gradebook';
import { downloadXMLFile, importFromXML } from '../utils/xmlParser';
import { SyncStatus } from '../utils/googleSheetsSync';

interface HeaderProps {
  classes: ClassData[];
  currentClassId: string;
  onSelectClass: (id: string) => void;
  onOpenAddClass: () => void;
  onOpenAddStudent: () => void;
  onOpenBulkAddStudents: () => void;
  onOpenCategories: () => void;
  onOpenGoogleSheets: () => void;
  onImportClass: (newClass: ClassData) => void;
  overallAverage: number;
  syncStatus: SyncStatus;
  syncMessage?: string;
  lastSyncTime?: Date | null;
}

export const Header: React.FC<HeaderProps> = ({
  classes,
  currentClassId,
  onSelectClass,
  onOpenAddClass,
  onOpenAddStudent,
  onOpenBulkAddStudents,
  onOpenCategories,
  onOpenGoogleSheets,
  onImportClass,
  overallAverage,
  syncStatus,
  syncMessage,
  lastSyncTime,
}) => {
  const currentClass = classes.find((c) => c.id === currentClassId) || classes[0];
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleXMLFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      try {
        const text = evt.target?.result as string;
        const imported = importFromXML(text);
        onImportClass(imported);
        alert(`Successfully imported "${imported.name}" with ${imported.students.length} students!`);
      } catch (err: any) {
        alert('Error importing XML: ' + (err.message || 'Unknown error'));
      }
    };
    reader.readAsText(file);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  const formattedSyncTime = lastSyncTime
    ? lastSyncTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
    : null;

  return (
    <header className="bg-white border-b border-slate-200/90 shadow-sm sticky top-0 z-30 backdrop-blur-md">
      <div className="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8 py-3">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          
          {/* Left: Brand & Class Selector */}
          <div className="flex items-center gap-4 flex-wrap">
            <div className="flex items-center gap-2.5">
              <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-indigo-600 to-violet-600 flex items-center justify-center text-white shadow-md shadow-indigo-200">
                <GraduationCap className="w-6 h-6" />
              </div>
              <div>
                <h1 className="text-base sm:text-lg font-black text-slate-900 tracking-tight flex items-center gap-2">
                  Journaller Gradebook
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
                    Live
                  </span>
                </h1>
                <p className="text-[11px] text-slate-500">Continuous Google Sheets Sync & Student Analytics</p>
              </div>
            </div>

            <div className="h-6 w-px bg-slate-200 hidden sm:block"></div>

            {/* Class Dropdown */}
            <div className="flex items-center gap-2">
              <div className="relative">
                <select
                  value={currentClassId}
                  onChange={(e) => onSelectClass(e.target.value)}
                  className="appearance-none bg-slate-50 hover:bg-slate-100 border border-slate-300 text-slate-800 text-xs sm:text-sm font-bold rounded-xl pl-3 pr-8 py-2 focus:ring-2 focus:ring-indigo-500 focus:outline-none transition cursor-pointer"
                >
                  {classes.map((cls) => (
                    <option key={cls.id} value={cls.id}>
                      {cls.name} ({cls.academicYear})
                    </option>
                  ))}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-500 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>

              <button
                onClick={onOpenAddClass}
                title="Create New Class"
                className="p-2 text-slate-600 hover:text-indigo-600 hover:bg-indigo-50 rounded-xl border border-slate-200 transition flex items-center gap-1 text-xs font-bold"
              >
                <Plus className="w-4 h-4" />
                <span className="hidden lg:inline">New Class</span>
              </button>
            </div>
          </div>

          {/* Center: Live Google Sheets Auto-Sync Status Badge */}
          <div className="flex items-center gap-2">
            <button
              onClick={onOpenGoogleSheets}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-bold transition border shadow-sm ${
                syncStatus === 'synced'
                  ? 'bg-emerald-50 text-emerald-800 border-emerald-300 hover:bg-emerald-100'
                  : syncStatus === 'syncing'
                  ? 'bg-amber-50 text-amber-800 border-amber-300 animate-pulse'
                  : syncStatus === 'error'
                  ? 'bg-rose-50 text-rose-800 border-rose-300 hover:bg-rose-100'
                  : syncStatus === 'connected'
                  ? 'bg-blue-50 text-blue-800 border-blue-300 hover:bg-blue-100'
                  : 'bg-emerald-600 text-white border-emerald-700 hover:bg-emerald-700'
              }`}
              title="Click to configure or view continuous Google Sheets sync"
            >
              {syncStatus === 'synced' && (
                <>
                  <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                  <span>Google Sheets Synced {formattedSyncTime && `(${formattedSyncTime})`}</span>
                </>
              )}

              {syncStatus === 'syncing' && (
                <>
                  <RefreshCw className="w-3.5 h-3.5 text-amber-600 animate-spin" />
                  <span>Saving to Google Sheet...</span>
                </>
              )}

              {syncStatus === 'error' && (
                <>
                  <AlertTriangle className="w-4 h-4 text-rose-600" />
                  <span>Sync Issue (Click to fix)</span>
                </>
              )}

              {syncStatus === 'connected' && (
                <>
                  <Radio className="w-3.5 h-3.5 text-blue-600" />
                  <span>Google Sheets Ready</span>
                </>
              )}

              {syncStatus === 'disconnected' && (
                <>
                  <FileSpreadsheet className="w-4 h-4" />
                  <span>Connect Google Sheet Auto-Sync</span>
                </>
              )}
            </button>
          </div>

          {/* Right: Actions */}
          <div className="flex items-center gap-2 flex-wrap">
            {/* Bulk Add Students */}
            <button
              onClick={onOpenBulkAddStudents}
              className="flex items-center gap-1.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm transition"
              title="Paste your class roster (30+ students at once)"
            >
              <ClipboardPaste className="w-3.5 h-3.5 text-indigo-600" />
              <span>Paste Roster</span>
            </button>

            {/* XML Export */}
            <button
              onClick={() => downloadXMLFile(currentClass)}
              className="flex items-center gap-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 px-3 py-1.5 rounded-xl text-xs font-semibold shadow-sm transition"
              title="Save class as XML file"
            >
              <Download className="w-3.5 h-3.5 text-slate-600" />
              <span>Save XML</span>
            </button>

            {/* XML Import */}
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleXMLFileChange}
              accept=".xml,text/xml"
              className="hidden"
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              className="flex items-center gap-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 px-3 py-1.5 rounded-xl text-xs font-semibold shadow-sm transition"
              title="Load from XML file"
            >
              <Upload className="w-3.5 h-3.5 text-slate-600" />
              <span>Load XML</span>
            </button>

            {/* Categories & Caps */}
            <button
              onClick={onOpenCategories}
              className="flex items-center gap-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 px-3 py-1.5 rounded-xl text-xs font-semibold shadow-sm transition"
              title="Configure categories (Attendance, Homework, Participation) and caps"
            >
              <SlidersHorizontal className="w-3.5 h-3.5 text-slate-600" />
              <span>Categories & Caps</span>
            </button>

            {/* Add Student Single */}
            <button
              onClick={onOpenAddStudent}
              className="p-2 text-slate-600 hover:text-indigo-600 hover:bg-indigo-50 rounded-xl border border-slate-300 transition"
              title="Add Single Student"
            >
              <UserPlus className="w-4 h-4" />
            </button>
          </div>

        </div>
      </div>
    </header>
  );
};
