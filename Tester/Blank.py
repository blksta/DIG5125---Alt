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
        return image


imagepath = processed_image('Tester\mandrill2.jpg')

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