from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = "/docs/data.pdf"

input_pdf = PdfFileReader(file_path)
num_pages = input_pdf.getNumPages()
title = ""
print(num_pages)

document_info = input_pdf.getDocumentInfo()
print(document_info)

#extract pages from a pdf
with open("Data.txt", "w") as output_file:
    output_file.write(f"{title}\n")
    output_file.write(f"Number of pages: {num_pages}\n\n")

    for page in input_pdf.pages:
        text = page.extractText()
        output_file.write(text)

#Adding new page
output_pdf = PdfFileWriter()
cover_page = input_pdf.getPage(0)
output_pdf.addPage(cover_page)

with open("portion.pdf", "wb") as output_file:
    output_pdf.write(output_file)