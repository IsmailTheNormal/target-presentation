import pandas as pd
df_teachers = pd.read_excel('/home/dpdp/target/timetable/Dars taqsimoti.xlsx')
print("--- Teachers Data ---")
for i, row in df_teachers.iterrows():
    if pd.notna(row['Unnamed: 1']) and str(row['Unnamed: 1']) != 'Full name':
        name = row['Unnamed: 1']
        grade = row['Unnamed: 2']
        subj = row['Unnamed: 3']
        hours = row['Unnamed: 4']
        print(f"Teacher: {name} | Grade: {grade} | Subject: {subj} | Hours: {hours}")
