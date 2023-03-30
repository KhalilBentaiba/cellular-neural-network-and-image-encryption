import numpy as np

def catMap(image, iterations):
    I = np.zeros_like(image)
    H, W = image.shape[:2]

    Ys, Xs = np.mgrid[0 : H, 0 : W]

    for _ in range(iterations):
        nX = np.round(Xs + 2 * Ys).astype(int) % H
        nY = np.round(Xs + Ys).astype(int) % W
    
        image[nY, nX] = image[Ys, Xs]

    try: I[nY, nX] = image[Ys, Xs]
    except: return image
    return I