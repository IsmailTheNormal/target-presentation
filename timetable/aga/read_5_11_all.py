import pandas as pd
xl = pd.ExcelFile('/home/dpdp/target/timetable/5-11 soatlar.xlsx')
df = xl.parse(xl.sheet_names[0])
print(df.head(15).to_string())
