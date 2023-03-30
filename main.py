import numpy as np
from catmap import catMap
from Sequances import get_sequances
from CONST import *
import cv2

path = 'Images/baboon.jpg'
img = cv2.imread(path)
H, W = img.shape[:2]
cv2.imshow('Original Image', img)

'''''' """ PART 1 - Subtitution Encryption - """ ''''''

''' using subtitution method to shuffle the pixels position '''


''' Arnold's Cat Map '''

Subtitution_iterations = 300

I = catMap(img, Subtitution_iterations)
cv2.imshow('CatMap Encryption', I.astype(np.uint8))


'''''' """ PART 2 - Diffusion Encryption - """ ''''''

''' the diffusion method is used to change the pixels color '''
''' this part will go with the steps as follow '''


""" Step 1 - get systems of equations -"""

''' Generating the sequances is done by using 6D-CNN (Cellular Neural Network) systems of equations '''

''' we get from 6D-CNN the following system of equations '''
''' 
    dx1 = - x3 - 1.2 * x4
    dx2 = 2 * x2 + x3
    dx3 = 11 * x1 - 12 * x2
    dx4 = 92 * x1 - 95 * x4 + x5 - x6 + 202 * (abs(x4 + 1) - abs(x4 - 1))
    dx5 = 5 * x3 - x5
    dx6 = 5 * x4 - 12 * x6
'''



""" Step 2 - generate pseudo-random numbers sequances - """

''' using Runge-Kutta 4-order method to solve the system of equations '''
''' by solving the equations we get the following 6 pseudo-random numbers sequances '''


''' number of iterations is the size of the image '''

iterations = W*H

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)



""" Step 3 - Encrypt the image - """

''' using XOR method and one of the 6 sequance e generated to encrypt the image '''

# adjust the sequance to be around 0 and 255 [0, 255] and shaped as the image
s1 = np.round((s1 * 10 ** 14) % 256).astype(int).reshape(H, W)
s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(H, W)
s6 = np.round((s6 * 10 ** 14) % 256).astype(int).reshape(H, W)

# encrypt with XOR method
I[..., 2] = I[..., 2] ^ s1
I[..., 1] = I[..., 1] ^ s4
I[..., 0] = I[..., 0] ^ s6

cv2.imshow('XOR Encrytion', I.astype(np.uint8))




'''''' """ PART 3 - Diffusion Decryption - """ ''''''

''' the decryption will be the same as the ecryption using XOR method and the same sequance '''

I[..., 2] = I[..., 2] ^ s1
I[..., 1] = I[..., 1] ^ s4
I[..., 0] = I[..., 0] ^ s6
cv2.imshow('XOR Decrytion', I.astype(np.uint8))



'''''' """ PART 4 - Diffusion Decryption - """ ''''''

I = catMap(I, 512 - Subtitution_iterations - 2)
cv2.imshow('CatMap Decryption', I.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
