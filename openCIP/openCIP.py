'''Main program for the entire project'''

import sys
import os
import logging

from utils import Util
from config import Config
from processing import Processing


def main():

    Config.working_directory = os.getcwd()

    logging.basicConfig(
            level=Config.logging_level,
            format=Config.logging_format
    )
    try:
        GUI, filename, other = Util.parse_cli_input(sys.argv)

    except AssertionError:
        sys.exit("Invalid command line input")
    except RuntimeError:
        sys.exit(0)
    except Exception:
        sys.exit("Something went wrong")

    logging.info("Successfully parsed command line arguments")

    Config.GUI = GUI
    Config.video_filename = filename
    Processing.preprocess_video()


if __name__ == '__main__':
    main()
