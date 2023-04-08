'''File with functions to parse cli args'''


from .help_message import print_help_message


def parse_cli_input(argv):
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
    assert idx != -1
    assert len(argv) > idx + 1
    filename = argv[idx + 1]

    if "-g" in argv:
        argv.remove("-g")

    argv.remove(filename)
    argv.remove("-f")

    return GUI, filename, argv
