import openpyxl

file_path = '/home/dpdp/target/timetable/MASTER_JADVAL_NEW.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb['Umumiy Jadval']

cohorts = [
    ["1-A", "1-B"], ["2-A", "2-B"], ["3-A", "4-A"],
    ["5-A", "5-B"],
    ["6-A", "6-B", "7-A", "7-B"],
    ["8-A", "8-B", "9-A", "9-B"],
    ["10-A", "10-B", "11-A", "11-B"]
]
all_classes = [c for cohort in cohorts for c in cohort]
def get_col(c): return openpyxl.utils.get_column_letter(all_classes.index(c) + 6)

fixed_breaks = ["NONUSHTA", "TUSHLIK", "POLNIK", "To'garak"]
shared_keywords = ["(Levels)", "(Ordinary/Advanced)", "(combined)", "Shaxmat"]

# Process day by day
for day_idx in range(5):
    start_row = 2 + (day_idx * 13)
    # The class slots are indices 1, 2, 3, 4, 6, 7, 8, 9 (skipping 0:Nonushta, 5:Lunch/5-soat, 10:Polnik, 11:9-soat, 12:10-soat)
    # Wait, the exact row indices for academic hours for 1-4 and 5-11 are slightly different due to staggered lunch.
    # Let's just iterate through the available 13 rows, skipping the fixed break rows.
    
    for cohort in cohorts:
        # Extract all subjects for this cohort on this day
        shared_subjects = [] # list of (val, duration)
        indep_subjects = {c: [] for c in cohort}
        
        # To avoid double counting shared, we just track what we found
        found_shared = set()
        
        for r in range(start_row, start_row + 13):
            # Check if this row is a fixed break for this cohort
            val_a = ws[f"{get_col(cohort[0])}{r}"].value
            if val_a and any(b in val_a for b in fixed_breaks):
                continue
                
            # It's an academic row
            # Is it shared?
            if val_a and any(sk in val_a for sk in shared_keywords):
                if val_a not in found_shared:
                    shared_subjects.append(val_a)
                    found_shared.add(val_a)
            else:
                for c in cohort:
                    val_c = ws[f"{get_col(c)}{r}"].value
                    if val_c and not any(sk in val_c for sk in shared_keywords) and not any(b in val_c for b in fixed_breaks):
                        indep_subjects[c].append(val_c)
                        
        # Now clear the academic rows for this cohort
        academic_rows = []
        for r in range(start_row, start_row + 13):
            val_a = ws[f"{get_col(cohort[0])}{r}"].value
            if not (val_a and any(b in val_a for b in fixed_breaks)):
                academic_rows.append(r)
                for c in cohort:
                    ws[f"{get_col(c)}{r}"] = None
                    
        # Re-place them compactly
        # 1. Place shared subjects (they take 2 hours usually, except Shaxmat is 1, let's just place as they were)
        # Wait, if we just place them one by one, we might separate 2-hour blocks!
        # Let's group independent subjects into duplicates to keep blocks if they existed.
        
        row_ptr = 0
        
        # Place shared
        for sub in shared_subjects:
            # How many times did it appear? If it was a block, it should appear twice.
            # Actually, we stored unique values. Let's assume shared are 2 hours except Shaxmat.
            is_block = "Math" in sub or "ELT" in sub
            times = 2 if is_block else 1
            for _ in range(times):
                if row_ptr < len(academic_rows):
                    for c in cohort:
                        ws[f"{get_col(c)}{academic_rows[row_ptr]}"] = sub
                    row_ptr += 1
                    
        # Place independent
        # Keep track of row_ptr per class since they might have different numbers of subjects
        class_ptrs = {c: row_ptr for c in cohort}
        for c in cohort:
            for sub in indep_subjects[c]:
                if class_ptrs[c] < len(academic_rows):
                    ws[f"{get_col(c)}{academic_rows[class_ptrs[c]]}"] = sub
                    class_ptrs[c] += 1

# Sync to POV
for c in all_classes:
    col = get_col(c)
    ws_class = wb[c]
    for row in range(2, 67):
        val = ws[f"{col}{row}"].value
        ws_class[f"D{row}"] = val if val else ""

wb.save(file_path)
print("Compacted! No windows left.")
