#doesnt work

from PyPDF2 import PdfWriter


merger = PdfWriter()

pdfs=[]
n=int(input("How many pdfs are there?"))

for i in range(n):
    name=input(f"Enter the name of the pdf{i+1}: ")
    
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merger.pdf")
merger.close()