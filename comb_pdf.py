##Python code to combine pdfs for Gentrification analysis
#Can be used generally for append_pdf functionality

from pyPdf import PdfFileWriter, PdfFileReader

N = 50
path = "C:\\Users\\Matthew\\Dropbox\Research\\Urban\\Resurgence\\Output\\"

incp    = path + "dci_incp_top"+str(N)+".pdf"
trctpop = path + "dci_trctpop_top"+str(N)+".pdf"
shrwht  = path + "dci_shrwht_top"+str(N)+".pdf"
shrblk  = path + "dci_shrblk_top"+str(N)+".pdf"
mcwkid   = path + "dci_mcwkid_top"+str(N)+".pdf"
mcnkid   = path + "dci_mcnkid_top"+str(N)+".pdf"
yprof   = path + "dci_yprof_top"+str(N)+".pdf"
outall  = path + "Top"+str(N)+"_byIncPerc.pdf"
outj    = path + "ByCity_Top"+str(N)+"_byIncPerc.pdf"

def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

output = PdfFileWriter()

append_pdf(PdfFileReader(file(incp,"rb")),output)
append_pdf(PdfFileReader(file(trctpop,"rb")),output)
append_pdf(PdfFileReader(file(shrwht,"rb")),output)
append_pdf(PdfFileReader(file(shrblk,"rb")),output)
append_pdf(PdfFileReader(file(mcwkid,"rb")),output)
append_pdf(PdfFileReader(file(mcnkid,"rb")),output)
append_pdf(PdfFileReader(file(yprof,"rb")),output)

output.write(file(outall,"wb"))

output = PdfFileWriter()

for j in range(0,N):

	city = path + "diff_incp" + str(j) + ".pdf"
	append_pdf(PdfFileReader(file(city,"rb")),output)

	
output.write(file(outj,"wb"))




    
	
	
	