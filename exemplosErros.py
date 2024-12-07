
#biblioteca para trabalhos com imagens
import cv2

try:
    # resultado = 10 + 5
    
    # novoResultado = int("abc")
    
    # print(novoResultado)
    
    #utilizar web cam do computador
#instalar biblioteca opencv :
#                       pip install opencv-python



    webcam = cv2.VideoCapture("carros.mp4")

    while True:
        #fazer a leitura da variavel webcam
        sucesso, frame = webcam.read()
        cv2.imshow("Camera", frame)
        
        #
        if cv2.waitKey(1) & 0xff == ord("s"):
            break
        
    webcam.release()
    cv2.destroyAllWindows()
    
except Exception as erro:
    print(f"O erro encontrado é {erro}")
    
