import cv2 # importing OpenCV
import numpy as np # importing Numpy and assign to np

image = cv2.imread("cameraman.tif", 0) # read the cameraman image in grayscale mode
cv2.imshow("Cameraman", image) # show the image in a window titled
cv2.imwrite("new_black-white_image.png", image) # save the new image in the same path

cv2.waitKey(0) # close with any key

cv2.destroyAllWindows() # close all image windows

