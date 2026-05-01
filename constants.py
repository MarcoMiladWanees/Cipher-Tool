import sys
import os

class UICONSTANTS:
    WINOW_WIDTH = 1200
    WINOW_HEIGHT = 700


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)