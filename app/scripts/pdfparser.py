from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from firebase_admin import credentials
from io import StringIO
import os



def PdfParser(fileName):
    # TODO: Make filepaths less hardcoded
    try:
        os.system("qpdf --decrypt --password='' ./app/scripts/{} ./app/scripts/transcript_decrypted.pdf".format(fileName))
    except:
        raise Exception('Failed to decrypt')
    # TODO: Replace code below with simpler PyPDF3 code
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open('./app/scripts/transcript_decrypted.pdf', 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()


    # Code above copy pasted
    flag=False
    course=[]
    coursenum=[]
    for line in text.splitlines():
        
        if(line.strip() == "Course"):
            flag=True
        elif(line.strip()=="Description" or line.strip() == "Term GPA"):
            flag=False
        elif flag:
            if line == "":
                continue
            try:
                int(line)
                coursenum.append(line)
            except ValueError:
                try:
                    int(line[:-1])
                    coursenum.append(line)
                except ValueError:
                    course.append(line)
     
    os.remove("./app/scripts/{}".format(fileName))        
    os.remove("./app/scripts/transcript_decrypted.pdf")        

    course = list(filter(None, course))
    coursenum = list(filter(None, coursenum))
    # should have a 1-1 pairing
    return [course, coursenum] 

