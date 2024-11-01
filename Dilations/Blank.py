import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np 
import cv2

def processed_image(filename):
    ImageA = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

    if ImageA is None:
        print("Error: Could not read the image.")
        exit()

    dims = np.shape(ImageA)

    if len(dims) == 3 and dims[2] == 3:
        Imagea1 = cv2.cvtColor(ImageA, cv2.COLOR_BGR2GRAY)
        print('Turn into a grayscale')
        return Imagea1

    elif len(dims) == 3 and dims[2] > 3:
        print('Image A is not an RGB image')
        exit()
        return None

    else:
        print('Image A is a Grayscale Image, no conversion needed')
        return ImageA


imagepath = processed_image('Tester\mandrill2.jpg')
ImageA = imagepath
ImageB = 'Tester\lena.tiff'

# comparing image sizes
ImageA_RGB = cv2.imread('Tester\lena.tiff', cv2.IMREAD_COLOR)
ImageB_RGB = cv2.imread('Tester\mandrill2.jpg', cv2.IMREAD_COLOR)

if ImageA_RGB is None or ImageB_RGB is None:
    print("Error could not read both images")
    exit()

ImageA1 = cv2.cvtColor(ImageA_RGB, cv2.COLOR_BGR2GRAY)
ImageB1 = cv2.cvtColor(ImageB_RGB, cv2.COLOR_BGR2GRAY)

sizeA = ImageA1.shape
sizeB = ImageB1.shape

if sizeA != sizeB:
    print("Images are different sizes. Resizing to match ImageA1")
    ImageB1 = cv2.resize(ImageB1, (sizeA[1], sizeA[0]))
else:
    print("Images are the same size, continue")

_, ImageA2 = cv2.threshold(ImageA1, 127, 255, cv2.THRESH_BINARY)
_, ImageB2 = cv2.threshold(ImageA1, 127, 255, cv2.THRESH_BINARY)

ImageC = cv2.bitwise_and(ImageA2, ImageB2)

fig = plt.figure()
gs = gridspec.GridSpec(2, 5, width_ratios=[1,1,1,2,2], height_ratios=[2,1])

ax1 = plt.subplot(gs[0])
ax1.imshow(cv2.cvtColor(ImageA_RGB, cv2.COLOR_BGR2RGB))
ax1.set_title('Original A')
ax1.axis('off')

ax2 = plt.subplot(gs[1])
ax2.imshow(ImageA1, cmap='gray')
ax2.set_title('Gray scale')
ax2.axis('off')

ax3 = plt.subplot(gs[2])
ax3.imshow(ImageA2, cmap='gray')
ax3.set_title('Binary')
ax3.axis('off')

ax4 = plt.subplot(gs[5])
ax4.imshow(cv2.cvtColor(ImageB_RGB, cv2.COLOR_BGR2RGB))
ax4.set_title('Original B')
ax4.axis('off')

ax5 = plt.subplot(gs[6])
ax5.imshow(ImageB1, cmap='gray')
ax5.set_title('Gray scale')
ax5.axis('off')

ax6 = plt.subplot(gs[7])
ax6.imshow(ImageB1, cmap='gray')
ax6.set_title('BW')
ax6.axis('off')

ax5 = plt.subplot(gs[3:5])
ax5.imshow(ImageC, cmap='gray')
ax5.set_title('and Image')
ax5.axis('off')

plt.tight_layout()
plt.show()