from docx import Document

try:
    doc = Document('/home/dpdp/target/timetable/1-11 umumiy soatlar.docx')
    for row in doc.tables[0].rows:
        cells = [c.text.strip().replace('\n', ' ') for c in row.cells]
        if "Total" in cells[-1] or cells[0].isdigit():
            print(" | ".join(cells))
except Exception as e:
    print(e)
