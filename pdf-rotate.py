import PyPDF2

with open('dummy.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotate.pdf', 'wb') as output_file:
        writer.write(output_file)
