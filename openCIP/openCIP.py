'''Main program for the entire project'''

import sys
import logging

from utils import parse_cli_input


def main(GUI, filename, other):
    pass


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
