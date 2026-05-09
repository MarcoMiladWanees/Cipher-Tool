import os
import sys

from PyQt5.QtCore import QPoint

class UICONSTANTS:
    WINOW_WIDTH = 1200
    WINOW_HEIGHT = 700
    IO_WIDTH = WINOW_WIDTH-100
    IO_HEIGHT = 175
    SIDEBAR_WIDTH = 280
    TOGGLE_X_EXPANDED = SIDEBAR_WIDTH + 8
    TOGGLE_X_COLLAPSED = 8
    TOGGLE_Y = 8
    TOGGLE_POS_COLLAPSED = QPoint(TOGGLE_X_COLLAPSED, TOGGLE_Y)
    TOGGLE_POS_EXPANDED = QPoint(TOGGLE_X_EXPANDED, TOGGLE_Y)
    ANIMATION_TIME = 500

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)