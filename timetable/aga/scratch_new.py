import pandas as pd
f = '/home/dpdp/target/timetable/soatlar yangi.xlsx'
print(f"=== Excel File: soatlar yangi.xlsx ===")
try:
    xl = pd.ExcelFile(f)
    print("Sheets:", xl.sheet_names)
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        print(f" Sheet '{sheet}' shape: {df.shape}")
        print(df.head(15).to_string())
except Exception as e:
    print("Error reading excel:", e)
