#Caminho: 'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR'
# instalar tesseract
# instalar da biblioteca pytesseract
        #pip install pytesseract
# instalar biblioteca opencv
        #pip install opencv-python

#para trabalhar/tratar com imagens
import cv2

#para reconhecer caracteres
import pytesseract

#indicar o pacote de reconhecimento de caracteres
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#exibindo e capturando imagem
meuLivro=cv2.imread("livro.png", 0)
cv2.imshow("img", meuLivro)

cv2.waitKey(0)

cv2.destroyAllWindows()