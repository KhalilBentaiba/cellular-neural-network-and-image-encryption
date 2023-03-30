''' image encryption and decryption '''
''' Generate Pseudo-random numbers sequances using 6D-CNN (Cellular Neural Network) '''
''' encrypt and decrypt image using one of those sequances and XOR method '''

import numpy as np
import cv2
from CONST import *
from Sequances import get_sequances
import matplotlib.pyplot as plt


fig, axs = plt.subplots(1, 3, figsize=(12, 4))  



''' open image'''

path = 'Images/baboon.jpg'
img = cv2.imread(path, 0)


# show original image
cv2.imshow('Original Image', img)

axs[0].set_ylim([0, 10000])
axs[0].hist(img.ravel(), 256, [0,256], color='b', linewidth=0.5);
axs[0].set_title('original image')


H, W = img.shape[:2]
iterations = H * W


''' generate pseudo-random numbers sequances '''

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)


s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(H, W)



''' encrypt image '''

img = img ^ s4

# show encrypted image
cv2.imshow('encrypted image', img.astype(np.uint8))


# encrypted image histogram

axs[1].set_ylim([0, 10000])
axs[1].hist(img.ravel(), 256, [0,256], color='b', linewidth=0.5); 
axs[1].set_title('encrypted image')



''' decrypt image '''

#s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4 + 10 ** -10, x5, x6, h, iterations)
#s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(H, W)


img = img ^ s4

# show decrypted image
cv2.imshow('decrypted image', img.astype(np.uint8))

# decrypted image histogram
axs[2].set_ylim([0, 10000])
axs[2].hist(img.ravel(), 256, [0,256], color='b', linewidth=0.5); 
axs[2].set_title('decrypted image')





plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

