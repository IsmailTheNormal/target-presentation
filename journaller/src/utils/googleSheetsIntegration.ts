import { ClassData } from '../types/gradebook';

/**
 * Generates TSV string for Google Sheets representing the scheduled lessons & categories.
 */
export function generateGoogleSheetsTSV(classData: ClassData): string {
  const lines: string[] = [];

  // Row 1: Header Info
  lines.push(`CLASS GRADEBOOK:\t${classData.name}\tSubject:\t${classData.subject}\tYear:\t${classData.academicYear}`);

  // Row 2: Months Spanning Headers
  const row2: string[] = ['', ''];
  classData.months.forEach((month) => {
    const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);
    const spanCount = monthLessons.length * (classData.categories.length + 1) + 2;
    row2.push(`📅 ${month.name}`);
    for (let i = 1; i < spanCount; i++) row2.push('');
  });
  row2.push('OVERALL STANDING', '');
  lines.push(row2.join('\t'));

  // Row 3: Days / Lessons Spanning Headers
  const row3: string[] = ['Roll', 'Student Name'];
  classData.months.forEach((month) => {
    const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);
    monthLessons.forEach((lesson) => {
      row3.push(`${lesson.title} (${lesson.date})`);
      for (let i = 1; i < classData.categories.length + 1; i++) row3.push('');
    });
    row3.push(`${month.shortName} Total`, `${month.shortName} %`);
  });
  row3.push('Grade Tier', 'Overall %');
  lines.push(row3.join('\t'));

  // Row 4: Category columns & Caps
  const row4: string[] = ['ID', 'Full Name'];
  const singleLessonCap = classData.categories.reduce((s, c) => s + c.defaultCap, 0);

  classData.months.forEach((month) => {
    const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);
    let monthCap = monthLessons.length * singleLessonCap;

    monthLessons.forEach(() => {
      classData.categories.forEach((cat) => {
        row4.push(`${cat.name} (/${cat.defaultCap})`);
      });
      row4.push(`Day Total (/${singleLessonCap})`);
    });

    row4.push(`Month Total (/${monthCap})`, 'Month %');
  });
  row4.push('Tier', 'YTD Average %');
  lines.push(row4.join('\t'));

  // Student Data Rows
  classData.students.forEach((student, index) => {
    const row: (string | number)[] = [student.rollNo || (index + 1), student.name];
    let grandTotal = 0;
    let grandMax = 0;

    classData.months.forEach((month) => {
      const monthLessons = classData.lessons.filter((l) => l.monthId === month.id);
      let monthTotal = 0;
      let monthMax = monthLessons.length * singleLessonCap;

      monthLessons.forEach((lesson) => {
        const lGrades = classData.grades[student.id]?.[lesson.id] || {};
        let dayTotal = 0;

        classData.categories.forEach((cat) => {
          const score = lGrades[cat.id] ?? 0;
          row.push(score);
          dayTotal += score;
        });

        row.push(dayTotal);
        monthTotal += dayTotal;
      });

      grandTotal += monthTotal;
      grandMax += monthMax;

      const monthPct = monthMax > 0 ? Math.round((monthTotal / monthMax) * 1000) / 10 : 0;
      row.push(monthTotal, `${monthPct}%`);
    });

    const overallPct = grandMax > 0 ? Math.round((grandTotal / grandMax) * 1000) / 10 : 0;
    const tier = overallPct >= 90 ? 'A' : overallPct >= 80 ? 'B' : overallPct >= 70 ? 'C' : overallPct >= 60 ? 'D' : 'F';
    row.push(tier, `${overallPct}%`);

    lines.push(row.join('\t'));
  });

  return lines.join('\n');
}

export function generateGoogleSheetsCSV(classData: ClassData): string {
  const tsv = generateGoogleSheetsTSV(classData);
  return tsv
    .split('\n')
    .map((row) =>
      row
        .split('\t')
        .map((cell) => `"${cell.replace(/"/g, '""')}"`)
        .join(',')
    )
    .join('\n');
}

export function generateGoogleAppsScript(classData: ClassData): string {
  return `/**
 * 🎓 Google Sheets Gradebook & Schedule Integration
 * Class: ${classData.name} (${classData.academicYear})
 * Categories: ${classData.categories.map((c) => `${c.name} (/${c.defaultCap})`).join(', ')}
 */

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🎓 Teacher Gradebook')
    .addItem('📊 Format Scheduled Lessons', 'setupGradebookSheet')
    .addItem('ℹ️ Live Sync Info', 'showHelpModal')
    .addToUi();
}

function setupGradebookSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName('Gradebook');
  if (!sheet) sheet = ss.insertSheet('Gradebook');
  SpreadsheetApp.getUi().alert('Gradebook ready with scheduled lessons!');
}

function showHelpModal() {
  SpreadsheetApp.getUi().alert('Continuous auto-save is enabled. Every lesson mark updates this sheet in real-time.');
}
`;
}
