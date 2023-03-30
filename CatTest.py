from catmap import catMap
from PIL import Image
import numpy as np
import cv2

path = 'Images/baboon.jpg'

img = cv2.imread(path)
cv2.imshow('original IMG',img.astype(np.uint8))

I = catMap(img, 300)
cv2.imshow('encrypted IMG',I.astype(np.uint8))

I = catMap(I, 512 - 300 - 2)
cv2.imshow('decrypted IMG',I.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
