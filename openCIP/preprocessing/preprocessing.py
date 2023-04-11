'''Class for all of the preprocessing options'''

import numpy as np
import cv2 as cv


class Preprocessing:
    '''
    Class for each of the preprocessing options
    '''

    def sobel_processing(img: np.array) -> np.array:
        pass

    def scharr_processing(img: np.array) -> np.array:
        pass

    def laplacian_processing(img: np.array) -> np.array:
        pass

    def gauss_processing(img: np.array) -> np.array:
        pass

    def change_brightness(img: np.array, amount: int) -> np.array:
        pass

    def change_contrast(img: np.array, amount: int) -> np.array:
        pass

    def canny_processing(img: np.array) -> np.array:
        pass
