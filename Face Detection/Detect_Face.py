import cv2

print '###################################'
print '#          FACE DETECT            #'
print '#                                 #'
print '# https://github.com/Kripto-Sec   #'
print '###################################'


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
	_, img = cap.read()


	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#detecta os rostos
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)

	#Desenha o retangulo em volta do rosto
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	cv2.imshow('img', img)
	
	#para se a tecla de saida for apertada
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
cap.release()
