#Reconhecimento de caracteres Pytesseract (só testo)
#Path:'C:\Users\Aluno'
#Tesseract path:"C:\Users\Aluno\tesseract.exe"
#Install libraries
#pip install opencv-python --> allows to work with imagens
#pip install pytesseract --> allows the caracters recognition in imagens
import cv2
import pytesseract
import time

residents_array=["Marcos - OTM 2022", "Alex - Palio - FBI 5551", "Gabriele - Civic - AAA - 5551"]
#call the library 
pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\tesseract.exe"

#inserting a image in a variable 
image=cv2.imread('pinguin.jpg', 0)
image2=cv2.imread('pinguin2.jpg', 0)
imageplate=cv2.imread('plate.png', 0)
imageplate2=cv2.imread('FBIplate.jpg', 0)
imageplate3=cv2.imread('AAAplate.jpg', 0)
imageplate4=cv2.imread('ABCDplate.jpg', 0)

#show the image
#cv2.imshow("img", image)
#time.sleep(3)
#cv2.imshow("img2", image2)
#time.sleep(3)
cv2.imshow("placa", imageplate)
cv2.imshow("placa2", imageplate2)
cv2.imshow("placa3", imageplate3)
cv2.imshow("placa4", imageplate4)
cv2.waitKey(1) # zero is used to allow that any key can close a image




#extract the text of image
#text_captured=pytesseract.image_to_string(image, config='-l eng --oem 3 --psm 12')
#print(text_captured)
#text_captured2=pytesseract.image_to_string(image3, config='-l eng --oem 3 --psm 12')
#print(text_captured2)
# text_captured=pytesseract.image_to_string(imageplate, config='-l eng --oem 3 --psm 12')
# print(text_captured)
# text_captured2=pytesseract.image_to_string(imageplate2, config='-l eng --oem 3 --psm 12')
# print(text_captured2)
text_captured3=pytesseract.image_to_string(imageplate3, config='-l eng --oem 3 --psm 12')
print(text_captured3)
# text_captured4=pytesseract.image_to_string(imageplate4, config='-l eng --oem 3 --psm 12')
# print(text_captured4)

# for i in range(residents_array[i]):
text_stripped=text_captured3.strip()
for i in residents_array:
    if text_stripped in i:
        print('PLACA VERIFICADA')


#insert a stopped point
cv2.waitKey(0) # zero is used to allow that any key can close a image

#destroy windows
cv2.destroyAllWindows()

