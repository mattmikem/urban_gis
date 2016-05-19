##Python code to combine pdfs for Gentrification analysis
#Can be used generally for append_pdf functionality

from pyPdf import PdfFileWriter, PdfFileReader

path = "C:\\Users\\Matthew\\Dropbox\\Research\\Alcohol (All)\\Alcohol\\Social Returns\\Data\\ADD HEALTH\\Admin\\"

base = path + "Restricted-Use Contract_Edited (Signed 5-22).pdf"
add  = path + "Supplement to Attachment B.pdf"
out  = path + "Full Restricted-Use Contract_SocialNetworks.pdf"


def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

output = PdfFileWriter()

append_pdf(PdfFileReader(file(base,"rb")),output)
append_pdf(PdfFileReader(file(add,"rb")),output)

output.write(file(out,"wb"))





    
	
	
	