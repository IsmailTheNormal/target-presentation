import { ClassData, Category, MonthInfo, Lesson, Student, GradeMatrix } from '../types/gradebook';

/**
 * Serializes a ClassData object into a standardized XML format.
 */
export function exportToXML(classData: ClassData): string {
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
  xml += `<gradebook version="1.0" exportedAt="${new Date().toISOString()}">\n`;
  xml += `  <class id="${escapeXml(classData.id)}" name="${escapeXml(classData.name)}" subject="${escapeXml(classData.subject)}" academicYear="${escapeXml(classData.academicYear)}" gradeLevel="${escapeXml(classData.gradeLevel)}">\n`;

  // Categories
  xml += `    <categories>\n`;
  for (const cat of classData.categories) {
    xml += `      <category id="${escapeXml(cat.id)}" name="${escapeXml(cat.name)}" defaultCap="${cat.defaultCap}" color="${escapeXml(cat.color || '')}" />\n`;
  }
  xml += `    </categories>\n`;

  // Months
  xml += `    <months>\n`;
  for (const month of classData.months) {
    xml += `      <month id="${escapeXml(month.id)}" name="${escapeXml(month.name)}" shortName="${escapeXml(month.shortName)}" academicYear="${escapeXml(month.academicYear)}" />\n`;
  }
  xml += `    </months>\n`;

  // Lessons
  xml += `    <lessons>\n`;
  for (const lesson of classData.lessons) {
    xml += `      <lesson id="${escapeXml(lesson.id)}" monthId="${escapeXml(lesson.monthId)}" dayNumber="${lesson.dayNumber}" date="${escapeXml(lesson.date)}" title="${escapeXml(lesson.title)}" />\n`;
  }
  xml += `    </lessons>\n`;

  // Students
  xml += `    <students>\n`;
  for (const st of classData.students) {
    xml += `      <student id="${escapeXml(st.id)}" name="${escapeXml(st.name)}" rollNo="${escapeXml(st.rollNo || '')}" email="${escapeXml(st.email || '')}">\n`;
    if (st.notes) {
      xml += `        <notes>${escapeXml(st.notes)}</notes>\n`;
    }
    xml += `      </student>\n`;
  }
  xml += `    </students>\n`;

  // Grades Matrix
  xml += `    <grades>\n`;
  for (const studentId in classData.grades) {
    const studentLessons = classData.grades[studentId];
    for (const lessonId in studentLessons) {
      const lessonCats = studentLessons[lessonId];
      for (const catId in lessonCats) {
        const score = lessonCats[catId];
        if (score !== undefined) {
          xml += `      <grade studentId="${escapeXml(studentId)}" lessonId="${escapeXml(lessonId)}" categoryId="${escapeXml(catId)}" score="${score}" />\n`;
        }
      }
    }
  }
  xml += `    </grades>\n`;

  xml += `  </class>\n`;
  xml += `</gradebook>`;

  return xml;
}

/**
 * Parses XML text into a ClassData object.
 */
