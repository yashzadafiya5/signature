from string import ascii_uppercase
from pip import main
import xlsxwriter
from PIL import Image
from pytesseract import pytesseract
import time
path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image_path = r"images/Untitled1.png"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

newtext=[]
text = pytesseract.image_to_string(img)
listToStrs = ''.join([str(param) for param in text])

ok=listToStrs.split(' ')
workbook = xlsxwriter.Workbook('excelfiles/new1.xlsx')
worksheet = workbook.add_worksheet()
firstalpha=[]
number=0
datalength=len(ok)
abc=ascii_uppercase
maindata=round(datalength/10)
number=1
while number<maindata:
    i=0
    while i<10:
        line=abc[i],number
        firstalphabet = ''.join([str(param) for param in line])
        firstalpha.append(firstalphabet)
        i+=1
    number+=1
newnumber=0
while newnumber<len(firstalpha):
    worksheet.write(firstalpha[newnumber],ok[newnumber])
    newnumber+=1
workbook.close()


# import pandas as pd
 
# # read by default 1st sheet of an excel file
# dataframe1 = pd.read_excel('excelfiles/new1.xlsx')
 
# print(dataframe1)



"-------------------------------------------------------------------------------------------------------------"
