import PyPDF2 as py2

pdf = open("pdfteste.pdf", "rb")

pdf_reader = py2.pdfFileReader(pdf)

n = pd_reader.numPages

for i in range(0, n):
    print("Página {}".format(i + 1))
    page = pdf_reader.getPage(i)
    print(page.extractText())



