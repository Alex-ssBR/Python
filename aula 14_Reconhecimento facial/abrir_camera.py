# uitlizar webcam do computador
    #instalar biblioteca opencv: pip install opencv-python
import cv2
webcam = cv2.VideoCapture(0)
while True:
    #fazer a leitura da variável WEBCAM
    sucesso, frame = webcam.read()
    cv2.imshow("camera", frame)
    #saida da estrutura de repetição quando clica no 's'
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
    
webcam.release()
cv2.destroyAllWindows()