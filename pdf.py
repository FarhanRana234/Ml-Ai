import PyPDF2 
data = open("nlp.pdf", "r")

reader= PyPDF2.PdfReader(data)

print(reader.numPages)