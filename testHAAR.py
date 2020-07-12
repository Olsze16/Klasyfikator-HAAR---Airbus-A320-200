import cv2

cascade=cv2.CascadeClassifier('./data/cascade30.xml')

img=cv2.imread('luftdanza.jpg')


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


szczoteczki = cascade.detectMultiScale(gray,1.1,10)

for (x,y,w,h) in szczoteczki:
	cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)

resized_image = cv2.resize(gray, (500, 500))
cv2.imshow('test', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows
