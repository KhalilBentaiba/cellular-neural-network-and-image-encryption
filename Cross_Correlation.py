from matplotlib import markers
import numpy as np
from PIL import Image
import cv2
from CONST import *
from Sequances import get_sequances
import pandas as pd
import matplotlib.pyplot as plt
from catmap import catMap


def corrH(img, u, v):
    Eu = img[:, u].mean()
    Ev = img[:, v].mean()

    #print(Eu, Ev)

    Du = ((img[:, u] - Eu) ** 2).mean()
    Dv = ((img[:, v] - Ev) ** 2).mean()

    #print(Du, Dv)

    cov = ((img[:, u] - Eu) * (img[:, v] - Ev)).mean()

    #print(cov)

    r = cov / (np.sqrt(Du) * np.sqrt(Dv))

    return r


def corrV(img, u, v):
    Eu = img[u, :].mean()
    Ev = img[v, :].mean()

    #print(Eu, Ev)

    Du = ((img[u, :] - Eu) ** 2).mean()
    Dv = ((img[v, :] - Ev) ** 2).mean()

    #print(Du, Dv)

    cov = ((img[u, :] - Eu) * (img[v, :] - Ev)).mean()

    #print(cov)

    r = cov / (np.sqrt(Du) * np.sqrt(Dv))

    return r
    


def corrD(img, u, v):
    Eu = img.diagonal(u)[:-1].mean()
    Ev = img.diagonal(v).mean()

    #print(Eu, Ev)

    Du = ((img.diagonal(u)[:-1] - Eu) ** 2).mean()
    Dv = ((img.diagonal(v) - Ev) ** 2).mean()

    #print(Du, Dv)

    cov = ((img.diagonal(u)[:-1] - Eu) * (img.diagonal(v) - Ev)).mean()

    #print(cov)

    r = cov / (np.sqrt(Du) * np.sqrt(Dv))

    return r

def corrP(s1, s2):

    E1 = s1.mean()
    E2 = s2.mean()

    cov = ((s1 - E1) * (s2 - E2)).mean()

    D1 = ((s1 - E1) ** 2).mean()
    D2 = ((s2 - E2) ** 2).mean()

    r = cov / (np.sqrt(D1) * np.sqrt(D2))

    print('P r: ',r)
    


def invCorrD(img, u, v):
    Eu = img.diagonal(u).mean()
    Ev = img.diagonal(v)[:-1].mean()

    Du = ((img.diagonal(u) - Eu) ** 2).mean()
    Dv = ((img.diagonal(v)[:-1] - Ev) ** 2).mean()

    cov = ((img.diagonal(u) - Eu) * (img.diagonal(v)[:-1] - Ev)).mean()

    r = cov / (np.sqrt(Du) * np.sqrt(Dv))

    return r


path = 'Images/Lenna.png'

image = np.array(Image.open(path))
img = np.array(Image.open(path))

Subtitution_iterations = 300


I = catMap(image, Subtitution_iterations)


#Ir = I[..., 0]
#Ig = I[..., 1]
#Ib = I[..., 2]



W, H = img.shape[:2]
iterations = W*H
s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)

#corrP(s3, s6)
#print()
s4 = np.round((s4 * 10 ** 14) % 256).astype(int).reshape(H, W)
s1 = np.round((s1 * 10 ** 14) % 256).astype(int).reshape(H, W)
s5 = np.round((s5 * 10 ** 14) % 256).astype(int).reshape(H, W)


Cr = I[..., 0] ^ s1
Cg = I[..., 1] ^ s4
Cb = I[..., 2] ^ s5

Image.fromarray(img.astype('uint8')).show()

#I[..., 0] = Cr
#I[..., 1] = Cg
#I[..., 2] = Cb


""" ''' Horizontal ''' """

Hb = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hr = np.zeros(W-1, dtype=np.float64)
for i in range(1, W):
    Hr[i-1] = corrH(img[..., 0], i-1, i)
    Hg[i-1] = corrH(img[..., 1], i-1, i)
    Hb[i-1] = corrH(img[..., 2], i-1, i)

print('original H Red:', Hr.mean())
print('original H Green:', Hg.mean())
print('original H Blue:', Hb.mean())

print()

Hr = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hb = np.zeros(W-1, dtype=np.float64)
for i in range(1, W):
    Hr[i-1] = corrH(Cr, i-1, i)
    Hg[i-1] = corrH(Cg, i-1, i)
    Hb[i-1] = corrH(Cb, i-1, i)

print('encrypted H Red:', Hr.mean())
print('encrypted H Green:', Hg.mean())
print('encrypted H Blue:', Hb.mean())
print()
print('encrypt H MEAN:',(Hr.mean() + Hb.mean() + Hr.mean()) / 3)
print()





""" ''' Vertical ''' """



Hr = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hb = np.zeros(W-1, dtype=np.float64)
for i in range(1, W):
    Hr[i-1] = corrV(img[..., 0], i-1, i)
    Hg[i-1] = corrV(img[..., 1], i-1, i)
    Hb[i-1] = corrV(img[..., 2], i-1, i)

print('original V Red:', Hr.mean())
print('original V Green:', Hg.mean())
print('original V Blue:', Hb.mean())


print()

Hb = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hr = np.zeros(W-1, dtype=np.float64)
for i in range(1, W):
    Hr[i-1] = corrV(Cr, i-1, i)
    Hg[i-1] = corrV(Cg, i-1, i)
    Hb[i-1] = corrV(Cb, i-1, i)

print('encrypted V Red:', Hr.mean())
print('encrypted V Green:', Hg.mean())
print('encrypted V Blue:', Hb.mean())
print()
print('encrypt V MEAN:',(Hr.mean() + Hb.mean() + Hr.mean()) / 3)
print()



""" ''' Diagonal ''' """


Hb = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hr = np.zeros(W-1, dtype=np.float64)

for i in range(-W//2, 0):
    Hr[i + W//2] = invCorrD(img[..., 0], i, i+1)
    Hg[i + W//2] = invCorrD(img[..., 1], i, i+1)
    Hb[i + W//2] = invCorrD(img[..., 2], i, i+1)

for i in range(1, W//2):
    Hr[i + W//2 - 1] = corrD(img[..., 0], i-1, i)
    Hg[i + W//2 - 1] = corrD(img[..., 1], i-1, i)
    Hb[i + W//2 - 1] = corrD(img[..., 2], i-1, i)


print('original D Red:', Hr.mean())
print('original D Green:', Hg.mean())
print('original D Blue:', Hb.mean())

print()

Hb = np.zeros(W-1, dtype=np.float64)
Hg = np.zeros(W-1, dtype=np.float64)
Hr = np.zeros(W-1, dtype=np.float64)

for i in range(-256, 0):
    Hr[i + W//2] = invCorrD(Cr, i, i+1)
    Hg[i + W//2] = invCorrD(Cg, i, i+1)
    Hb[i + W//2] = invCorrD(Cb, i, i+1)

for i in range(1, 256):
    Hr[i + W//2 - 1] = corrD(Cr, i-1, i)
    Hg[i + W//2 - 1] = corrD(Cg, i-1, i)
    Hb[i + W//2 - 1] = corrD(Cb, i-1, i)

print('encrypt D Red:', Hr.mean())
print('encrypt D Green:', Hg.mean())
print('encrypt D Blue:', Hb.mean())
print()
print('encrypt D MEAN:',(Hr.mean() + Hg.mean() + Hb.mean())/3.)
