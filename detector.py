import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

billete2000= cv2.CascadeClassifier('2000.xml')
billete10000= cv2.CascadeClassifier('10000.xml')

while True:
   
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bi2000 = billete2000.detectMultiScale(gray,
    scaleFactor = 5,
    minNeighbors = 91,
    minSize=(70,78))
    bi10000 = billete10000.detectMultiScale(gray,
    scaleFactor = 5,
    minNeighbors = 91,
    minSize=(70,78))
    for (x,y,w,h) in bi2000:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'2000 PESOS',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    for (x,y,w,h) in bi10000:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'10000 PESOS',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)  
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
