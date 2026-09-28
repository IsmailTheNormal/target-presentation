import React, { useState } from 'react';
import { 
  X, 
  TrendingUp, 
  TrendingDown, 
  Minus, 
  Award, 
  Calendar, 
  CheckCircle2, 
  AlertTriangle,
  Printer,
  ChevronLeft,
  ChevronRight,
  BookOpen,
  Clock,
  Target
} from 'lucide-react';
import { 
  ResponsiveContainer, 
  LineChart, 
  Line, 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend, 
  ReferenceLine,
  Cell
} from 'recharts';
import { ClassData, Student } from '../types/gradebook';
import { 
  calculateStudentOverallStats, 
  calculateClassMonthlyAverages,
  calculateClassLessonAverages,
  getGradeBadge 
} from '../utils/calculations';

interface StudentAnalyticsModalProps {
  student: Student | null;
  classData: ClassData;
  onClose: () => void;
  onNavigateStudent: (direction: 'prev' | 'next') => void;
}

export const StudentAnalyticsModal: React.FC<StudentAnalyticsModalProps> = ({
  student,
  classData,
  onClose,
  onNavigateStudent,
}) => {
  const [activeChartTab, setActiveChartTab] = useState<'lessons' | 'monthly' | 'categories'>('lessons');

  if (!student) return null;

  const stats = calculateStudentOverallStats(student, classData);
  const classMonthlyAverages = calculateClassMonthlyAverages(classData);
  const classLessonAverages = calculateClassLessonAverages(classData);
  const gradeBadge = getGradeBadge(stats.overallAveragePercentage);

  // Lesson-by-lesson data
  const lessonChartData = stats.lessonTrajectory.map((l) => ({
    name: `${l.lessonTitle} (${l.lessonDate})`,
    studentScore: l.percentage,
    classAverage: classLessonAverages[l.lessonId] || 0,
    gainDrop: l.gainDropFromPrevLesson,
  }));

  // Monthly data
  const monthlyChartData = stats.monthlyStats.map((m) => ({
    name: m.monthShortName,
    studentScore: m.percentage,
    classAverage: classMonthlyAverages[m.monthId] || 0,
    gainDrop: m.gainDrop,
  }));

  // Category Mastery
  const categoryMasteryData = classData.categories.map((cat) => {
    let totalScore = 0;
    let totalCap = 0;

    classData.lessons.forEach((l) => {
      const score = classData.grades[student.id]?.[l.id]?.[cat.id];
      if (typeof score === 'number') {
        totalScore += score;
      }
      totalCap += cat.defaultCap;
    });

    const pct = totalCap > 0 ? Math.round((totalScore / totalCap) * 1000) / 10 : 0;
    return {
      category: cat.name,
      percentage: pct,
      totalScore,
      totalCap,
    };
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-5xl my-8 overflow-hidden transition-all">
        
        {/* Modal Header */}
        <div className="px-6 py-5 border-b border-slate-200 bg-gradient-to-r from-indigo-900 via-indigo-800 to-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 rounded-2xl bg-indigo-500/30 border border-indigo-400/40 flex items-center justify-center text-xl font-bold shadow-inner">
              {student.name.charAt(0)}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl font-bold tracking-tight">{student.name}</h2>
                <span className="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/30 border border-indigo-400/40 font-mono">
                  Roll: {student.rollNo || 'N/A'}
                </span>
              </div>
              <p className="text-xs text-indigo-200 mt-0.5">
                {classData.name} &bull; {classData.lessons.length} Lessons Scheduled across {classData.months.length} Months
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <div className="flex items-center bg-white/10 rounded-xl p-0.5 border border-white/20">
              <button
                onClick={() => onNavigateStudent('prev')}
                className="p-1.5 hover:bg-white/20 rounded-lg text-slate-200 hover:text-white transition"
                title="Previous Student"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
              <button
                onClick={() => onNavigateStudent('next')}
                className="p-1.5 hover:bg-white/20 rounded-lg text-slate-200 hover:text-white transition"
                title="Next Student"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>

            <button
              onClick={() => window.print()}
              className="p-2 bg-white/10 hover:bg-white/20 text-white rounded-xl border border-white/20 transition flex items-center gap-1.5 text-xs font-semibold"
              title="Print Report"
            >
              <Printer className="w-4 h-4" />
              <span className="hidden sm:inline">Print Report</span>
            </button>

            <button
              onClick={onClose}
              className="p-2 hover:bg-white/20 rounded-xl text-slate-300 hover:text-white transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-6">
          
          {/* Key Metric Cards */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            
            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between">
              <span className="text-xs font-medium text-slate-500">Overall Average</span>
              <div className="flex items-baseline gap-2 mt-2">
                <span className="text-3xl font-extrabold text-slate-900">
                  {stats.overallAveragePercentage}%
                </span>
                <span className={`text-xs px-2 py-0.5 rounded font-bold border ${gradeBadge.color}`}>
                  {gradeBadge.label}
                </span>
              </div>
              <span className="text-[11px] text-slate-400 mt-1">Across all scheduled lessons</span>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between">
              <span className="text-xs font-medium text-slate-500">Lesson Trajectory</span>
              <div className="flex items-center gap-2 mt-2">
                {stats.trend === 'gain' && (
                  <>
                    <div className="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center">
                      <TrendingUp className="w-5 h-5" />
                    </div>
                    <div>
                      <div className="text-sm font-bold text-emerald-700">Gaining</div>
                      <div className="text-[11px] text-emerald-600 font-semibold">
                        +{stats.latestGainDrop}% gain
                      </div>
                    </div>
                  </>
                )}
                {stats.trend === 'drop' && (
                  <>
                    <div className="w-8 h-8 rounded-lg bg-rose-100 text-rose-700 flex items-center justify-center">
                      <TrendingDown className="w-5 h-5" />
                    </div>
                    <div>
                      <div className="text-sm font-bold text-rose-700">Drop Detected</div>
                      <div className="text-[11px] text-rose-600 font-semibold">
                        {stats.latestGainDrop}% drop
                      </div>
                    </div>
                  </>
                )}
                {stats.trend === 'stable' && (
                  <>
                    <div className="w-8 h-8 rounded-lg bg-slate-200 text-slate-700 flex items-center justify-center">
                      <Minus className="w-5 h-5" />
                    </div>
                    <div>
                      <div className="text-sm font-bold text-slate-700">Steady</div>
                      <div className="text-[11px] text-slate-500 font-semibold">
                        Consistent marks
                      </div>
                    </div>
                  </>
                )}
                {stats.trend === 'insufficient_data' && (
                  <span className="text-xs text-slate-400 font-medium">Recorded</span>
                )}
              </div>
              <span className="text-[11px] text-slate-400 mt-1">Recent trend direction</span>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between">
              <span className="text-xs font-medium text-slate-500">Peak Month</span>
              <div className="flex items-center gap-2 mt-2">
                <div className="w-8 h-8 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center">
                  <Award className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-sm font-bold text-slate-800">
                    {stats.bestMonth || 'N/A'}
                  </div>
                  <div className="text-[11px] text-amber-700 font-semibold">
                    Best monthly score
                  </div>
                </div>
              </div>
              <span className="text-[11px] text-slate-400 mt-1">Highest achievement</span>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between">
              <span className="text-xs font-medium text-slate-500">Per-Lesson Mastery</span>
              <div className="mt-2">
                <div className="text-xs font-bold text-slate-800 flex items-center gap-1">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                  <span>Strong: {stats.strongestCategory || 'All'}</span>
                </div>
                {stats.weakestCategory && (
                  <div className="text-xs font-bold text-amber-700 flex items-center gap-1 mt-1">
                    <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                    <span>Focus: {stats.weakestCategory}</span>
                  </div>
                )}
              </div>
              <span className="text-[11px] text-slate-400 mt-1">Category breakdown</span>
            </div>

          </div>

          {/* Graph Section */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
            {/* Chart Tabs */}
            <div className="flex items-center justify-between border-b border-slate-200 pb-3 mb-4 flex-wrap gap-2">
              <div>
                <h3 className="text-sm font-bold text-slate-800">
                  Performance Gain & Drop Progression
                </h3>
                <p className="text-xs text-slate-500">
                  Visualizing student marks per scheduled lesson and month
                </p>
              </div>

              <div className="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-bold text-slate-600">
                <button
                  onClick={() => setActiveChartTab('lessons')}
                  className={`px-3 py-1.5 rounded-lg transition ${
                    activeChartTab === 'lessons'
                      ? 'bg-white text-indigo-700 shadow-sm'
                      : 'hover:text-slate-900'
                  }`}
                >
                  📅 Lesson-by-Lesson Trajectory
                </button>
                <button
                  onClick={() => setActiveChartTab('monthly')}
                  className={`px-3 py-1.5 rounded-lg transition ${
                    activeChartTab === 'monthly'
                      ? 'bg-white text-indigo-700 shadow-sm'
                      : 'hover:text-slate-900'
                  }`}
                >
                  📈 Month-over-Month
                </button>
                <button
                  onClick={() => setActiveChartTab('categories')}
                  className={`px-3 py-1.5 rounded-lg transition ${
                    activeChartTab === 'categories'
                      ? 'bg-white text-indigo-700 shadow-sm'
                      : 'hover:text-slate-900'
                  }`}
                >
                  🎯 Category Mastery
                </button>
              </div>
            </div>

            {/* Render Active Chart */}
            <div className="h-72 w-full pt-2">
              {activeChartTab === 'lessons' && (
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={lessonChartData} margin={{ top: 10, right: 30, left: -10, bottom: 25 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" vertical={false} />
                    <XAxis
                      dataKey="name"
                      stroke="#94a3b8"
                      tick={{ fontSize: 11, fill: '#64748b' }}
                      angle={-20}
                      textAnchor="end"
                    />
                    <YAxis
                      stroke="#94a3b8"
                      domain={[0, 100]}
                      tick={{ fontSize: 12, fill: '#64748b' }}
                      tickFormatter={(v) => `${v}%`}
                    />
                    <Tooltip
                      formatter={(val: any, name: string) => [
                        `${val}%`,
                        name === 'studentScore' ? `${student.name}` : 'Class Average',
                      ]}
                      contentStyle={{ backgroundColor: '#1e293b', borderRadius: '12px', color: '#fff', border: 'none' }}
                    />
                    <Legend verticalAlign="top" height={36} />
                    <Line
                      type="monotone"
                      dataKey="studentScore"
                      name={`${student.name} Score (%)`}
                      stroke="#4f46e5"
                      strokeWidth={3}
                      dot={{ r: 5, fill: '#4f46e5', strokeWidth: 2, stroke: '#fff' }}
                      activeDot={{ r: 7 }}
                    />
                    <Line
                      type="monotone"
                      dataKey="classAverage"
                      name="Class Lesson Average (%)"
                      stroke="#94a3b8"
                      strokeWidth={2}
                      strokeDasharray="4 4"
                      dot={false}
                    />
                  </LineChart>
                </ResponsiveContainer>
              )}

              {activeChartTab === 'monthly' && (
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={monthlyChartData} margin={{ top: 10, right: 30, left: -10, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" vertical={false} />
                    <XAxis dataKey="name" stroke="#94a3b8" tick={{ fontSize: 12, fill: '#64748b' }} />
                    <YAxis stroke="#94a3b8" domain={[0, 100]} tick={{ fontSize: 12, fill: '#64748b' }} tickFormatter={(v) => `${v}%`} />
                    <Tooltip
                      formatter={(val: any, name: string) => [
                        `${val}%`,
                        name === 'studentScore' ? `${student.name}` : 'Class Average',
                      ]}
                      contentStyle={{ backgroundColor: '#1e293b', borderRadius: '12px', color: '#fff', border: 'none' }}
                    />
                    <Legend />
                    <Line
                      type="monotone"
                      dataKey="studentScore"
                      name={`${student.name} (%)`}
                      stroke="#10b981"
                      strokeWidth={3}
                      dot={{ r: 6, fill: '#10b981', strokeWidth: 2, stroke: '#fff' }}
                      activeDot={{ r: 8 }}
                    />
                    <Line
                      type="monotone"
                      dataKey="classAverage"
                      name="Class Average (%)"
                      stroke="#94a3b8"
                      strokeWidth={2}
                      strokeDasharray="5 5"
                      dot={false}
                    />
                  </LineChart>
                </ResponsiveContainer>
              )}

              {activeChartTab === 'categories' && (
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={categoryMasteryData} layout="vertical" margin={{ top: 10, right: 30, left: 30, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" horizontal={false} />
                    <XAxis type="number" domain={[0, 100]} stroke="#94a3b8" tickFormatter={(v) => `${v}%`} />
                    <YAxis dataKey="category" type="category" stroke="#94a3b8" tick={{ fontSize: 12, fill: '#334155' }} />
                    <Tooltip
                      formatter={(val: any) => [`${val}%`, 'Category Mastery']}
                      contentStyle={{ backgroundColor: '#1e293b', borderRadius: '12px', color: '#fff', border: 'none' }}
                    />
                    <Bar dataKey="percentage" fill="#6366f1" radius={[0, 8, 8, 0]}>
                      {categoryMasteryData.map((entry, index) => (
                        <Cell
                          key={`cell-cat-${index}`}
                          fill={entry.percentage >= 85 ? '#10b981' : entry.percentage >= 70 ? '#6366f1' : '#f59e0b'}
                        />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              )}
            </div>
          </div>

          {/* Schedule Breakdown Table */}
          <div className="border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
            <div className="bg-slate-50 px-5 py-3 border-b border-slate-200">
              <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                Scheduled Lessons & Mark History
              </h4>
            </div>

            <div className="overflow-x-auto max-h-60">
              <table className="w-full text-xs text-left">
                <thead className="bg-slate-100 text-slate-600 border-b border-slate-200 sticky top-0">
                  <tr>
                    <th className="px-4 py-2 font-bold">Lesson / Day</th>
                    <th className="px-3 py-2 font-bold">Date</th>
                    {classData.categories.map((cat) => (
                      <th key={cat.id} className="px-3 py-2 font-semibold text-center">
                        {cat.name} (/{cat.defaultCap})
                      </th>
                    ))}
                    <th className="px-3 py-2 font-bold text-center">Day Score</th>
                    <th className="px-3 py-2 font-bold text-center">Percentage</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {classData.lessons.map((lesson) => {
                    const lGrades = classData.grades[student.id]?.[lesson.id] || {};
                    let dayTotal = 0;
                    let dayMax = 0;

                    classData.categories.forEach((cat) => {
                      const s = lGrades[cat.id];
                      if (typeof s === 'number') dayTotal += s;
                      dayMax += cat.defaultCap;
                    });

                    const pct = dayMax > 0 ? Math.round((dayTotal / dayMax) * 1000) / 10 : 0;
                    const grade = getGradeBadge(pct);

                    return (
                      <tr key={lesson.id} className="hover:bg-slate-50 transition">
                        <td className="px-4 py-2 font-bold text-slate-800">{lesson.title}</td>
                        <td className="px-3 py-2 text-slate-600">{lesson.date}</td>
                        {classData.categories.map((cat) => (
                          <td key={cat.id} className="px-3 py-2 text-center text-slate-700">
                            <span className="font-semibold">{lGrades[cat.id] ?? '—'}</span>
                            <span className="text-[10px] text-slate-400">/{cat.defaultCap}</span>
                          </td>
                        ))}
                        <td className="px-3 py-2 text-center font-bold text-slate-800">
                          {dayTotal} <span className="text-[10px] text-slate-400">/{dayMax}</span>
                        </td>
                        <td className="px-3 py-2 text-center">
                          <span className={`px-2 py-0.5 rounded font-bold border ${grade.color}`}>
                            {pct}%
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};
