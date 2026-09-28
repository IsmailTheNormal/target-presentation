import { ClassData, Student, StudentMonthStats, StudentOverallStats, LessonScoreStats } from '../types/gradebook';

/**
 * Computes stats for each scheduled lesson/day for a student.
 */
export function calculateStudentLessonStats(
  studentId: string,
  classData: ClassData
): LessonScoreStats[] {
  const result: LessonScoreStats[] = [];

  for (const lesson of classData.lessons) {
    let totalScore = 0;
    let maxScore = 0;
    const categoryBreakdown = [];

    const lessonGrades = classData.grades[studentId]?.[lesson.id] || {};

    for (const cat of classData.categories) {
      const rawScore = lessonGrades[cat.id];
      const score = typeof rawScore === 'number' ? rawScore : 0;
      const cap = cat.defaultCap;

      totalScore += score;
      maxScore += cap;

      categoryBreakdown.push({
        categoryId: cat.id,
        categoryName: cat.name,
        score,
        cap,
      });
    }

    const percentage = maxScore > 0 ? Math.round((totalScore / maxScore) * 1000) / 10 : 0;

    result.push({
      lessonId: lesson.id,
      lessonTitle: lesson.title,
      lessonDate: lesson.date,
      monthId: lesson.monthId,
      totalScore,
      maxScore,
      percentage,
      categoryBreakdown,
    });
  }

  return result;
}

/**
 * Computes monthly performance metrics by aggregating all lessons in each month.
 */
export function calculateStudentMonthlyStats(
  studentId: string,
  classData: ClassData
): StudentMonthStats[] {
  const allLessonStats = calculateStudentLessonStats(studentId, classData);
  const result: StudentMonthStats[] = [];
  let prevPercentage: number | null = null;

  for (const month of classData.months) {
    const monthLessons = allLessonStats.filter((ls) => ls.monthId === month.id);
    const monthLessonDefs = classData.lessons.filter((l) => l.monthId === month.id);

    let totalScore = 0;
    let maxScore = 0;

    // Category totals for this month
    const catSums: Record<string, { score: number; cap: number; name: string }> = {};
    classData.categories.forEach((cat) => {
      catSums[cat.id] = { score: 0, cap: 0, name: cat.name };
    });

    monthLessons.forEach((ls) => {
      totalScore += ls.totalScore;
      maxScore += ls.maxScore;

      ls.categoryBreakdown.forEach((cb) => {
        if (catSums[cb.categoryId]) {
          catSums[cb.categoryId].score += cb.score;
          catSums[cb.categoryId].cap += cb.cap;
        }
      });
    });

    const categoryBreakdown = Object.keys(catSums).map((catId) => {
      const item = catSums[catId];
      const pct = item.cap > 0 ? Math.round((item.score / item.cap) * 1000) / 10 : 0;
      return {
        categoryId: catId,
        categoryName: item.name,
        score: item.score,
        cap: item.cap,
        percentage: pct,
      };
    });

    const percentage = maxScore > 0 ? Math.round((totalScore / maxScore) * 1000) / 10 : 0;

    let gainDrop: number | null = null;
    if (prevPercentage !== null) {
      gainDrop = Math.round((percentage - prevPercentage) * 10) / 10;
    }

    result.push({
      monthId: month.id,
      monthName: month.name,
      monthShortName: month.shortName,
      lessonCount: monthLessonDefs.length,
      totalScore,
      maxScore,
      percentage,
      previousPercentage: prevPercentage,
      gainDrop,
      lessonStats: monthLessons,
      categoryBreakdown,
    });

    if (maxScore > 0) {
      prevPercentage = percentage;
    }
  }

  return result;
}

/**
 * Computes overall student statistics, lesson trajectories, trends, and category mastery.
 */
