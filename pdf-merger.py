import PyPDF2
import sys

input_file = sys.argv[1:]


def merge_pdfs(pdf_merge):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_merge:
        merger.append(pdf)
    merger.write('merged.pdf')


merge_pdfs(input_file)
