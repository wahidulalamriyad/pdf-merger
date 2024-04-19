import PyPDF2

path_prefix = './'
super_pdf = PyPDF2.PdfReader(f'{path_prefix}merged.pdf')
stamp_pdf = PyPDF2.PdfReader(f'{path_prefix}wtr.pdf')
writer = PyPDF2.PdfWriter()

for page in super_pdf.pages:
    page.merge_page(stamp_pdf.pages[0])
    writer.add_page(page)

writer.write(f'{path_prefix}super_watermarked.pdf')
