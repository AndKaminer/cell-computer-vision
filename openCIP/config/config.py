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
    video_height: int = 1080
    working_directory: str = os.getcwd()
    intermediate_dir: str = os.getcwd()
    framecount: int = 0
    logging_level: int = logging.INFO
    logging_format: str = "%(asctime)s %(levelname)s %(message)s"
    terminal_width: int = 60
