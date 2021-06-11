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

#make a collage by horizontal concat
collage = cv2.hconcat([Sid , Akki])

cv2.imshow("SidFace" , collage)
cv2.waitKey()
cv2.destroyAllWindows()
