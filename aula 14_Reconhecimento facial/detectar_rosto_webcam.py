import cv2
#utilizar o arquivo detector de rostos/faces
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#abrir a camera
camera= cv2.VideoCapture(0)
while True:
    sucesso, frame= camera.read()
    cv2.imshow('webcam', frame)
    #converter o frame pra preto e branco
    framePretoBranco=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', framePretoBranco)
    
    #detectar os rostos/faces no frame
    rostos= detector.detectMultiScale(framePretoBranco, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))
    
    #desenhar o retangulo no frame
    
    for (x, y, lar, alt) in rostos:
        cv2.rectangle(frame, (x,y), (x+lar, y+alt), (000, 255, 255), 2)
    #exibindo o frame desenhado  
    cv2.imshow('Rostos detectados...', frame)
    
    
    
    
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
#fecha streaming
camera.release()
cv2.destroyAllWindows()
