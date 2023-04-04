import imagej


class FidaApp:

    def __init__(self, verbose=False):
        try:
            self.ij = imagej.init()
        except Exception:
            if verbose:
                print("ImageJ failed to initialize. Exiting now.")
            raise Exception("ImageJ failed to initialize")

        if verbose:
            print(f"ImageJ {self.ij.getVersion()} successfully initialized.")


if __name__ == '__main__':
    fa = FidaApp(verbose=True)
