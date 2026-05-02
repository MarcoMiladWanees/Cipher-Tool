import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget,
                             QVBoxLayout, QRadioButton, QButtonGroup,
                             QLineEdit, QHBoxLayout, QComboBox,
                             QGroupBox, QTextEdit, QSplitter, QTreeWidget, QStackedWidget, QTreeWidgetItem)

from   PyQt5.QtGui     import QIcon, QFont
from   PyQt5.QtCore    import Qt, QThread, pyqtSignal
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS, resource_path
from registry import CLASSICAL_REGISTRY


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing the UI
        self.initUI()

    def initUI(self):
        #Window setup
        self.setWindowTitle("Kryptos")
        self.setWindowIcon(QIcon(resource_path('assets/icon.png')))
        self.resize(1200, 750)
        self.setMinimumSize(1000, 650)

        #Defining everything
        self.main_widget   = QSplitter()
        self.side_bar      = QTreeWidget()
        self.side_bar.setColumnCount(1)
        self.stacked_pages = QStackedWidget()

        #Adding stuff to the sidebar

        #Adding the Top level Items
        self.classical_ciphers = QTreeWidgetItem(self.side_bar)
        self.classical_ciphers.setText(0,"Classical Ciphers")
        self.modern_ciphers = QTreeWidgetItem(self.side_bar)
        self.modern_ciphers.setText(0,"Modern Ciphers")

        #Adding the classical ciphers
        for item in CLASSICAL_REGISTRY.keys():
            self.cipher = QTreeWidgetItem(self.classical_ciphers)
            self.cipher.setText(0,item)

        #Adding the widgets to the splitter
        self.main_widget.addWidget(self.side_bar)
        self.main_widget.addWidget(self.stacked_pages)

        #Setting the splitter as the central widget
        self.setCentralWidget(self.main_widget)
