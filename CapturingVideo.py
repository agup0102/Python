import cv2,time
#Eithe we give a path to capture video or provide number using webcam
#VideoCapture will creates its object and trigger the camera
#0 specifies built in camera

video=cv2.VideoCapture(0)
#check bool datatype which returns the value if python is able to read the obj
#rame n dimensional array
check,frame=video.read()
cv2.imshow('Capturing',frame)
time.sleep(3)
cv2.waitKey(0)
print(check)
print(frame)
# release camera in milli seconds
video.release()
cv2.destroyAllWindows()
