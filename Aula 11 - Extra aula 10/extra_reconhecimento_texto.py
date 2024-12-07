#C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR

#1 - Instalação do tesseract
#2 - Instalação da Biblioteca pytesseract
    #pip install pytesseract
    
#3 - Instalação da Biblioteca opencv
    #pip install opencv-python

#Biblioteca para trabalho com imagens
import cv2 
#Biclioteca para reconhecer caracteres
import pytesseract

lista_moradores=["Marcos - Gol - OTM 2022", "Alex - Palio - FB1 55517", "Gabriele - Civic - AAA 5551"]

# #Indicar o pacote de reconhecimento de caracteres
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#Inserindo a imagem em uma variável
meu_livro = cv2.imread("gato_pepeu.jpg",0)
meu_livro2 = cv2.imread("livro.jpg",0)
placa = cv2.imread("placa.png",0)
placa_2 = cv2.imread("placa_2.jpg",0)
placa_3 = cv2.imread("placa_3.jpg",0)

# Exibir a imagem
cv2.imshow("img",meu_livro)
cv2.imshow("img2",meu_livro2)
cv2.imshow("img3",placa)
cv2.imshow("img4",placa_2)
cv2.imshow("img5",placa_3)

# Extrair o texto da imagem
texto_capturado1 = pytesseract.image_to_string(placa, config='-l eng --oem 3 --psm 12')
texto_capturado2 = pytesseract.image_to_string(placa_2, config='-l eng --oem 3 --psm 12')
placa_lida = pytesseract.image_to_string(placa, config='-l eng --oem 3 --psm 12')

print(texto_capturado1)
print(texto_capturado2)
print(placa_lida)

#Removendo espaços do texto capturado
captura_sem_espaco = placa_lida.strip()
print(captura_sem_espaco)

#Printar informações do proprietário do veículo
for cadastro in lista_moradores:
    if captura_sem_espaco in cadastro:
        print(cadastro)

#Inserir um ponto de parada
cv2.waitKey(0)
cv2.destroyAllWindows()





    
    