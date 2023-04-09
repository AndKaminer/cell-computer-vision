'''Main program for the entire project'''

import sys
import os
import logging

from utils import parse_cli_input
from preprocessing import preprocess_video


def main(GUI, filename, other):
    working_dir = os.pwd()
    intermediate_dir = os.path.basename(__file__) + "/intermediate_files"

    preprocessed_file_name: str = preprocess_video(filename, intermediate_dir)
    print(preprocessed_file_name)
    print(working_dir)


if __name__ == '__main__':

    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
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

    main(GUI, filename, other)
