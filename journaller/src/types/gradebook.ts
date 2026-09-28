export interface Category {
  id: string;
  name: string;
  defaultCap: number; // Max points per lesson for this category (e.g. Attendance: 5, Participation: 10, Homework: 10)
  color?: string;
  description?: string;
}

export interface MonthInfo {
  id: string;
  name: string;
  shortName: string;
  academicYear: string;
}

export interface Lesson {
  id: string;
  monthId: string;
  dayNumber: number;
  date: string; // e.g. "Sep 02", "Sep 05"
  title: string; // e.g. "Day 1", "Lesson 1: Intro"
}

export interface Student {
  id: string;
  name: string;
  rollNo?: string;
  email?: string;
  notes?: string;
}

// StudentId -> LessonId -> CategoryId -> Score
export type GradeMatrix = Record<string, Record<string, Record<string, number | undefined>>>;

export interface ClassData {
  id: string;
  name: string;
  gradeLevel: string;
  academicYear: string;
  subject: string;
  categories: Category[]; // Categories evaluated each lesson
  months: MonthInfo[];
  lessons: Lesson[]; // Scheduled days/lessons in the class
  students: Student[];
  grades: GradeMatrix;
}

export interface LessonScoreStats {
  lessonId: string;
  lessonTitle: string;
  lessonDate: string;
  monthId: string;
  totalScore: number;
  maxScore: number;
  percentage: number;
  categoryBreakdown: {
    categoryId: string;
    categoryName: string;
    score: number;
    cap: number;
  }[];
}

export interface StudentMonthStats {
  monthId: string;
  monthName: string;
  monthShortName: string;
  lessonCount: number;
  totalScore: number;
  maxScore: number;
  percentage: number;
  previousPercentage: number | null;
  gainDrop: number | null; // e.g. +5.2% or -3.1%
  lessonStats: LessonScoreStats[];
  categoryBreakdown: {
    categoryId: string;
    categoryName: string;
    score: number;
    cap: number;
    percentage: number;
  }[];
}

export interface StudentOverallStats {
  student: Student;
  monthlyStats: StudentMonthStats[];
  lessonTrajectory: {
    lessonId: string;
    lessonTitle: string;
    lessonDate: string;
    percentage: number;
    totalScore: number;
    maxScore: number;
    gainDropFromPrevLesson: number | null;
  }[];
  overallAveragePercentage: number;
  trend: 'gain' | 'drop' | 'stable' | 'insufficient_data';
  latestGainDrop: number | null;
  bestMonth: string | null;
  weakestCategory: string | null;
  strongestCategory: string | null;
}
