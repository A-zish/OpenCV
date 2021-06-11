import cv2

#read image
Sid = cv2.imread('s.jpg')

cv2.imshow("Sid", Sid)
cv2.waitKey()
cv2.destroyAllWindows()

#crop an image
sid = Sid[10:200 , 50:280]
cv2.imshow("SidFace", sid)
cv2.waitKey()
cv2.destroyAllWindows()
