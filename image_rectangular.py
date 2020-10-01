import cv2
import numpy as np
#image=np.zeros((512,512,3),np.uint8)
mycolor=cv2.imread("s3.jpg")
#print(image.shape)
#image_line=cv2.line(image,(0,0),(512,512),(0,0,255),3)
image_rect=cv2.rectangle(mycolor,(195,2),(102,115),(255,0,0),4)
#eyes_rect=cv2.rectangle(image_rect,(132,51),(117,67),(0,255,0),2)
eyes_rect=cv2.rectangle(image_rect,(130,54),(116,66),(0,255,0),2)
eyes_rect2=cv2.rectangle(eyes_rect,(159,53),(140,64),(0,255,0),2)
#cv2.imshow("black",image)
cv2.imshow("rect",image_rect)
cv2.waitKey()
cv2.destroyAllWindows()