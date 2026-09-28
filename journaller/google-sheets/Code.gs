/**
 * ==============================================================================
 * 🎓 TEACHER GRADEBOOK CONTINUOUS AUTO-SYNC SCRIPT (PRODUCTION)
 * ==============================================================================
 * This script runs in your Google Sheet and acts as a LIVE 2-WAY API.
 * Whenever you type or edit grades in the Journaller Web App, it continuously
 * saves and updates this Google Sheet in real time!
 * 
 * QUICK SETUP (2 MINUTES):
 * 1. In your Google Sheet, click Extensions > Apps Script
 * 2. Delete existing code, paste this ENTIRE file, and click Save (Ctrl+S)
 * 3. Click "Deploy" (top right) > "New deployment"
 * 4. Select type: "Web app"
 * 5. Configuration:
 *    - Description: "Gradebook Continuous Sync"
 *    - Execute as: "Me"
 *    - Who has access: "Anyone" (allows your web app to save marks)
 * 6. Click "Deploy", authorize permissions, and COPY the Web App URL!
 * 7. Paste that URL into the Journaller Web App to enable continuous live sync!
 * ==============================================================================
 */

const SHEET_NAME = 'Gradebook';

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🎓 Teacher Gradebook')
    .addItem('📊 Format & Group Columns', 'setupEmptyGradebook')
    .addItem('📈 Open Student Analytics Tab', 'setupStudentChartTab')
    .addSeparator()
    .addItem('ℹ️ Continuous Auto-Sync Info', 'showSyncInfo')
    .addToUi();
}

/**
 * Handles incoming continuous updates from the Journaller Web App.
 * Uses ContentService with CORS support.
 */
function doPost(e) {
  try {
    let postDataString = '';
    if (e && e.postData && e.postData.contents) {
      postDataString = e.postData.contents;
    } else {
      return responseJSON({ status: 'error', message: 'No payload received' });
    }

    const payload = JSON.parse(postDataString);
    const action = payload.action || 'sync_all';

    if (action === 'sync_all') {
      const classData = payload.classData;
      if (!classData) {
        return responseJSON({ status: 'error', message: 'Missing classData' });
      }

      writeClassDataToSheet(classData);

      return responseJSON({
        status: 'success',
        message: 'Successfully updated Google Sheet',
        updatedAt: new Date().toISOString(),
        studentCount: classData.students ? classData.students.length : 0
      });
    }

    if (action === 'test_connection') {
      return responseJSON({
        status: 'success',
        message: 'Google Sheets Live Sync Connected Successfully!',
        sheetTitle: SpreadsheetApp.getActiveSpreadsheet().getName()
      });
    }

    return responseJSON({ status: 'error', message: 'Unknown action' });
  } catch (err) {
    Logger.log('doPost Error: ' + err.toString());
    return responseJSON({ status: 'error', message: err.toString() });
  }
}

/**
 * Handles GET requests to pull current data or check status.
 */
