# 🎓 Teacher Gradebook & Performance Journaller

A lightweight, zero-backend gradebook web application designed specifically for teachers. It supports **horizontally expandable/collapsible monthly columns**, **category caps** (e.g. Attendance, Participation, Homework), **individual student performance gain/drop graphs**, and seamless **Google Sheets integration & XML file storage**.

---

## ✨ Key Features

1. **Student Rows & Horizontal Monthly Columns**:
   - Rows list all students (Roll No, Name, Overall YTD Average, and Trend Indicator).
   - Columns expand and collapse horizontally by month (September, October, November, etc.).
   - **Expanded Month**: Displays individual category columns (e.g., Attendance [Cap: 10], Participation [Cap: 20], Homework [Cap: 30], Quiz [Cap: 40]), plus Month Total and Month %.
   - **Collapsed Month**: Shows a compact monthly total, percentage, and month-over-month gain/drop indicator (`▲ +5.2%` or `▼ -3.1%`).
   - Global **"Expand All" / "Collapse All"** switch.

2. **Student Performance Gain / Drop Graphs**:
   - Click on any student row or the graph icon to open their detailed performance report:
     - **Performance Trajectory Chart**: Interactive line graph comparing the student's monthly progression against the class average.
     - **Gain / Drop Delta Bar Chart**: Green bars for performance gains, red bars for drops from the previous month.
     - **Category Mastery Chart**: Visualizes strengths and growth areas (e.g. 100% in Attendance, 65% in Homework).
     - **Printable Student Report**: One-click printable summary for parent-teacher meetings or records.

3. **Google Sheets Integration**:
   - **1-Click Copy & Paste**: Formatted grid ready to paste directly into cell `A1` in Google Sheets.
   - **Expandable Month Apps Script**: Includes a ready-to-use Google Apps Script that generates native `[+]` and `[-]` bracket column groupings right inside Google Sheets.
   - **CSV Export**: Standard `.csv` download that opens cleanly in Google Sheets or Excel.

4. **XML File Storage**:
   - **Export XML**: Save your entire gradebook (classes, students, categories, caps, and grades) as an `.xml` file on your computer.
   - **Import XML**: Open or restore any previously saved `.xml` gradebook file anytime.
   - **Automatic Local Storage**: Automatically saves all edits in your browser so you never lose work.

5. **Configurable Categories & Caps**:
   - Add, edit, or remove categories (e.g. Attendance, Homework, Quizzes, Lab Reports, Projects).
   - Set custom maximum caps per category with live total monthly cap calculation.
   - Visual warning if a mark exceeds the allowed cap.

---

## 🚀 Quick Start

To run the application locally:

```bash
# Install dependencies (already installed)
npm install

# Start the local development server
npm run dev
```

Then open your browser to `http://localhost:5173`.

To create an optimized production build:
```bash
npm run build
```

---

## 📁 File Structure

- [`src/App.tsx`](file:///home/dpdp/target/journaller/src/App.tsx) - Main application layout and state management.
- [`src/components/GradebookTable.tsx`](file:///home/dpdp/target/journaller/src/components/GradebookTable.tsx) - Gradebook grid with expandable monthly columns and cap validation.
- [`src/components/StudentAnalyticsModal.tsx`](file:///home/dpdp/target/journaller/src/components/StudentAnalyticsModal.tsx) - Individual student performance trajectory, gain/drop charts, and category breakdown.
- [`src/components/GoogleSheetsModal.tsx`](file:///home/dpdp/target/journaller/src/components/GoogleSheetsModal.tsx) - Google Sheets 1-click clipboard copy and Apps Script generator.
- [`src/components/CategorySettingsModal.tsx`](file:///home/dpdp/target/journaller/src/components/CategorySettingsModal.tsx) - Configure categories (Attendance, Homework, Participation) and caps.
- [`src/utils/xmlParser.ts`](file:///home/dpdp/target/journaller/src/utils/xmlParser.ts) - XML export and import serialization.
- [`src/utils/googleSheetsIntegration.ts`](file:///home/dpdp/target/journaller/src/utils/googleSheetsIntegration.ts) - Google Sheets formatters and column grouping scripts.
- [`src/utils/calculations.ts`](file:///home/dpdp/target/journaller/src/utils/calculations.ts) - Monthly averages, student trends, and gain/drop calculations.
- [`sample_gradebook.xml`](file:///home/dpdp/target/journaller/sample_gradebook.xml) - Example XML gradebook file.
