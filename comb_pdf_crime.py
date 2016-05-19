##Python code to combine pdfs for Gentrification analysis
#Can be used generally for append_pdf functionality

from pyPdf import PdfFileWriter, PdfFileReader

N = 10

path = "C:\\Users\\Matthew\\Dropbox\\Research\\Urban\\Papers\\Gentrification and Crime\\Output\\"
outj = path + "ByCity_"+str(N)+"_CrimeRates.pdf"


def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

output = PdfFileWriter()

for j in range(0,N):

	city = path + "pmrate_" + str(j) + ".pdf"
	append_pdf(PdfFileReader(file(city,"rb")),output)

	
output.write(file(outj,"wb"))




    
	
	
	