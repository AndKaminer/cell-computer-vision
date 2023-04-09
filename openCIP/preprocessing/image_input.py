'''Functions for preprocessing a video'''

import cv2 as cv
import numpy as np


def preprocess_video(filename: str, intermediate_dir: str):
    '''
    Preprocesses the video and writes the new, preprocessed, video to a file.
    Parameters:
        filename: str - The filename of the video to be preprocessed
        intermediate_dir: str - String with the intermediate files directory
    Returns:
        NEW_FILENAME: str - The filename of the new, preprocessed, video.
    '''

    NEW_FILENAME = intermediate_dir + "preprocessed.mp4"
    VIDEO_CODEC = "MP4V"

    video = cv.VideoCapture(filename)
    fps = video.get(cv.cv2.CAP_PROP_FPS)
    width = video.get(cv.cv2.CAP_PROP_WIDTH)
    height = video.get(cv.cv2.CAP_PROP_HEIGHT)

    out = cv.VideoWriter(NEW_FILENAME,
                         cv.VideoWriter_fourcc(*VIDEO_CODEC),
                         fps,
                         (width, height)
                         )

    framecount = int(video.get(cv.cv2.CAP_PROP_FRAME_COUNT))

    for frame in range(framecount):
        ret, img = video.read()

        if not ret:
            break

        img = preprocess_image(img)
        out.write(img)

    video.release()
    out.release()
    return NEW_FILENAME


def preprocess_image(img: np.array) -> np.array:
    '''
    Takes an image of the video from preprocess_video and does some sort of
    preprocessing on it.
    Parameters:
        img: np.array - The image to be processed
    Returns:
        img: np.array - The new, processed, image
    '''
    return img