export function calculateStudentOverallStats(
  student: Student,
  classData: ClassData
): StudentOverallStats {
  const monthlyStats = calculateStudentMonthlyStats(student.id, classData);
  const allLessonStats = calculateStudentLessonStats(student.id, classData);

  // Lesson trajectory with lesson-over-lesson delta
  let prevLessonPct: number | null = null;
  const lessonTrajectory = allLessonStats.map((ls) => {
    let delta: number | null = null;
    if (prevLessonPct !== null) {
      delta = Math.round((ls.percentage - prevLessonPct) * 10) / 10;
    }
    prevLessonPct = ls.percentage;

    return {
      lessonId: ls.lessonId,
      lessonTitle: ls.lessonTitle,
      lessonDate: ls.lessonDate,
      percentage: ls.percentage,
      totalScore: ls.totalScore,
      maxScore: ls.maxScore,
      gainDropFromPrevLesson: delta,
    };
  });

  const activeMonths = monthlyStats.filter((m) => m.maxScore > 0);
  const overallAveragePercentage = activeMonths.length > 0
    ? Math.round(
        (activeMonths.reduce((sum, m) => sum + m.percentage, 0) / activeMonths.length) * 10
      ) / 10
    : 0;

  // Latest non-null gain/drop
  let latestGainDrop: number | null = null;
  for (let i = monthlyStats.length - 1; i >= 1; i--) {
    if (monthlyStats[i].gainDrop !== null) {
      latestGainDrop = monthlyStats[i].gainDrop;
      break;
    }
  }

  // Trend determination
  let trend: 'gain' | 'drop' | 'stable' | 'insufficient_data' = 'stable';
  if (latestGainDrop !== null) {
    if (latestGainDrop >= 1.5) trend = 'gain';
    else if (latestGainDrop <= -1.5) trend = 'drop';
    else trend = 'stable';
  } else if (activeMonths.length <= 1) {
    trend = 'insufficient_data';
  }

  // Best month
  let bestMonth: string | null = null;
  let maxMonthPct = -1;
  for (const m of activeMonths) {
    if (m.percentage > maxMonthPct) {
      maxMonthPct = m.percentage;
      bestMonth = m.monthName;
    }
  }

  // Category aggregates across all lessons
  const catSums: Record<string, { totalScore: number; totalCap: number; name: string }> = {};
  for (const cat of classData.categories) {
    catSums[cat.id] = { totalScore: 0, totalCap: 0, name: cat.name };
  }

  for (const m of monthlyStats) {
    for (const cb of m.categoryBreakdown) {
      if (catSums[cb.categoryId]) {
        catSums[cb.categoryId].totalScore += cb.score;
        catSums[cb.categoryId].totalCap += cb.cap;
      }
    }
  }

  let weakestCategory: string | null = null;
  let strongestCategory: string | null = null;
  let minCatPct = 999;
  let maxCatPct = -1;

  for (const catId in catSums) {
    const item = catSums[catId];
    if (item.totalCap > 0) {
      const pct = (item.totalScore / item.totalCap) * 100;
      if (pct < minCatPct) {
        minCatPct = pct;
        weakestCategory = item.name;
      }
      if (pct > maxCatPct) {
        maxCatPct = pct;
        strongestCategory = item.name;
      }
    }
  }

  return {
    student,
    monthlyStats,
    lessonTrajectory,
    overallAveragePercentage,
    trend,
    latestGainDrop,
    bestMonth,
    weakestCategory,
    strongestCategory,
  };
}

/**
 * Calculates class-wide monthly average percentages.
 */
export function calculateClassMonthlyAverages(classData: ClassData): Record<string, number> {
  const averages: Record<string, number> = {};

  for (const month of classData.months) {
    let sum = 0;
    let count = 0;
    for (const student of classData.students) {
      const studentStats = calculateStudentMonthlyStats(student.id, classData);
      const mStat = studentStats.find((s) => s.monthId === month.id);
      if (mStat && mStat.maxScore > 0) {
        sum += mStat.percentage;
        count++;
      }
    }
    averages[month.id] = count > 0 ? Math.round((sum / count) * 10) / 10 : 0;
  }

  return averages;
}

/**
 * Calculates class-wide average for each scheduled lesson/day.
 */
export function calculateClassLessonAverages(classData: ClassData): Record<string, number> {
  const averages: Record<string, number> = {};

  for (const lesson of classData.lessons) {
    let sum = 0;
    let count = 0;
    for (const student of classData.students) {
      const lStats = calculateStudentLessonStats(student.id, classData);
      const stat = lStats.find((s) => s.lessonId === lesson.id);
      if (stat && stat.maxScore > 0) {
        sum += stat.percentage;
        count++;
      }
    }
    averages[lesson.id] = count > 0 ? Math.round((sum / count) * 10) / 10 : 0;
  }

  return averages;
}

export function getGradeBadge(percentage: number) {
  if (percentage >= 90) return { label: 'A', color: 'bg-emerald-100 text-emerald-800 border-emerald-300' };
  if (percentage >= 80) return { label: 'B', color: 'bg-blue-100 text-blue-800 border-blue-300' };
  if (percentage >= 70) return { label: 'C', color: 'bg-amber-100 text-amber-800 border-amber-300' };
  if (percentage >= 60) return { label: 'D', color: 'bg-orange-100 text-orange-800 border-orange-300' };
  return { label: 'F', color: 'bg-rose-100 text-rose-800 border-rose-300' };
}
