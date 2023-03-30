import numpy as np
from PIL import Image
import cv2
from Sequances import get_sequances
from CONST import *
from catmap import catMap


def entropy(im):
    # Compute normalized histogram -> p(g)
    p = np.array([(im==v).sum() for v in range(256)])
    p = p/p.sum()
    # Compute e = -sum(p(g)*log2(p(g)))
    e = -(p[p>0]*np.log2(p[p>0])).sum()
    
    return e


path = 'Images/baboon.jpg'

image = cv2.imread(path)
img = cv2.imread(path)

Subtitution_iterations = 300

I = catMap(image, Subtitution_iterations)
#Ir = np.copy(catMap(image[..., 2], Subtitution_iterations))
#Ig = np.copy(catMap(image[..., 1], Subtitution_iterations))
#Ib = np.copy(catMap(image[..., 0], Subtitution_iterations))

img = cv2.imread(path)

W, H = img.shape[:2]
iterations = W*H
s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)

s1 = np.round((s1 * 10 ** 14) % 256).astype(int).reshape(W, H)
s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(W, H)
s6 = np.round((s6 * 10 ** 14) % 256).astype(int).reshape(W, H)


Cb = I[..., 2] ^ s4 #image[..., 2] ^ s4
Cg = I[..., 1] ^ s4 #image[..., 1] ^ s4
Cr = I[..., 0] ^ s4 #image[..., 0] ^ s4

print('R:',entropy(img[..., 2]))
print('G:',entropy(img[..., 1]))
print('B:',entropy(img[..., 0]))

print()

print('C r: ', entropy(Cr))
print('C b: ', entropy(Cb))
print('C g: ', entropy(Cg))
