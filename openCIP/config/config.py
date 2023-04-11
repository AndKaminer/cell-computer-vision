'''
Class containing configuration settings and video information for openCIP
'''

import os
import logging


class Config:
    '''
    Class containing configuration settings and video information for openCIP
    '''
    GUI: bool = False
    video_width: int = 1920
    video_height = 1080
    working_directory = os.getcwd()
    intermediate_dir = os.getcwd()
    framecount = 0
    logging_level = logging.INFO
    logging_format = "%(asctime)s %(levelname)s %(message)s"
