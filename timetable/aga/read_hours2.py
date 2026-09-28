from docx import Document

doc = Document('/home/dpdp/target/timetable/1-11 umumiy soatlar.docx')
for row in doc.tables[0].rows:
    cells = [c.text.strip().replace('\n', ' ') for c in row.cells]
    print(" | ".join(cells))
