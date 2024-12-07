import cv2
import pytesseract
#utilizar o arquivo detector de rostos/faces
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#abrir a camera
camera= cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

while True:
    sucesso, frame= camera.read()
    cv2.imshow('webcam', frame)
    #converter o frame pra preto e branco
    cv2.imwrite('ImagemSalva.png', frame)
    img_salva = cv2.imread('ImagemSalva.png')
    img_pt_br = cv2.cvtColor(img_salva, cv2.COLOR_BGR2GRAY)
    texto_capturado = pytesseract.image_to_string(img_pt_br, config='-l eng --oem 3 --psm 12')
    print(texto_capturado)
 

    #exibindo o frame desenhado  
    cv2.imshow('Detectados...', frame)
    
    
    
    
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
#fecha streaming
camera.release()
cv2.destroyAllWindows()
