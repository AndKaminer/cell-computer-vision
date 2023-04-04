from FIDA import FidaApp


class ApplicationTest:

    def runtests():
        errors = []
        errors.append(ApplicationTest.test_initialize())

        print(errors)

    def test_initialize():
        try:
            FidaApp()
        except Exception:
            return False
        return True


if __name__ == '__main__':
    ApplicationTest.runtests()
