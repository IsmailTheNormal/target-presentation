import React, { useState, useMemo } from 'react';
import { 
  ChevronRight, 
  ChevronDown, 
  TrendingUp, 
  TrendingDown, 
  Minus, 
  BarChart3, 
  Search, 
  Maximize2, 
  Minimize2,
  Trash2,
  Calendar,
  Layers,
  Plus,
  Clock,
  Sparkles
} from 'lucide-react';
import { ClassData, Student, Lesson } from '../types/gradebook';
import { 
  calculateStudentLessonStats,
  calculateStudentMonthlyStats, 
  calculateStudentOverallStats,
  calculateClassMonthlyAverages,
  calculateClassLessonAverages,
  getGradeBadge
} from '../utils/calculations';

interface GradebookTableProps {
  classData: ClassData;
  onUpdateGrade: (studentId: string, lessonId: string, categoryId: string, value: number | undefined) => void;
  onSelectStudentForAnalytics: (student: Student) => void;
  onDeleteStudent: (studentId: string) => void;
  onAddLesson?: (monthId: string) => void;
}

export const GradebookTable: React.FC<GradebookTableProps> = ({
  classData,
  onUpdateGrade,
  onSelectStudentForAnalytics,
  onDeleteStudent,
  onAddLesson,
}) => {
  // State for expanded/collapsed months: by default expand the first month
  const [expandedMonths, setExpandedMonths] = useState<Record<string, boolean>>(() => {
    const initial: Record<string, boolean> = {};
    classData.months.forEach((m, idx) => {
      initial[m.id] = idx === 0;
    });
    return initial;
  });

  const [searchQuery, setSearchQuery] = useState('');
  const [trendFilter, setTrendFilter] = useState<'all' | 'gain' | 'drop'>('all');

  const toggleMonth = (monthId: string) => {
    setExpandedMonths((prev) => ({
      ...prev,
      [monthId]: !prev[monthId],
    }));
  };

  const expandAllMonths = () => {
    const next: Record<string, boolean> = {};
    classData.months.forEach((m) => (next[m.id] = true));
    setExpandedMonths(next);
  };

  const collapseAllMonths = () => {
    const next: Record<string, boolean> = {};
    classData.months.forEach((m) => (next[m.id] = false));
    setExpandedMonths(next);
  };

  // Precompute overall stats for all students
  const studentsWithStats = useMemo(() => {
    return classData.students.map((student) => {
      const stats = calculateStudentOverallStats(student, classData);
      return {
        student,
        stats,
      };
    });
  }, [classData]);

  // Filter students
  const filteredStudents = useMemo(() => {
    return studentsWithStats.filter(({ student, stats }) => {
      const matchesSearch =
        student.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (student.rollNo && student.rollNo.toLowerCase().includes(searchQuery.toLowerCase()));

      if (!matchesSearch) return false;
      if (trendFilter === 'gain') return stats.trend === 'gain';
      if (trendFilter === 'drop') return stats.trend === 'drop';
      return true;
    });
  }, [studentsWithStats, searchQuery, trendFilter]);

  // Class monthly averages
  const classMonthlyAverages = useMemo(() => {
    return calculateClassMonthlyAverages(classData);
  }, [classData]);

  const classLessonAverages = useMemo(() => {
    return calculateClassLessonAverages(classData);
  }, [classData]);

  const areAllExpanded = classData.months.length > 0 && classData.months.every((m) => expandedMonths[m.id]);

  // Total max points per single lesson
  const singleLessonCap = classData.categories.reduce((s, c) => s + c.defaultCap, 0);

  return (
    <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden flex flex-col transition-all">
      
      {/* Table Toolbar */}
      <div className="px-5 py-3.5 border-b border-slate-200 bg-slate-50 flex flex-wrap items-center justify-between gap-4">
        
        {/* Search and Filters */}
        <div className="flex items-center gap-3 flex-wrap">
          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search student or roll no..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9 pr-3 py-1.5 bg-white border border-slate-300 rounded-xl text-xs font-medium text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 w-56 shadow-sm transition"
            />
          </div>

          <div className="flex items-center gap-1 bg-slate-200/70 p-0.5 rounded-xl text-xs font-medium text-slate-600">
            <button
              onClick={() => setTrendFilter('all')}
              className={`px-3 py-1 rounded-lg transition-all ${
                trendFilter === 'all'
                  ? 'bg-white text-indigo-700 shadow-sm font-bold'
                  : 'hover:text-slate-900'
              }`}
            >
              All ({classData.students.length})
            </button>
            <button
              onClick={() => setTrendFilter('gain')}
              className={`px-3 py-1 rounded-lg flex items-center gap-1 transition-all ${
                trendFilter === 'gain'
                  ? 'bg-white text-emerald-700 shadow-sm font-bold'
                  : 'hover:text-slate-900'
              }`}
            >
              <TrendingUp className="w-3.5 h-3.5 text-emerald-600" />
              <span>Gaining</span>
            </button>
            <button
              onClick={() => setTrendFilter('drop')}
              className={`px-3 py-1 rounded-lg flex items-center gap-1 transition-all ${
                trendFilter === 'drop'
                  ? 'bg-white text-rose-700 shadow-sm font-bold'
                  : 'hover:text-slate-900'
              }`}
            >
              <TrendingDown className="w-3.5 h-3.5 text-rose-600" />
              <span>Dropping</span>
            </button>
          </div>
        </div>

        {/* Horizontal Month Expansion Controls */}
        <div className="flex items-center gap-2">
          <div className="hidden lg:flex items-center gap-1.5 mr-2 text-xs text-slate-500 font-semibold">
            <Calendar className="w-4 h-4 text-indigo-600" />
            <span>Schedule:</span>
          </div>

          {/* Month Mini-Pills for Quick Expansion */}
          <div className="hidden md:flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200">
            {classData.months.map((m) => {
              const isExp = !!expandedMonths[m.id];
              const monthLessonCount = classData.lessons.filter((l) => l.monthId === m.id).length;

              return (
                <button
                  key={m.id}
                  onClick={() => toggleMonth(m.id)}
                  className={`px-3 py-1 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 ${
                    isExp
                      ? 'bg-indigo-600 text-white shadow-sm'
                      : 'text-slate-700 hover:bg-slate-200 hover:text-slate-900'
                  }`}
                  title={isExp ? `Collapse ${m.name}` : `Expand ${m.name} (${monthLessonCount} Lessons)`}
                >
                  <span>{m.shortName}</span>
                  <span className="text-[10px] opacity-80">({monthLessonCount}d)</span>
                  <span className={`text-[10px] transform transition-transform duration-300 ${isExp ? 'rotate-90' : 'rotate-0'}`}>
                    ▸
                  </span>
                </button>
              );
            })}
          </div>

          <div className="h-4 w-px bg-slate-300 hidden md:block"></div>

          {areAllExpanded ? (
            <button
              onClick={collapseAllMonths}
              className="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-xl bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 transition shadow-sm"
              title="Collapse all months into compact summary view"
            >
              <Minimize2 className="w-3.5 h-3.5 text-slate-500" />
              <span>Collapse All Months</span>
            </button>
          ) : (
            <button
              onClick={expandAllMonths}
              className="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-xl bg-indigo-50 border border-indigo-200 hover:bg-indigo-100 text-indigo-700 transition shadow-sm"
              title="Expand all monthly schedules"
            >
              <Maximize2 className="w-3.5 h-3.5 text-indigo-600" />
              <span>Expand All Months</span>
            </button>
          )}
        </div>
      </div>

      {/* Main Gradebook Scrollable Grid */}
      <div className="overflow-x-auto relative">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            {/* ROW 1: Top Month Spans */}
            <tr className="bg-[#f1f5f9] text-slate-700 border-b border-slate-300">
              {/* Sticky Col 1 Header: Roll (SOLID BACKGROUND) */}
              <th
                rowSpan={3}
                style={{ width: 60, minWidth: 60, maxWidth: 60, left: 0 }}
                className="sticky z-30 bg-[#f1f5f9] px-2 py-3 font-bold text-slate-800 border-r border-slate-300 text-center"
              >
                Roll
              </th>

              {/* Sticky Col 2 Header: Student Name (SOLID BACKGROUND) */}
              <th
                rowSpan={3}
                style={{ width: 220, minWidth: 220, maxWidth: 220, left: 60 }}
                className="sticky z-30 bg-[#f1f5f9] px-4 py-3 font-bold text-slate-800 border-r border-slate-300"
              >
                Student Name
              </th>

              {/* Sticky Col 3 Header: Score & Standing (SOLID BACKGROUND, NO BLEED-THROUGH) */}
              <th
                rowSpan={3}
                style={{ width: 130, minWidth: 130, maxWidth: 130, left: 280 }}
                className="sticky z-30 bg-[#f1f5f9] px-3 py-3 font-bold text-slate-800 border-r-2 border-slate-300 text-center shadow-[6px_0_12px_rgba(0,0,0,0.06)]"
              >
                Overall % & Trend
              </th>

              {/* Month Group Headers */}
              {classData.months.map((month) => {
                const isExpanded = !!expandedMonths[month.id];
                const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);
                // Each lesson has categories.length + 1 (Day Total) columns, plus 2 for Month Total & %
                const colSpan = isExpanded
                  ? monthLessons.length * (classData.categories.length + 1) + 2
                  : 1;

                return (
                  <th
                    key={month.id}
                    colSpan={colSpan}
                    onClick={() => toggleMonth(month.id)}
                    className={`px-3 py-2.5 font-bold border-r-2 border-slate-300 select-none cursor-pointer transition-all duration-300 ${
                      isExpanded
                        ? 'bg-indigo-100 text-indigo-950 border-b border-indigo-300'
                        : 'bg-[#e2e8f0] hover:bg-[#cbd5e1] text-slate-800'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-3">
                      <div className="flex items-center gap-2">
                        <div
                          className={`w-5 h-5 rounded-full flex items-center justify-center transition-transform duration-300 ${
                            isExpanded ? 'rotate-180 bg-indigo-600 text-white' : 'rotate-0 bg-slate-300 text-slate-700'
                          }`}
                        >
                          <ChevronDown className="w-3.5 h-3.5" />
                        </div>
                        <span className="text-sm font-extrabold tracking-tight">
                          📅 {month.name}
                        </span>
                        <span className="text-[11px] font-semibold text-slate-600">
                          ({monthLessons.length} Scheduled Lessons)
                        </span>
                      </div>

                      <div className="flex items-center gap-2">
                        <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-white border border-slate-300 text-slate-700">
                          {isExpanded ? 'Click to Collapse' : 'Click to Expand Schedule'}
                        </span>
                      </div>
                    </div>
                  </th>
                );
              })}
            </tr>

            {/* ROW 2: Days / Lessons in each month */}
            <tr className="bg-[#f8fafc] text-slate-700 border-b border-slate-200 text-xs">
              {classData.months.map((month) => {
                const isExpanded = !!expandedMonths[month.id];
                const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);

                if (!isExpanded) {
                  return (
                    <th
                      key={`${month.id}-day-collapsed`}
                      rowSpan={2}
                      className="px-3 py-2 border-r-2 border-slate-300 text-center font-bold text-slate-700 min-w-[130px] bg-[#eef2f6]"
                    >
                      Month Total & %
                    </th>
                  );
                }

                return (
                  <React.Fragment key={`${month.id}-days-expanded`}>
                    {monthLessons.map((lesson) => (
                      <th
                        key={lesson.id}
                        colSpan={classData.categories.length + 1}
                        className="px-2 py-1.5 border-r border-slate-300 text-center font-bold bg-indigo-50/70 border-b border-slate-200"
                      >
                        <div className="flex items-center justify-center gap-1.5">
                          <Clock className="w-3 h-3 text-indigo-600" />
                          <span className="text-indigo-950 font-bold">{lesson.title}</span>
                          <span className="text-[10px] text-indigo-700 bg-white px-1.5 py-0.2 rounded border border-indigo-200">
                            {lesson.date}
                          </span>
                        </div>
                      </th>
                    ))}

                    {/* Month Summary Headers (Total & %) */}
                    <th
                      colSpan={2}
                      className="px-2 py-1.5 border-r-2 border-slate-300 text-center font-extrabold text-indigo-900 bg-indigo-100 border-b border-slate-200"
                    >
                      {month.shortName} Summary
                    </th>
                  </React.Fragment>
                );
              })}
            </tr>

            {/* ROW 3: Categories & Caps for each lesson */}
            <tr className="bg-[#f1f5f9] text-slate-600 border-b-2 border-slate-300 text-[11px]">
              {classData.months.map((month) => {
                const isExpanded = !!expandedMonths[month.id];
                const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);

                if (!isExpanded) return null;

                return (
                  <React.Fragment key={`${month.id}-cats-expanded`}>
                    {monthLessons.map((lesson) => (
                      <React.Fragment key={`${lesson.id}-cat-headers`}>
                        {classData.categories.map((cat) => (
                          <th
                            key={`${lesson.id}-${cat.id}-th`}
                            className="px-2 py-1.5 border-r border-slate-200 text-center min-w-[85px] bg-white font-bold text-slate-800"
                          >
                            <div className="truncate">{cat.name}</div>
                            <div className="text-[10px] text-indigo-700 font-semibold">
                              /{cat.defaultCap}
                            </div>
                          </th>
                        ))}
                        {/* Day Total */}
                        <th
                          key={`${lesson.id}-day-total`}
                          className="px-2 py-1.5 border-r border-slate-300 text-center min-w-[70px] bg-slate-100 font-bold text-slate-700"
                        >
                          <div>Total</div>
                          <div className="text-[10px] text-slate-500 font-normal">/{singleLessonCap}</div>
                        </th>
                      </React.Fragment>
                    ))}

                    {/* Month Total & Month % */}
                    <th className="px-2 py-1.5 border-r border-slate-200 text-center min-w-[75px] font-bold text-slate-800 bg-indigo-50">
                      Total
                    </th>
                    <th className="px-2 py-1.5 border-r-2 border-slate-300 text-center min-w-[90px] font-bold text-slate-800 bg-indigo-100">
                      Month %
                    </th>
                  </React.Fragment>
                );
              })}
            </tr>
          </thead>

          {/* Student Rows Body (SOLID OPAQUE BACKGROUNDS ON STICKY COLS!) */}
          <tbody className="divide-y divide-slate-200">
            {filteredStudents.length === 0 ? (
              <tr>
                <td colSpan={30} className="text-center py-16 text-slate-400">
                  <p className="text-sm font-semibold text-slate-600">No students found.</p>
                  <p className="text-xs text-slate-400">Click "Paste Roster" in the top bar to paste your real class list.</p>
                </td>
              </tr>
            ) : (
              filteredStudents.map(({ student, stats }, index) => {
                const gradeBadge = getGradeBadge(stats.overallAveragePercentage);

                return (
                  <tr
                    key={student.id}
                    className="hover:bg-indigo-50/40 transition-colors group"
                  >
                    {/* Sticky Col 1: Roll No (SOLID BG-WHITE, NO BLEED) */}
                    <td
                      style={{ width: 60, minWidth: 60, maxWidth: 60, left: 0 }}
                      className="sticky z-20 bg-white group-hover:bg-[#f8fafc] px-2 py-2.5 border-r border-slate-200 text-center font-mono text-slate-600 font-semibold"
                    >
                      {student.rollNo || index + 1}
                    </td>

                    {/* Sticky Col 2: Student Name (SOLID BG-WHITE, NO BLEED) */}
                    <td
                      style={{ width: 220, minWidth: 220, maxWidth: 220, left: 60 }}
                      className="sticky z-20 bg-white group-hover:bg-[#f8fafc] px-4 py-2.5 border-r border-slate-200"
                    >
                      <div className="flex items-center justify-between gap-2">
                        <button
                          onClick={() => onSelectStudentForAnalytics(student)}
                          className="font-bold text-slate-900 hover:text-indigo-600 text-left transition flex items-center gap-1 truncate"
                          title="Click to view student performance trajectory graph"
                        >
                          <span className="truncate">{student.name}</span>
                        </button>

                        <div className="flex items-center gap-1 opacity-70 group-hover:opacity-100 transition-opacity shrink-0">
                          <button
                            onClick={() => onSelectStudentForAnalytics(student)}
                            className="p-1 rounded-md text-slate-400 hover:text-indigo-600 hover:bg-indigo-100/60 transition"
                            title="Open performance graph"
                          >
                            <BarChart3 className="w-3.5 h-3.5 text-indigo-600" />
                          </button>

                          <button
                            onClick={() => {
                              if (window.confirm(`Remove "${student.name}" from this class?`)) {
                                onDeleteStudent(student.id);
                              }
                            }}
                            className="p-1 rounded-md text-slate-300 hover:text-rose-600 hover:bg-rose-50 transition"
                            title="Remove student"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </div>
                    </td>

                    {/* Sticky Col 3: Score & Trend (SOLID BG-WHITE, OPAQUE, SHADOW BORDER) */}
                    <td
                      style={{ width: 130, minWidth: 130, maxWidth: 130, left: 280 }}
                      className="sticky z-20 bg-white group-hover:bg-[#f8fafc] px-3 py-2.5 border-r-2 border-slate-300 text-center shadow-[6px_0_12px_rgba(0,0,0,0.06)]"
                    >
                      <div className="flex items-center justify-center gap-1.5">
                        <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold border ${gradeBadge.color}`}>
                          {gradeBadge.label}
                        </span>
                        <span className="font-extrabold text-slate-800 text-xs">
                          {stats.overallAveragePercentage}%
                        </span>
                        {stats.trend === 'gain' && (
                          <span title={`Recent Gain: +${stats.latestGainDrop}%`}>
                            <TrendingUp className="w-3.5 h-3.5 text-emerald-600" />
                          </span>
                        )}
                        {stats.trend === 'drop' && (
                          <span title={`Recent Drop: ${stats.latestGainDrop}%`}>
                            <TrendingDown className="w-3.5 h-3.5 text-rose-600" />
                          </span>
                        )}
                        {stats.trend === 'stable' && (
                          <span title="Consistent performance">
                            <Minus className="w-3 h-3 text-slate-400" />
                          </span>
                        )}
                      </div>
                    </td>

                    {/* Monthly Horizontal Columns */}
                    {classData.months.map((month) => {
                      const isExpanded = !!expandedMonths[month.id];
                      const mStats = stats.monthlyStats.find((m) => m.monthId === month.id);
                      const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);

                      // Collapsed View
                      if (!isExpanded) {
                        return (
                          <td
                            key={`${month.id}-collapsed`}
                            onClick={() => toggleMonth(month.id)}
                            className="px-3 py-2.5 border-r-2 border-slate-300 text-center bg-slate-50/50 cursor-pointer hover:bg-indigo-50/60 transition-colors"
                            title={`Click to expand ${month.name} (${monthLessons.length} lessons)`}
                          >
                            <div className="flex items-center justify-center gap-1.5">
                              <span className="font-bold text-slate-800">
                                {mStats?.totalScore || 0}
                              </span>
                              <span className="text-[10px] text-slate-400">/{mStats?.maxScore || 0}</span>
                              <span className="font-extrabold text-xs text-indigo-700 ml-1">
                                {mStats?.percentage || 0}%
                              </span>
                              {mStats?.gainDrop !== null && mStats?.gainDrop !== undefined && (
                                <span
                                  className={`text-[10px] font-bold px-1.5 py-0.5 rounded-full ml-1 ${
                                    mStats.gainDrop > 0
                                      ? 'bg-emerald-100 text-emerald-800'
                                      : mStats.gainDrop < 0
                                      ? 'bg-rose-100 text-rose-800'
                                      : 'bg-slate-100 text-slate-500'
                                  }`}
                                >
                                  {mStats.gainDrop > 0 ? `+${mStats.gainDrop}%` : `${mStats.gainDrop}%`}
                                </span>
                              )}
                            </div>
                          </td>
                        );
                      }

                      // Expanded View: Render each scheduled day/lesson and its categories
                      return (
                        <React.Fragment key={`${month.id}-expanded-lessons`}>
                          {monthLessons.map((lesson) => {
                            const lessonGrades = classData.grades[student.id]?.[lesson.id] || {};
                            let dayTotal = 0;

                            return (
                              <React.Fragment key={`${lesson.id}-data-cells`}>
                                {classData.categories.map((cat) => {
                                  const rawVal = lessonGrades[cat.id];
                                  const score = typeof rawVal === 'number' ? rawVal : undefined;
                                  if (score !== undefined) dayTotal += score;
                                  const isOverCap = typeof score === 'number' && score > cat.defaultCap;
                                  const pct = typeof score === 'number' && cat.defaultCap > 0
                                    ? Math.min(100, Math.max(0, (score / cat.defaultCap) * 100))
                                    : 0;

                                  return (
                                    <td
                                      key={`${lesson.id}-${cat.id}`}
                                      className={`px-1.5 py-1.5 border-r border-slate-200 text-center transition ${
                                        isOverCap ? 'bg-rose-50' : 'bg-white'
                                      }`}
                                    >
                                      <div className="relative inline-block w-full">
                                        <input
                                          type="number"
                                          min="0"
                                          max={cat.defaultCap}
                                          step="0.5"
                                          value={score !== undefined ? score : ''}
                                          onChange={(e) => {
                                            const val = e.target.value === '' ? undefined : parseFloat(e.target.value);
                                            onUpdateGrade(student.id, lesson.id, cat.id, isNaN(val as number) ? undefined : val);
                                          }}
                                          placeholder="—"
                                          className={`w-full text-center py-1 px-0.5 rounded-lg text-xs font-bold focus:outline-none focus:ring-2 transition-all ${
                                            isOverCap
                                              ? 'bg-rose-100 text-rose-800 ring-2 ring-rose-400'
                                              : score === cat.defaultCap
                                              ? 'bg-emerald-50 text-emerald-800 border border-emerald-300 font-extrabold'
                                              : 'bg-white text-slate-800 border border-slate-200 hover:border-slate-400 focus:ring-indigo-500'
                                          }`}
                                        />

                                        {/* Horizontal score gauge meter */}
                                        {score !== undefined && !isOverCap && (
                                          <div className="w-full h-1 bg-slate-100 rounded-full mt-0.5 overflow-hidden">
                                            <div
                                              className={`h-full transition-all duration-300 rounded-full ${
                                                pct >= 85 ? 'bg-emerald-500' : pct >= 70 ? 'bg-indigo-500' : 'bg-amber-500'
                                              }`}
                                              style={{ width: `${pct}%` }}
                                            />
                                          </div>
                                        )}
                                      </div>
                                    </td>
                                  );
                                })}

                                {/* Day Total */}
                                <td className="px-2 py-1.5 border-r border-slate-300 text-center font-bold text-slate-700 bg-slate-50">
                                  {dayTotal}
                                </td>
                              </React.Fragment>
                            );
                          })}

                          {/* Month Total & Month % */}
                          <td className="px-2 py-1.5 border-r border-slate-200 text-center font-extrabold text-slate-800 bg-indigo-50/50">
                            {mStats?.totalScore || 0}
                          </td>
                          <td className="px-2.5 py-1.5 border-r-2 border-slate-300 text-center bg-indigo-100/70">
                            <span className="font-extrabold text-xs text-indigo-950">
                              {mStats?.percentage || 0}%
                            </span>
                          </td>
                        </React.Fragment>
                      );
                    })}
                  </tr>
                );
              })
            )}
          </tbody>

          {/* Table Footer: Class Summary Averages (SOLID OPAQUE STICKY COLS!) */}
          <tfoot>
            <tr className="bg-[#f1f5f9] font-bold text-slate-800 border-t-2 border-slate-300">
              <td
                style={{ width: 60, minWidth: 60, maxWidth: 60, left: 0 }}
                className="sticky z-20 bg-[#f1f5f9] px-2 py-3 border-r border-slate-300 text-center text-slate-500"
              >
                —
              </td>
              <td
                style={{ width: 220, minWidth: 220, maxWidth: 220, left: 60 }}
                className="sticky z-20 bg-[#f1f5f9] px-4 py-3 border-r border-slate-300 font-extrabold text-indigo-950"
              >
                CLASS AVERAGE
              </td>
              <td
                style={{ width: 130, minWidth: 130, maxWidth: 130, left: 280 }}
                className="sticky z-20 bg-[#f1f5f9] px-3 py-3 border-r-2 border-slate-300 text-center font-extrabold text-indigo-700 shadow-[6px_0_12px_rgba(0,0,0,0.06)]"
              >
                {Math.round(
                  (Object.values(classMonthlyAverages).reduce((a, b) => a + b, 0) /
                    (Object.keys(classMonthlyAverages).length || 1)) *
                    10
                ) / 10}%
              </td>

              {classData.months.map((month) => {
                const isExpanded = !!expandedMonths[month.id];
                const avg = classMonthlyAverages[month.id] || 0;
                const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);

                if (!isExpanded) {
                  return (
                    <td
                      key={`footer-${month.id}-collapsed`}
                      className="px-3 py-3 border-r-2 border-slate-300 text-center font-extrabold text-indigo-900 bg-slate-200"
                    >
                      {avg}%
                    </td>
                  );
                }

                return (
                  <React.Fragment key={`footer-${month.id}-expanded`}>
                    {monthLessons.map((lesson) => {
                      const lessonAvg = classLessonAverages[lesson.id] || 0;

                      return (
                        <React.Fragment key={`footer-${lesson.id}`}>
                          {classData.categories.map((cat) => {
                            let sum = 0;
                            let count = 0;
                            classData.students.forEach((st) => {
                              const s = classData.grades[st.id]?.[lesson.id]?.[cat.id];
                              if (typeof s === 'number') {
                                sum += s;
                                count++;
                              }
                            });
                            const catAvg = count > 0 ? Math.round((sum / count) * 10) / 10 : 0;

                            return (
                              <td
                                key={`footer-${lesson.id}-${cat.id}`}
                                className="px-1.5 py-2 border-r border-slate-200 text-center text-slate-700 font-bold bg-slate-50"
                              >
                                {catAvg}
                              </td>
                            );
                          })}

                          {/* Day Avg */}
                          <td className="px-2 py-2 border-r border-slate-300 text-center font-bold text-slate-800 bg-slate-100">
                            {lessonAvg}%
                          </td>
                        </React.Fragment>
                      );
                    })}

                    <td className="px-2 py-3 border-r border-slate-200 text-center font-bold text-slate-700 bg-indigo-50">
                      —
                    </td>
                    <td className="px-2.5 py-3 border-r-2 border-slate-300 text-center font-extrabold text-indigo-900 bg-indigo-100">
                      {avg}%
                    </td>
                  </React.Fragment>
                );
              })}
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  );
};
