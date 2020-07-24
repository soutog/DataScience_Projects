import PyPDF2

template = PyPDF2.PdfFileReader(open('pdfs_Combined.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in list(range(template.getNumPages())):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

outPutStream = open('watermarked.pdf', 'wb')
output.write(outPutStream)
outPutStream.close()
