import pandas as pd
xl = pd.ExcelFile('/home/dpdp/target/timetable/5-11 soatlar.xlsx')
for sheet in xl.sheet_names:
    df = xl.parse(sheet)
    print(f"--- Sheet: {sheet} ---")
    for idx, row in df.iterrows():
        row_list = [str(x) for x in row.values]
        if any("Math" in x or "Matematika" in x for x in row_list):
            print(row_list)
