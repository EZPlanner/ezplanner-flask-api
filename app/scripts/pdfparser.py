from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from firebase_admin import credentials
from io import StringIO
import os, pyrebase

config = {
        'apiKey': os.environ['FIREBASE_API_KEY'],
        'authDomain': os.environ['FIREBASE_AUTH_DOMAIN'],
        'databaseURL': os.environ['FIREBASE_URL'],
        'storageBucket': os.environ['FIREBASE_BUCKET'],
        'serviceAccount': './admin.json'
    }

def parser(filepath):
    
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child(filepath).download("transcript.pdf")
    # TODO: surround with try catch and raise an exception
    os.system("qpdf --decrypt --password='' transcript.pdf transcript_decrypted.pdf")

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    
    fp = open('transcript_decrypted.pdf', 'rb')
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
    courses=[]
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
    
                
    os.remove("transcript.pdf")        
    os.remove("transcript_decrypted.pdf")        

    course = list(filter(None, course))
    coursenum = list(filter(None, coursenum))
    # should have a 1-1 pairing
    return [course, coursenum] 

if __name__ == "__main__":
    print(parser('test/t.pdf'))