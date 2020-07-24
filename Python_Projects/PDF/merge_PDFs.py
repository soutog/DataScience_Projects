import PyPDF2
import sys

inputs = sys.argv[1:] #includes any number of PDFs

def pdf_Combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('pdfs_Combined.pdf')

pdf_Combiner(inputs)

