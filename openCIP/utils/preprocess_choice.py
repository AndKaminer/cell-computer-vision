'''Util for cli to choose which method of preprocessing happens.'''


from config import Config


def preprocess_choice() -> int:
    '''
    Manages choosing and previewing different preprocessing for the video.
    '''
    if Config.GUI:
        return preprocess_choice_GUI()
    else:
        return preprocess_choice_CLI()


def preprocess_choice_GUI() -> int:
    '''
    Provides an interface for choosing and previewing different preprocessing
    types in GUI mode.
    '''
    pass


def preprocess_choice_CLI() -> int:
    '''
    Provides an interface for choosing and previewing different preprocessing
    types in CLI mode.
    '''
    pass

    # IMAGE GRADIENTS/FILTERS TO IMPLEMENT:
    # Sobel
    # Scharr
    # Laplacian
    # Gauss
    # Brightness up
    # Brightness down
    # Contrast up
    # Contrast down
    # Canny
