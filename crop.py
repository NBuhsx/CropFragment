import sys
from cropp_fragment.app import App


def args():
    if "-f" in sys.argv or "-file" in sys.argv:
        pass


if __name__ == '__main__':
    print(sys.argv)
    app = App()
    app.run()
