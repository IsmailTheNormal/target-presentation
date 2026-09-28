# 🎓 Production Google Sheets Setup Guide

This guide allows you to run your gradebook **directly inside Google Sheets** with:
- Native **`[+]` / `[-]` expandable/collapsible monthly columns**
- Categories with caps: **Attendance (/10), Participation (/20), Homework (/30), Quiz/Exam (/40)**
- **Bulk roster paste** (insert 30+ real students in 5 seconds)
- **Interactive Student Performance Line Chart** (gain/drop tracking vs class average)
- **XML file export & import**

---

## ⚡ Option 1: Instant Upload to Google Drive (Fastest, 10 seconds)

We have already generated a production workbook file:
📄 [`Teacher_Production_Gradebook.xlsx`](file:///home/dpdp/target/journaller/Teacher_Production_Gradebook.xlsx)

1. Open [Google Drive](https://drive.google.com).
2. Click **New > File upload**, and select `Teacher_Production_Gradebook.xlsx`.
3. Double-click the file in Google Drive to open it as a **Google Sheet**.
4. That's it!
   - Notice the **`[-]` and `[+]` brackets** above columns `C` through `F` for each month. Click them to expand or collapse category marks!
   - All formulas for **Month Total**, **Month %**, **Class Averages**, and **Standing** are pre-configured.

---

## 🚀 Option 2: Install the Automation Script in Any Google Sheet

If you already have an existing Google Sheet or want full automation (bulk roster paste, student chart tab generation, and XML export):

1. In your Google Sheet, click **Extensions > Apps Script** in the top menu.
2. Delete any placeholder code in the script editor.
3. Open [`google-sheets/Code.gs`](file:///home/dpdp/target/journaller/google-sheets/Code.gs), copy all contents, and paste it into the editor.
4. Click the **Save** icon (disk icon or `Ctrl+S`).
5. Close the Apps Script tab and **refresh your Google Sheet**.
6. A new custom menu will appear in the top toolbar:
   👉 **`🎓 Teacher Gradebook`**

### Available Actions in the Menu:
1. **`📊 1. Setup / Reset Gradebook Sheet`**:
   Formats the entire sheet with expandable monthly column groups, styled headers, and automated formulas.
2. **`➕ 2. Bulk Paste Student Names`**:
   Opens a modal where you paste your real class roster (one name per line). Instantly creates all rows with `=SUM()` and percentage formulas.
3. **`📈 3. Create Student Performance Chart Tab`**:
   Creates an interactive **Student Analytics** tab with a student selector and a line chart comparing the selected student's monthly performance against the class average.
4. **`💾 Export Gradebook as XML`**:
   Generates a standardized `.xml` file containing your real student records, categories, caps, and grades.
