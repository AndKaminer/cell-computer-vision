'''Main program for the entire project'''

import sys
import os
import logging

from utils import parse_cli_input
from preprocessing import preprocess_video
from config import Config


def main(filename, other):
    Config.working_directory = os.getcwd()
    Config.intermediate_dir = (
            f"{os.path.basename(__file__)}/intermediate_files")

    preprocessed_file_name: str = preprocess_video(filename)
    print(preprocessed_file_name)


if __name__ == '__main__':

    logging.basicConfig(
            level=Config.logging_level,
            format=Config.logging_format
    )

    try:
        GUI, filename, other = parse_cli_input(sys.argv)

    except AssertionError:
        sys.exit("Invalid command line input")
    except RuntimeError:
        sys.exit(0)
    except Exception:
        sys.exit("Something went wrong")

    logging.info("Successfully parsed command line arguments")

    Config.GUI = GUI

    main(filename, other)
