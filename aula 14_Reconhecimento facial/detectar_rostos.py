import cv2
#capturando uma imagem
image= cv2.imread('foto1.jpg')
cv2.imshow("foto1", image)

#carregar cacteristicas do arquivo
cascadeFace= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Converter a imagem pra tons de cinzas
imagem_cinza=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#verificar se a imagem está preto e branco
cv2.imshow("Imagem preto e branco", imagem_cinza)

#detectando rostos e desenhando um quadrado
faces= cascadeFace.detectMultiScale(imagem_cinza, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (000, 255, 000), 2)
    
cv2.imshow("resultado", image)
cv2.waitKey(0)
cv2.destroyAllWindows()