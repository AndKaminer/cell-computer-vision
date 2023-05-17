from typing import List
import os

import cv2 as cv

from .help_message import print_help_message
from config import Config
from processing import Processing


class Util:

    def parse_cli_input(argv: List):
        '''
        Function to parse argv.
        Parameters:
            argv: List - The list of command line args
        Returns:
            GUI: boolean - Whether or not to use a gui
            filename: str - The filename of the input file
            other: List - A list of all of the other command line arguments
        '''

        help = "-h" in argv or "--help" in argv

        if help:
            print_help_message()
            raise RuntimeError("Printing help message")

        GUI = "-g" in argv

        idx = argv.index("-f")
        assert len(argv) > idx + 1
        filename = argv[idx + 1]

        assert os.path.isfile(filename)

        if "-g" in argv:
            argv.remove("-g")

        argv.remove(filename)
        argv.remove("-f")

        return GUI, filename, argv

    def get_cell_frames():
        '''
        Given the video, find all frames where there is a cell doing cell
        things
        '''

        if not Config.video_filename or not os.path.isfile(
                Config.video_filename):
            raise FileNotFoundError("Video file not found")

        try:
            video = cv.VideoCapture(Config.video_filename)
        except Exception:
            raise FileNotFoundError("Video is not a supported filetype")

        clips = []

        success, img = video.read()
        frame = 0
        while success:
            num_objects = Processing.count_objects(img)
            # TODO: implement further

            success, img = video.read()
            frame += 1

        return clips
