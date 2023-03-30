''' image encryption and decryption '''
''' Generate Pseudo-random numbers sequances using 6D-CNN (Cellular Neural Network) '''
''' encrypt and decrypt image using one of those sequances and XOR method '''

import numpy as np
import cv2
from CONST import *
from Sequances import get_sequances
import matplotlib.pyplot as plt
from PIL import Image


fig, axs = plt.subplots(1, 3, figsize=(14, 4)) 


''' open image'''

path = 'Images/baboon.jpg'
img = cv2.imread(path)

# show original image
cv2.imshow('Original Image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#axs[0].set_ylim([0, 5500])
axs[0].hist(img[..., 0].ravel(), 256, [0,256], color = 'r', linewidth=0.5) 
axs[0].hist(img[..., 1].ravel(), 256, [0,256], color = 'g', linewidth=0.5) 
axs[0].hist(img[..., 2].ravel(), 256, [0,256], color = 'b', linewidth=0.5) 
axs[0].set_title('original image')

H, W = img.shape[:2]
iterations = H * W


''' generate pseudo-random numbers sequances '''

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)

s1 = np.round((s1 * 10 ** 14) % 256).astype(int).reshape(H, W)
s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(H, W)
s6 = np.round((s6 * 10 ** 14) % 256).astype(int).reshape(H, W)



''' encrypt image '''

img[..., 0] = img[..., 0] ^ s1
img[..., 1] = img[..., 1] ^ s4
img[..., 2] = img[..., 2] ^ s6

Image.fromarray(img.astype('uint8')).save('Images/Encrypted_Image.jpg')

# show encrypted image
cv2.imshow('encrypted image', img.astype(np.uint8))

# encrypted image histogram
axs[1].set_ylim([0, 3000])
axs[1].hist(img[..., 0].ravel(), 256, [0,256], color = 'r', linewidth=0.5) 
axs[1].hist(img[..., 1].ravel(), 256, [0,256], color = 'g', linewidth=0.5) 
axs[1].hist(img[..., 2].ravel(), 256, [0,256], color = 'b', linewidth=0.5) 
axs[1].set_title('encrypted image')




''' decrypt image '''
img[..., 0] = img[..., 0] ^ s1
img[..., 1] = img[..., 1] ^ s4
img[..., 2] = img[..., 2] ^ s6

Image.fromarray(img.astype('uint8')).save('Images/Decrypted_Image.jpg')


# decrypted image histogram
#axs[2].set_ylim([0, 5500])
axs[2].hist(img[..., 0].ravel(), 256, [0,256], color = 'r', linewidth=0.5) 
axs[2].hist(img[..., 1].ravel(), 256, [0,256], color = 'g', linewidth=0.5) 
axs[2].hist(img[..., 2].ravel(), 256, [0,256], color = 'b', linewidth=0.5) 
axs[2].set_title('decrypted image')





# show decrypted image
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('decrypted image', img.astype(np.uint8))


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