function doGet(e) {
  try {
    const action = (e && e.parameter && e.parameter.action) ? e.parameter.action : 'ping';
    
    if (action === 'get_data') {
      const classData = readClassDataFromSheet();
      return responseJSON({ status: 'success', classData: classData });
    }

    return responseJSON({
      status: 'success',
      message: 'Teacher Gradebook Sync Endpoint is LIVE',
      sheetTitle: SpreadsheetApp.getActiveSpreadsheet().getName(),
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    return responseJSON({ status: 'error', message: err.toString() });
  }
}

function responseJSON(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Batch updates the Gradebook sheet with the incoming live class data.
 */
function writeClassDataToSheet(classData) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME, 0);
  }

  // Clear previous groups & values
  sheet.clearColumnsGroups();
  sheet.clear();

  const categories = classData.categories || [];
  const months = classData.months || [];
  const students = classData.students || [];
  const grades = classData.grades || {};

  const totalMonthCap = categories.reduce((sum, c) => sum + (c.defaultCap || 0), 0);

  // Row 1 & 2: Title Block
  sheet.getRange('A1').setValue(classData.name || 'CLASS GRADEBOOK')
    .setFontSize(14).setFontWeight('bold').setFontColor('#0f172a');
  sheet.getRange('A2').setValue('Subject: ' + (classData.subject || '') + ' | Year: ' + (classData.academicYear || '') + ' | Live Synced')
    .setFontSize(10).setFontStyle('italic').setFontColor('#64748b');

  // Headers
  sheet.getRange('A4').setValue('Roll').setFontWeight('bold').setBackground('#f8fafc').setHorizontalAlignment('center');
  sheet.getRange('A5').setValue('ID').setFontWeight('bold').setBackground('#f8fafc').setHorizontalAlignment('center');
  sheet.getRange('B4').setValue('Student Name').setFontWeight('bold').setBackground('#f8fafc');
  sheet.getRange('B5').setValue('Full Name').setFontWeight('bold').setBackground('#f8fafc');

  sheet.setColumnWidth(1, 65);
  sheet.setColumnWidth(2, 220);

  let col = 3;
  const monthGroupRanges = [];
  const monthPctColumns = [];

  months.forEach((month, mIdx) => {
    const startMonthCol = col;
    const isOdd = mIdx % 2 === 0;
    const monthBg = isOdd ? '#e0e7ff' : '#eef2f6';

    // Categories
    categories.forEach(cat => {
      sheet.getRange(5, col).setValue(cat.name + '\n(Max ' + cat.defaultCap + ')')
        .setFontWeight('bold').setFontSize(9).setBackground(monthBg)
        .setHorizontalAlignment('center').setWrap(true);
      sheet.setColumnWidth(col, 100);
      col++;
    });

    const catCount = categories.length;

    // Month Total
    sheet.getRange(5, col).setValue('Total\n(/' + totalMonthCap + ')')
      .setFontWeight('bold').setFontSize(10).setBackground('#f1f5f9')
      .setHorizontalAlignment('center').setWrap(true);
    sheet.setColumnWidth(col, 85);
    col++;

    // Month %
    const pctCol = col;
    monthPctColumns.push(pctCol);
    sheet.getRange(5, col).setValue(month.shortName + ' %\n(Gain/Drop)')
      .setFontWeight('bold').setFontSize(10).setBackground('#fef3c7')
      .setHorizontalAlignment('center').setWrap(true);
    sheet.setColumnWidth(col, 105);
    col++;

    const endMonthCol = col - 1;

    // Merge month header
    sheet.getRange(4, startMonthCol, 1, endMonthCol - startMonthCol + 1)
      .merge()
      .setValue('📅 ' + month.name)
      .setFontWeight('bold').setFontSize(11).setFontColor('#0f172a')
      .setBackground(monthBg).setHorizontalAlignment('center');

    // Group categories for native [+] / [-] collapsible controls
    if (catCount > 0) {
      monthGroupRanges.push({ start: startMonthCol, count: catCount });
    }
  });

  // Overall Columns
  sheet.getRange(4, col).setValue('OVERALL').setFontWeight('bold').setBackground('#dcfce7').setHorizontalAlignment('center');
  sheet.getRange(5, col).setValue('Average %').setFontWeight('bold').setBackground('#dcfce7').setHorizontalAlignment('center');
  sheet.setColumnWidth(col, 120);
  const overallCol = col;
  col++;

  sheet.getRange(4, col).setValue('STANDING').setFontWeight('bold').setBackground('#dcfce7').setHorizontalAlignment('center');
  sheet.getRange(5, col).setValue('Grade Tier').setFontWeight('bold').setBackground('#dcfce7').setHorizontalAlignment('center');
  sheet.setColumnWidth(col, 95);

  const startRow = 6;
  const numCols = col;

  // Insert Student Rows with Values & Formulas
  if (students.length > 0) {
    const dataMatrix = [];

    students.forEach((student, sIdx) => {
      const rowNum = startRow + sIdx;
      const row = [student.rollNo || (sIdx + 1), student.name];

      let cOffset = 3;
      const pctRefs = [];

      months.forEach(month => {
        const studentMonthGrades = grades[student.id]?.[month.id] || {};
        const catStartColLet = getColLetter(cOffset);

        categories.forEach(cat => {
          const val = studentMonthGrades[cat.id];
          row.push(val !== undefined && val !== null ? val : '');
          cOffset++;
        });

        const catEndColLet = getColLetter(cOffset - 1);
        const totalColLet = getColLetter(cOffset);

        // Formula for Total
        row.push('=SUM(' + catStartColLet + rowNum + ':' + catEndColLet + rowNum + ')');
        cOffset++;

        // Formula for %
        row.push('=IF(' + totalColLet + rowNum + '>0, ' + totalColLet + rowNum + '/' + totalMonthCap + ', 0)');
        pctRefs.push(getColLetter(cOffset) + rowNum);
        cOffset++;
      });

      // Overall Average
      row.push('=AVERAGE(' + pctRefs.join(',') + ')');

      // Grade Tier
      const ovLet = getColLetter(overallCol);
      row.push('=IF(' + ovLet + rowNum + '>=0.9,"A",IF(' + ovLet + rowNum + '>=0.8,"B",IF(' + ovLet + rowNum + '>=0.7,"C",IF(' + ovLet + rowNum + '>=0.6,"D","F"))))');

      dataMatrix.push(row);
    });

    sheet.getRange(startRow, 1, dataMatrix.length, dataMatrix[0].length).setValues(dataMatrix);

    // Format Percentages
    monthPctColumns.forEach(pCol => {
      sheet.getRange(startRow, pCol, students.length, 1)
        .setNumberFormat('0.0%').setHorizontalAlignment('center').setFontWeight('bold');
    });
    sheet.getRange(startRow, overallCol, students.length, 1)
      .setNumberFormat('0.0%').setHorizontalAlignment('center').setFontWeight('bold');
    sheet.getRange(startRow, overallCol + 1, students.length, 1)
      .setHorizontalAlignment('center').setFontWeight('bold');

    // Class Average Summary Row
    const avgRow = startRow + students.length;
    sheet.getRange(avgRow, 1).setValue('—').setHorizontalAlignment('center');
    sheet.getRange(avgRow, 2).setValue('CLASS AVERAGE').setFontWeight('bold').setFontColor('#1e40af');

    let c = 3;
    months.forEach(() => {
      categories.forEach(() => {
        const colLet = getColLetter(c);
        sheet.getRange(avgRow, c).setFormula('=AVERAGE(' + colLet + startRow + ':' + colLet + (avgRow - 1) + ')')
          .setHorizontalAlignment('center');
        c++;
      });
      // total
      const totLet = getColLetter(c);
      sheet.getRange(avgRow, c).setFormula('=AVERAGE(' + totLet + startRow + ':' + totLet + (avgRow - 1) + ')')
        .setHorizontalAlignment('center').setFontWeight('bold');
      c++;
      // pct
      const pctLet = getColLetter(c);
      sheet.getRange(avgRow, c).setFormula('=AVERAGE(' + pctLet + startRow + ':' + pctLet + (avgRow - 1) + ')')
        .setNumberFormat('0.0%').setHorizontalAlignment('center').setFontWeight('bold');
      c++;
    });

    const ovLet = getColLetter(overallCol);
    sheet.getRange(avgRow, overallCol).setFormula('=AVERAGE(' + ovLet + startRow + ':' + ovLet + (avgRow - 1) + ')')
      .setNumberFormat('0.0%').setHorizontalAlignment('center').setFontWeight('bold').setFontColor('#1e40af');
  }

  // Create collapsible [+] / [-] column groupings
  monthGroupRanges.forEach(grp => {
    try {
      sheet.getRange(1, grp.start, sheet.getMaxRows(), grp.count).shiftColumnGroupDepth(1);
    } catch(e) {
      Logger.log('Group error: ' + e.message);
    }
  });

  sheet.setColumnGroupControlPosition(SpreadsheetApp.GroupControlPosition.AFTER);
  sheet.setFrozenColumns(2);
  sheet.setFrozenRows(5);
}

function getColLetter(col) {
  let temp, letter = '';
  while (col > 0) {
    temp = (col - 1) % 26;
    letter = String.fromCharCode(temp + 65) + letter;
    col = (col - temp - 1) / 26;
  }
  return letter;
}

function showSyncInfo() {
  SpreadsheetApp.getUi().alert(
    'Continuous Auto-Sync Active',
    'Whenever you edit grades in the Journaller Web App, this Google Sheet automatically updates in real-time!\\n\\n' +
    'Click [+] and [-] brackets above month headers to expand or collapse categories horizontally.',
    SpreadsheetApp.getUi().ButtonSet.OK
  );
}
