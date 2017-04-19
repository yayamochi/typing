#coding:utf-8
import cv2
import numpy as np
import tesseract

org_image_name  = "image.png"
gray_image_name = org_image_name[:-4] + "_gray.png"

org_image = cv2.imread(org_image_name,0)

#8近傍の定義
neiborhood8 = np.array([[1, 1, 1],[1, 1, 1], [1, 1, 1]],np.uint8)
neiborhood4 = np.array([[0, 1, 0],[1, 1, 1], [0, 1, 0]],np.uint8)

"""org_image = cv2.erode(org_image,neiborhood8,iterations=1)
org_image = cv2.dilate(org_image,neiborhood8,iterations=1)"""


org_image = 255 - org_image
ret,org_image = cv2.threshold(org_image,20,255,cv2.THRESH_BINARY)

cv2.imwrite(gray_image_name,org_image)
