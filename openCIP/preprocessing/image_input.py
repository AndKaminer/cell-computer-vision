'''Functions for preprocessing a video'''

import cv2 as cv
import numpy as np

from utils import preprocess_choice
from utils import choose_brightness
from utils import choose_contrast
from utils import confirm_and_preview
from config import Config


def preprocess_video(filename: str):
    '''
    Preprocesses the video and writes the new, preprocessed, video to a file.
    Parameters:
        filename: str - The filename of the video to be preprocessed
        intermediate_dir: str - String with the intermediate files directory
    Returns:
        NEW_FILENAME: str - The filename of the new, preprocessed, video.
    '''

    NEW_FILENAME = Config.intermediate_dir + "preprocessed.mp4"
    VIDEO_CODEC = "MP4V"

    video = cv.VideoCapture(filename)
    Config.fps = video.get(cv.cv2.CAP_PROP_FPS)
    Config.width = video.get(cv.cv2.CAP_PROP_WIDTH)
    Config.height = video.get(cv.cv2.CAP_PROP_HEIGHT)
    Config.framecount = int(video.get(cv.cv2.CAP_PROP_FRAME_COUNT))

    out = cv.VideoWriter(NEW_FILENAME,
                         cv.VideoWriter_fourcc(*VIDEO_CODEC),
                         Config.fps,
                         (Config.width, Config.height)
                         )

    redo = True
    while redo:
        choice: int = preprocess_choice()
        amount: int = 0
        if choice == 6:
            amount = choose_brightness(True)
        elif choice == 7:
            amount = choose_brightness(False)
        elif choice == 8:
            amount = choose_contrast(True)
        elif choice == 9:
            amount = choose_contrast(False)

        redo = confirm_and_preview()

    for frame in range(Config.framecount):
        ret, img = video.read()

        if not ret:
            break

        img = preprocess_image(img, choice, amount)
        out.write(img)

    video.release()
    out.release()
    return NEW_FILENAME


def preprocess_image(img: np.array, choice: int) -> np.array:
    '''
    Takes an image of the video from preprocess_video and does some sort of
    preprocessing on it.
    Parameters:
        img: np.array - The image to be processed
    Returns:
        img: np.array - The new, processed, image
    '''
    return img
