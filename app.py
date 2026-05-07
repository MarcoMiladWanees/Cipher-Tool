from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QSplitter, QTreeWidget, QStackedWidget, QTreeWidgetItem)

from constants import resource_path
from registry import CLASSICAL_REGISTRY, PAGES_DIC


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing the UI
        self.initUI()
        self.side_bar.itemClicked.connect(self.on_side_bar_clicked)

    def initUI(self):
        #Window setup
        self.setWindowTitle("Kryptos")
        self.setWindowIcon(QIcon(resource_path('assets/icon.png')))
        self.resize(1200, 750)
        self.setMinimumSize(1000, 650)

        #Defining everything
        self.main_widget   = QSplitter()
        self.side_bar      = QTreeWidget()
        self.side_bar.setHeaderHidden(True)
        self.side_bar.setMinimumWidth(350)
        self.side_bar.setMaximumWidth(400)
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
            sub_cat = QTreeWidgetItem(self.classical_ciphers)
            sub_cat.setText(0,item)
            for cipher in CLASSICAL_REGISTRY[item]:
                name, key, PageCLass = cipher
                tree_item = QTreeWidgetItem(sub_cat)
                tree_item.setText(0,name)
                tree_item.setData(0,Qt.UserRole, key)
                page = PageCLass()
                self.stacked_pages.addWidget(page)
                PAGES_DIC[key] = page

        #Adding the widgets to the splitter
        self.side_bar.expandAll()
        self.main_widget.addWidget(self.side_bar)
        self.main_widget.addWidget(self.stacked_pages)
        self.main_widget.setStretchFactor(0, 1)
        self.main_widget.setStretchFactor(1, 1)


        #Setting the splitter as the central widget
        self.setCentralWidget(self.main_widget)


    def on_side_bar_clicked(self, item):
        key = item.data(0, Qt.UserRole)
        if key:
            self.stacked_pages.setCurrentWidget(PAGES_DIC[key])