import numpy as np
import matplotlib.pyplot as plt

def my_spatial_filter(my_image_name):
    I = plt.imread(my_image_name)
    if I.ndim == 3:
        I = np.mean(I, -1)

    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.show()

    mask_size = 3

    padd_size = mask_size // 2

    I_padded = np.pad(I, ((padd_size, padd_size), (padd_size, padd_size)), mode='constant')
        
    plt.imshow(I_padded, cmap='gray')
    plt.title('Padded Image')
    plt.show()

    I2 = np.zeros_like(I_padded)

    for i in range(padd_size, I_padded.shape[0]-padd_size):
        for j in range(padd_size, I_padded.shape[1]-padd_size):
            pixbuffer = I_padded[i-padd_size:i+padd_size+1, j-padd_size:j+padd_size]
            I2[i, j] = np.median(pixbuffer)

    my_filtered_image = I2[padd_size:-padd_size, padd_size:-padd_size]

    plt.imshow(my_filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.show()

    return my_filtered_image
    
filtered_image = my_spatial_filter('Filters\SaltPeppernoise.png')