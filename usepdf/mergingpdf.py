from pypdf import PdfWriter
nofi = int(input("Enter the number of files:    "))

fils = []
for i in range(nofi):
    file_name = input("Enter the file name with location:")
    fils.append(file_name)
newmerge = input("what to name it:    ")
merger = PdfWriter()

for pdf in fils:
    merger.append(pdf)

merger.write(f"{newmerge}.pdf")
merger.close()