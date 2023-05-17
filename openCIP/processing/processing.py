import os

import cv2 as cv
import numpy as np

from config import Config
from utils import Util


class Processing:

    def preprocess_video() -> None:
        '''
        Assumes that there is a valid file in in config.file
        '''
        if not Config.video_filename or not os.path.isfile(
                Config.video_filename):
            raise FileNotFoundError("Video file not found")

        try:
            video = cv.VideoCapture(Config.video_filename)
        except Exception:
            raise FileNotFoundError("Video is not a supported filetype")

        # TODO: Deal with .cine files

        Config.fps = video.get(cv.CAP_PROP_FPS)
        Config.width = video.get(cv.CAP_PROP_FRAME_WIDTH)
        Config.height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
        Config.framecount = int(video.get(cv.CAP_PROP_FRAME_COUNT))

        video.release()

    def break_into_clips() -> None:
        '''
        Assumes that video has been preprocessed already
        '''
        frames = Util.get_cell_frames()

        len(frames)

    def count_objects(img: np.array) -> int:
        '''
        Assumes standard BGR cv2 image
        '''

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        blur = cv.gaussianBlur(gray, (5, 5), 0)

        t, threshold_img = cv.threshold(
                blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        new_img, contours, hierarchy = cv.findContours(
                threshold_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        return len(contours)
