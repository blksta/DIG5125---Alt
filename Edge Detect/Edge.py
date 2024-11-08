import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Dilations/lena.tiff', cv2.IMREAD_GRAYSCALE)

roberts_x = np.array([[1, 0], [0,-1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1,0]], dtype=np.float32)

edge_x = cv2.filter2D(image, -1, roberts_x)
edge_y = cv2.filter2D(image, -1, roberts_y)

edge_mag = np.sqrt(np.square(edge_x) + np.square(edge_y))
edge_mag = np.uint8(edge_mag)

plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(edge_mag, cmap='gray'), plt.title('Edge Image Roberts')
plt.show()