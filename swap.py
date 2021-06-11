import cv2 
import numpy as np

#original image 1
Sid = cv2.imread('s.jpg')

cv2.imshow("Sid", Sid)
cv2.waitKey()
cv2.destroyAllWindows()

#original image 2
Akki = cv2.imread('a.jpg')

cv2.imshow("Akki", Akki)
cv2.waitKey()
cv2.destroyAllWindows()

#resize images
sid = cv2.resize(cv2.imread('s.jpg') , (400,400))
akki = cv2.resize(cv2.imread('a.jpg') , (400,400))

#swap face 
sid[10:200 , 50:280] = akki[10:200 , 50:280]
cv2.imshow("akkiface", sid)
cv2.waitKey()
cv2.destroyAllWindows()
