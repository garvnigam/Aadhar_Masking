from tkinter import Y
from pdf2image import convert_from_path
import cv2
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\700100480\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import numpy as np
pdf_files= r'qwe.pdf'

pages = convert_from_path(pdf_files ,poppler_path=(r"C:\Program Files (x86)\poppler-0.68.0\bin"))
count = 0
lis=[]


for page in pages:
     count +=1
     
     
     x='file-'+str(count)+'.jpg'
     
     page.save(x, 'JPEG')
     y=cv2.imread(x)
    #  print(y)
     lis.append(y)
     
     
final_image=cv2.vconcat(lis)
cv2.imwrite("App Form1.jpg", final_image)
img = cv2.imread('App Form1.jpg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold

# print(boxes)
script = pytesseract.image_to_string(img)
f = open("gaurav.txt", "w")
f.write(script)
f.close()
count=0
file1 = open('gaurav.txt', 'r')
Lines = file1.readlines()
EMAIL_REG = r"^[0-9]{4}\s[0-9]{4}\s[0-9]{4}$"
for line in Lines:
		
	# print(line)		# matching the regex to each line
	if re.search(EMAIL_REG, line, re.IGNORECASE):
        
		search = re.search(EMAIL_REG, line, re.IGNORECASE)
		matchList = str(search.group())
		# print(matchList[:4])

# print(line)
hImg,wImg=gray.shape
cong=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.image_to_data(gray,config=cong)
#print(type(boxes))
       
for x,b  in enumerate(boxes.splitlines()):
    if x!=0:
        b=b.split()
    
    
    if len(b)==12:
        #print(b)
        if str(matchList[:4]) in (b[11]): 
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            #cv2.rectangle(gray,(x,y),(w+x,h+y),(0,0,255),3)
            # print(x,y,w,h)
        # cv2.putText(gray,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
start_point = (x+500,y)
   
# Ending coordinate, here (125, 80)
# represents the bottom right corner of rectangle
end_point = (w+x-100,h+y)
   
# Black color in BGR
color = (0, 0, 0)
   
# Line thickness of -1 px
# Thickness of -1 will fill the entire shape
thickness = -1
   
# Using cv2.rectangle() method
# Draw a rectangle of black color of thickness -1 px
image = cv2.rectangle(gray, start_point, end_point, color, thickness)
   
# Displaying the image 
grays = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
cv2.imwrite("App Form.jpg", grays)
print("product Developed")
# cv2.imshow('result',gray)
#cv2.waitKey(0)


     
