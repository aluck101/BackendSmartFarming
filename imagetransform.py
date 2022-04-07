import base64
from PIL import Image
import cv2 as cv
import numpy as np


def stringToRGB(base64_string):
    imageData = base64.b64decode(str(base64_string))
    return imageData


def img_normalize(image):
    img = cv.imread(image)
    normImge = np.zeros((800, 800))
    normalized_img = (img, normImge, 0, 255, cv.NORM_MINMAX)
    return normalized_img


def gradient_filter(image):
    depth = cv.CV_64F
    kernal_size = 5
    img = cv.imread(image)
    lapl_img = cv.Laplacian(img, depth, ksize=kernal_size)
    return lapl_img
