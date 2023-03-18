import docx
def creatingadocx(x):
    doc = docx.Document()
    doc.add_heading('Резюме', 0)
    par1 = doc.add_paragraph(x)
    return doc.save('resume.docx')
x = input()
f = creatingadocx(x)