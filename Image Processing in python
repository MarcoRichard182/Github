import cv2
import numpy as np

img = cv2.imread("gambar15.jpg")

resize = cv2.resize(img,(250, 250))
hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

lower_blue = np.array([75, 80, 2])      # low_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_pink = np.array([170, 50, 50]) #light red not pink
upper_pink = np.array([180, 255, 255])

lower_purple = np.array([130, 50, 50])
upper_purple = np.array([160, 255, 255])

#mask color
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)


mask =  mask_pink
# gambar4.png mask = mask_pink+mask_blue
# gambar9.jpg mask = mask_green + mask_blue + mask_pink
# gambar 12.jpg mask = mask_red + mask_blue + mask_yellow +mask_green
# gambar 13.jpg mask = mask_red + mask_pink + mask_blue + mask_yellow +mask_green
# gambar 15.jpg mask = mask_pink + mask_blue +mask_green 

result = cv2.bitwise_and(resize, resize, mask=mask)

cv2.imshow("rezise", resize)
cv2.imshow("hsv", hsv)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


