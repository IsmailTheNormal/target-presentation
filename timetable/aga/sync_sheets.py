import openpyxl

file_path = '/home/dpdp/target/timetable/MASTER_JADVAL_NEW.xlsx'
wb = openpyxl.load_workbook(file_path)
ws_master = wb['Umumiy Jadval']

classes_1_4 = ["1-A", "1-B", "2-A", "2-B", "3-A", "4-A"]
classes_5_11 = ["5-A", "5-B", "6-A", "6-B", "7-A", "7-B", "8-A", "8-B", "9-A", "9-B", "10-A", "10-B", "11-A", "11-B"]
all_classes = classes_1_4 + classes_5_11

for col_idx, c in enumerate(all_classes):
    col_letter = openpyxl.utils.get_column_letter(col_idx + 6)
    ws_class = wb[c]
    
    # Rows 2 to 66
    for row in range(2, 67):
        val = ws_master[f"{col_letter}{row}"].value
        if val:
            ws_class[f"D{row}"] = val

wb.save(file_path)
print("POV Sheets synced!")
