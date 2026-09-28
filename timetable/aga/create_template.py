import pandas as pd

# Define the times
times_1_4 = [
    "09:00-09:40", "09:45-10:25", "10:30-11:10", "11:15-11:55",
    "12:00-12:40", "12:45-13:25", "13:30-14:10", "14:15-14:55",
    "15:00-15:40", "16:20-17:00", "17:05-17:45"
]
labels_1_4 = [
    "1-soat", "2-soat", "3-soat", "4-soat",
    "TUSHLIK", "5-soat", "6-soat", "7-soat",
    "8-soat", "9-soat", "10-soat"
]

times_5_11 = [
    "09:00-09:40", "09:45-10:25", "10:30-11:10", "11:15-11:55", "12:00-12:40",
    "12:40-13:25", "13:25-14:05", "14:10-14:50", "14:55-15:35",
    "16:20-17:00", "17:05-17:45"
]
labels_5_11 = [
    "1-soat", "2-soat", "3-soat", "4-soat", "5-soat",
    "TUSHLIK", "6-soat", "7-soat", "8-soat",
    "9-soat", "10-soat"
]

days = ["DUSHANBA", "SESHANBA", "CHORSHANBA", "PAYSHANBA", "JUMA"]

classes_1_4 = ["1-A", "1-B", "2-A", "2-B", "3-A", "4-A"]
classes_5_11 = ["5-A", "5-B", "6-A", "6-B", "7-A", "7-B", "8-A", "8-B", "9-A", "9-B", "10-A", "10-B", "11-A", "11-B"]

rows = []
for day in days:
    # 1-4 logic
    for i in range(len(labels_1_4)):
        row = {"KUN": day if i == 0 else "", "VAQT": times_1_4[i], "SOAT": labels_1_4[i]}
        for c in classes_1_4:
            row[c] = "TUSHLIK" if labels_1_4[i] == "TUSHLIK" else ""
        for c in classes_5_11:
            row[c] = "TUSHLIK" if labels_5_11[i] == "TUSHLIK" else ""
        rows.append(row)

df = pd.DataFrame(rows)

# Correct KUN display so it spans, but in pandas just leave blank
with pd.ExcelWriter('/home/dpdp/target/timetable/Yangi_Dars_Jadvali_Template.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Barcha Sinflar')
print("Created Yangi_Dars_Jadvali_Template.xlsx!")
