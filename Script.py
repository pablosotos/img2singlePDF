import os
import img2pdf

directory_path = "/Users/pablosotos/img2singlePDF"

image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]

pdf_data = img2pdf.convert(image_files)

with open("my_pdf.pdf", "wb") as file:
    file.write(pdf_data)