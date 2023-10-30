import cv2
import matplotlib.pyplot as plt
import numpy as np


for i in range(1,10):
    img = cv2.imread("fruit_" + str(i) + ".png")
    cv2.imshow("Image", img)
    cv2.waitKey(5000)

