from pyPdf2 import PdfFileWriter, PdfFileReader
 
path = "C:/Users/Matthew/Dropbox/Research/Urban/Papers/Delayed Marriage/Presentations/Results.pdf"
to   = "C:/Users/Matthew/Dropbox/Research/Urban/Papers/Delayed Marriage/Presentations/Results_flip.pdf"
 
output = PdfFileWriter()
input1 = PdfFileReader(file(path, "rb"))
output.addPage(input1.getPage(1).rotateClockwise(90))
output.addPage(input1.getPage(2).rotateClockwise(90))
output.addPage(input1.getPage(3).rotateClockwise(90))
output.addPage(input1.getPage(4).rotateClockwise(90))
 
outputStream = file(to, "wb")
output.write(outputStream)
outputStream.close()