export function importFromXML(xmlText: string): ClassData {
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(xmlText, 'text/xml');

  const parserError = xmlDoc.getElementsByTagName('parsererror');
  if (parserError.length > 0) {
    throw new Error('Invalid XML format: ' + parserError[0].textContent);
  }

  const classElem = xmlDoc.querySelector('class');
  if (!classElem) {
    throw new Error('Missing <class> element in XML');
  }

  const classId = classElem.getAttribute('id') || `class-${Date.now()}`;
  const className = classElem.getAttribute('name') || 'Imported Class';
  const subject = classElem.getAttribute('subject') || 'General';
  const academicYear = classElem.getAttribute('academicYear') || '2026-2027';
  const gradeLevel = classElem.getAttribute('gradeLevel') || 'Grade 10';

  // Categories
  const categories: Category[] = [];
  const catNodes = xmlDoc.querySelectorAll('categories > category');
  catNodes.forEach((node) => {
    categories.push({
      id: node.getAttribute('id') || `cat-${Math.random().toString(36).substr(2, 5)}`,
      name: node.getAttribute('name') || 'Category',
      defaultCap: parseFloat(node.getAttribute('defaultCap') || '10') || 10,
      color: node.getAttribute('color') || '#4f46e5',
    });
  });

  // Months
  const months: MonthInfo[] = [];
  const monthNodes = xmlDoc.querySelectorAll('months > month');
  monthNodes.forEach((node) => {
    months.push({
      id: node.getAttribute('id') || 'm',
      name: node.getAttribute('name') || 'Month',
      shortName: node.getAttribute('shortName') || 'M',
      academicYear: node.getAttribute('academicYear') || academicYear,
    });
  });

  // Lessons
  const lessons: Lesson[] = [];
  const lessonNodes = xmlDoc.querySelectorAll('lessons > lesson');
  lessonNodes.forEach((node, idx) => {
    lessons.push({
      id: node.getAttribute('id') || `l-${idx}`,
      monthId: node.getAttribute('monthId') || months[0]?.id || 'sep',
      dayNumber: parseInt(node.getAttribute('dayNumber') || String(idx + 1)),
      date: node.getAttribute('date') || `Day ${idx + 1}`,
      title: node.getAttribute('title') || `Day ${idx + 1}`,
    });
  });

  // Students
  const students: Student[] = [];
  const studentNodes = xmlDoc.querySelectorAll('students > student');
  studentNodes.forEach((node) => {
    const notesElem = node.querySelector('notes');
    students.push({
      id: node.getAttribute('id') || `st-${Math.random().toString(36).substr(2, 5)}`,
      name: node.getAttribute('name') || 'Student',
      rollNo: node.getAttribute('rollNo') || '',
      email: node.getAttribute('email') || '',
      notes: notesElem ? notesElem.textContent || '' : '',
    });
  });

  // Grades
  const grades: GradeMatrix = {};
  const gradeNodes = xmlDoc.querySelectorAll('grades > grade');
  gradeNodes.forEach((node) => {
    const sId = node.getAttribute('studentId');
    const lId = node.getAttribute('lessonId') || node.getAttribute('monthId');
    const cId = node.getAttribute('categoryId');
    const scoreVal = parseFloat(node.getAttribute('score') || '0');

    if (sId && lId && cId && !isNaN(scoreVal)) {
      if (!grades[sId]) grades[sId] = {};
      if (!grades[sId][lId]) grades[sId][lId] = {};
      grades[sId][lId][cId] = scoreVal;
    }
  });

  return {
    id: classId,
    name: className,
    subject,
    academicYear,
    gradeLevel,
    categories: categories.length > 0 ? categories : [
      { id: 'att', name: 'Attendance', defaultCap: 5, color: '#10b981' },
      { id: 'part', name: 'Participation', defaultCap: 10, color: '#6366f1' },
      { id: 'hw', name: 'Homework', defaultCap: 10, color: '#f59e0b' },
    ],
    months: months.length > 0 ? months : [
      { id: 'sep', name: 'September', shortName: 'Sep', academicYear },
      { id: 'oct', name: 'October', shortName: 'Oct', academicYear },
    ],
    lessons: lessons.length > 0 ? lessons : [
      { id: 'sep-l1', monthId: 'sep', dayNumber: 1, date: 'Sep 02', title: 'Day 1' },
      { id: 'sep-l2', monthId: 'sep', dayNumber: 2, date: 'Sep 05', title: 'Day 2' },
    ],
    students,
    grades,
  };
}

export function downloadXMLFile(classData: ClassData, filename?: string) {
  const xml = exportToXML(classData);
  const blob = new Blob([xml], { type: 'application/xml;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename || `${classData.name.replace(/\s+/g, '_')}_gradebook.xml`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

function escapeXml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}
