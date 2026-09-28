import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment

classes_1_4 = ["1-A", "1-B", "2-A", "2-B", "3-A", "4-A"]
classes_5_11 = ["5-A", "5-B", "6-A", "6-B", "7-A", "7-B", "8-A", "8-B", "9-A", "9-B", "10-A", "10-B", "11-A", "11-B"]
all_classes = classes_1_4 + classes_5_11

days = ["DUSHANBA", "SESHANBA", "CHORSHANBA", "PAYSHANBA", "JUMA"]

# Periods structure. We will unify rows by their logical sequence (13 rows per day)
# 0: Nonushta, 1: 1-soat, 2: 2-soat, 3: 3-soat, 4: 4-soat
# 5: 1-4 Lunch / 5-11 5-soat
# 6: 1-4 5-soat / 5-11 Lunch
# 7: 6-soat, 8: 7-soat, 9: 8-soat
# 10: Polnik, 11: 9-soat, 12: 10-soat

rows = []
for day in days:
    for idx in range(13):
        row = {"KUN": day if idx == 0 else ""}
        
        # Determine 1-4 label and time
        if idx == 0: l1, t1 = "NONUSHTA", "08:30-09:00"
        elif idx == 1: l1, t1 = "1-soat", "09:00-09:40"
        elif idx == 2: l1, t1 = "2-soat", "09:45-10:25"
        elif idx == 3: l1, t1 = "3-soat", "10:30-11:10"
        elif idx == 4: l1, t1 = "4-soat", "11:15-11:55"
        elif idx == 5: l1, t1 = "TUSHLIK", "12:00-12:40"
        elif idx == 6: l1, t1 = "5-soat", "12:45-13:25"
        elif idx == 7: l1, t1 = "6-soat", "13:30-14:10"
        elif idx == 8: l1, t1 = "7-soat", "14:15-14:55"
        elif idx == 9: l1, t1 = "8-soat", "15:00-15:40"
        elif idx == 10: l1, t1 = "POLNIK", "15:40-16:20"
        elif idx == 11: l1, t1 = "9-soat", "16:20-17:00"
        elif idx == 12: l1, t1 = "10-soat", "17:05-17:45"
        
        # Determine 5-11 label and time
        if idx == 0: l5, t5 = "NONUSHTA", "08:30-09:00"
        elif idx == 1: l5, t5 = "1-soat", "09:00-09:40"
        elif idx == 2: l5, t5 = "2-soat", "09:45-10:25"
        elif idx == 3: l5, t5 = "3-soat", "10:30-11:10"
        elif idx == 4: l5, t5 = "4-soat", "11:15-11:55"
        elif idx == 5: l5, t5 = "5-soat", "12:00-12:40"
        elif idx == 6: l5, t5 = "TUSHLIK", "12:40-13:25"
        elif idx == 7: l5, t5 = "6-soat", "13:25-14:05"
        elif idx == 8: l5, t5 = "7-soat", "14:10-14:50"
        elif idx == 9: l5, t5 = "8-soat", "14:55-15:35"
        elif idx == 10: l5, t5 = "POLNIK", "15:40-16:20"
        elif idx == 11: l5, t5 = "9-soat", "16:20-17:00"
        elif idx == 12: l5, t5 = "10-soat", "17:05-17:45"
        
        row["SOAT (1-4)"] = l1
        row["VAQT (1-4)"] = t1
        row["SOAT (5-11)"] = l5
        row["VAQT (5-11)"] = t5
        
        # Fill cells
        for c in all_classes:
            val = ""
            is_1_4 = c in classes_1_4
            label = l1 if is_1_4 else l5
            
            if label in ["NONUSHTA", "TUSHLIK", "POLNIK"]:
                val = label
            elif label in ["9-soat", "10-soat"]:
                val = "To'garak (English/Math Uzum Market)"
            else:
                # Apply rules
                if day in ["SESHANBA", "PAYSHANBA"]:
                    if c in ["1-A", "1-B"] and idx == 1: val = "Jismoniy tarbiya (combined)"
                    if c in ["2-A", "2-B"] and idx == 2: val = "Jismoniy tarbiya (combined)"
                    if c in ["3-A", "4-A"] and idx == 3: val = "Jismoniy tarbiya (combined)"
                    if c in ["5-A", "5-B"] and idx == 1: val = "Jismoniy tarbiya (combined)"
                    if c in ["6-A", "6-B"] and idx == 2: val = "Jismoniy tarbiya (combined)"
                    if c in ["7-A", "7-B"] and idx == 3: val = "Jismoniy tarbiya (combined)"
                    if c in ["8-A", "8-B"] and idx == 4: val = "Jismoniy tarbiya (combined)"
                    if c in ["11-A", "11-B"] and idx == 7: val = "Jismoniy tarbiya (combined)"
                    
                    if is_1_4 and idx == 6 and not val: val = "Mental arifmetika"
                    if not is_1_4 and c.startswith(("5", "6", "7", "8")) and idx == 8 and not val: val = "Shaxmat"
                
                if day == "DUSHANBA":
                    if c.startswith(("5", "6")) and idx == 7 and not val: val = "Science"
                    if is_1_4 and idx == 6 and not val: val = "Mental arifmetika"
            
            row[c] = val
        rows.append(row)

df = pd.DataFrame(rows)

# Create Excel writer
out_path = '/home/dpdp/target/timetable/MASTER_JADVAL_NEW.xlsx'
with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Umumiy Jadval', index=False)
    
    # Class POV sheet
    for c in all_classes:
        df_class = df[["KUN", "SOAT (1-4)" if c in classes_1_4 else "SOAT (5-11)", 
                       "VAQT (1-4)" if c in classes_1_4 else "VAQT (5-11)", c]].copy()
        df_class.columns = ["KUN", "SOAT", "VAQT", "FAN"]
        df_class.to_excel(writer, sheet_name=c, index=False)

print("Timetable generated successfully at", out_path)
