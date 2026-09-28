import pandas as pd

# 1. Extract Classes from Master Timetable
print("=== CLASSES ===")
try:
    df = pd.read_excel('/home/dpdp/target/timetable/Umjumiy dars jadvali (namuna).xlsx', sheet_name=0)
    # the classes are in row 0 or 1. Let's look at the first few rows
    classes = set()
    for col in df.columns:
        for val in df[col].head(10).values:
            if isinstance(val, str) and len(val) <= 4 and '-' in val and val[0].isdigit():
                classes.add(val)
    # Sort classes logically
    def class_sort_key(c):
        num, letter = c.split('-')
        return (int(num), letter)
    sorted_classes = sorted(list(classes), key=class_sort_key)
    print("Found Classes:", ", ".join(sorted_classes))
except Exception as e:
    print("Error getting classes:", e)

# 2. Extract Teachers from Dars taqsimoti.xlsx
print("\n=== TEACHERS & SUBJECTS ===")
try:
    df_teachers = pd.read_excel('/home/dpdp/target/timetable/Dars taqsimoti.xlsx')
    print("Columns in Dars taqsimoti.xlsx:", list(df_teachers.columns))
    print(df_teachers.head(15).to_string())
except Exception as e:
    print("Error getting teachers:", e)

