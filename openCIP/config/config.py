'''
Class containing configuration settings and video information for openCIP
'''

import os


class Config:
    '''
    Class containing configuration settings and video information for openCIP
    '''
    GUI: bool = False
    video_width: int = 1920
    video_height = 1080
    working_directory = os.pwd()
    intermediate_dir = os.pwd()
    framecount = 0
