from PyPDF2 import PdfWriter
merger = PdfWriter()
pdfs=[]
x=input("Hi, Welcome to pdf merger\nDo you want to continue?(y/n) ")
if x=="y":
    a=int(input("How many PDF's do you want to merge? "))
    for i in range(0,a):
        name=input(f"Enter the name of the {i+1} PDF file ")
        pdfs.append(name)
    for pdf in pdfs:    
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()
else:
    exit()   
    