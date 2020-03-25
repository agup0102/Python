import cv2

img=cv2.imread("C:\\Users\\agup0013\\Desktop\\pp.jpg")
print("matrix of image", type(img))
print("type of image", type(img))
print("shape of image", img.shape)

resize = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Legend", resize)
#cv2.imshow("Legend", img)
cv2.waitKey(0)
cv2.waitKey(2000)
cv2.destroyAllWindows()


