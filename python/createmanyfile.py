from os import closerange
from PIL import Image
import pytesseract as tess
from string import ascii_lowercase, ascii_uppercase
import string


tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# image = r'python\result.png'
# text = tess.image_to_string(Image.open(image), lang="eng")

text=['a','A','b','D','c','d','e','f',"@",'1']


    
newtext = []
for ele in text:
    if ele.strip():
        newtext.append(ele)
    
count=0
for i in newtext:
    if i in ascii_uppercase:
        file = open(i ,"w") 
        file.write(i)
        
    elif i in ascii_lowercase:
        file = open(i + "1.txt","w") 
        file.write(i)
        
    elif i in string.digits:
        file = open(i ,"w") 
        file.write(i)
        
    elif i in string.punctuation:
        file = open(i,"w") 
        file.write(i)
    elif '|' in i:
        file = open('|',"w") 
        file.write(i)
    else:
        file = open(i,"w") 
        file.write(i)
    count+=1
print(count)