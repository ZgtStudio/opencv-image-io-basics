import cv2 # import OpenCV2

image = cv2.imread("bird.jpg") # read the image
if image is None:
    raise FileNotFoundError("bird.jpg not found. Check the file path.") # debug

cv2.imshow("Bird", image)  # show the image in a window titled "Bird"

 # Explore the Matrix in terminal
print("Shape:", image.shape)    # (height, width, channels)
print("Dtype:", image.dtype)    # data type, e.g. uint8
print("Min/Max:", image.min(), image.max())

# wait for a key press and then close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()