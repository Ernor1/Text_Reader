import cv2
import matplotlib.pyplot as plt

img_path="C:\\Users\honor\\Downloads\\lenna.jpeg"
image= cv2.imread(img_path)
cv2.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# plt.title("LENNA")
# plt.show()