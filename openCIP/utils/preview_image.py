'''
Function to allow a user to preview a frame of the video while choosing
how to process it
'''


import cv2 as cv
import numpy as np


def preview_image(img: np.array):
    '''
    Previews a frame during processing.
    Parameters:
        img: np.array - The image to show
    Returns:
        void
    '''
    cv.imshow("Preview Frame. Press Q to exit.", img)

    cv.waitKey("Q")
    cv.destroyAllWindows()
