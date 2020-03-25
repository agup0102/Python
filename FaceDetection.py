import cv2

face_cascade=cv2.CascadeClassifier("C:\\Users\\agup0013\\PycharmProjects\\ImageProcessing\\haarcascade_frontalface_default.xml")

img=cv2.imread("C:\\Users\\agup0013\\Desktop\\pp.jpg")

#Reading image as grey scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the coordinates of image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

print(type(faces))

print(faces)

#Adding rectangular box around face

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Gray",img)

cv2.waitKey(0)