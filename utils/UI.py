from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QSize
from PyQt5.QtGui import QIcon, QFont, QBrush, QColor, QKeySequence, QPainter
from PyQt5.QtWidgets import (QMainWindow, QTreeWidget, QStackedWidget, QTreeWidgetItem, QPushButton,
                             QShortcut, QWidget, QHBoxLayout)

from pages import welcome_page
from pages.welcome_page import WelcomePage
from utils.constants import resource_path
from utils.registry import CLASSICAL_REGISTRY, PAGES_DIC
from utils.constants import UICONSTANTS

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

        #icons
        self.menu_icon = QIcon(resource_path("assets/menu.svg"))
        self.chevron_icon = QIcon(resource_path("assets/chevron-right.svg"))
        self.close_icon = QIcon(resource_path("assets/x.svg"))
        #Defining everything
        self.main_widget   = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_widget.setLayout(self.main_layout)

        #defining the toggle button

        self.toggle_button = QPushButton("x",self)
        self.toggle_button.setIcon(self.chevron_icon)
        self.toggle_button.setIconSize(QSize(24, 24))
        self.toggle_button.setText("")
        self.toggle_button.setObjectName("toggleButton")
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.move(UICONSTANTS.TOGGLE_X_COLLAPSED, UICONSTANTS.TOGGLE_Y)

        self.side_bar_button_shortcut = QShortcut(QKeySequence("Ctrl+S"), self) #defining the button shortcut

        # X button
        self.close_button = QPushButton("X",self)
        self.close_button.setIcon(self.close_icon)
        self.close_button.setIconSize(QSize(24, 24))
        self.close_button.setText("")
        self.close_button.setObjectName("closeButton")
        self.close_button.setFixedSize(40, 40)
        self.close_button.move(UICONSTANTS.TOGGLE_X_COLLAPSED, UICONSTANTS.TOGGLE_Y)
        self.close_button.hide()

        # items' font
        self.sidebar_font = QFont()
        self.sidebar_font.setWeight(450)
        self.sidebar_font.setPointSize(11)
        self.sidebar_font.setFamily("Segoe UI")

        self.side_bar      = QTreeWidget() #defining the sidebar
        self.side_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.side_bar_collapsed = True

        self.side_bar.setIndentation(0) #setting up the indentation
        self.side_bar.setHeaderHidden(True) # hiding the header

        # Lock sidebar to a fixed width using equal min/max.
        # Both must be animated together (see sidebar_animation + sidebar_min_animation)
        # so the widget can collapse without the layout fighting back.
        self.side_bar.setMinimumWidth(0) #sidebar's min width
        self.side_bar.setMaximumWidth(0) #sidebar's max width
        self.side_bar.setColumnCount(1) #setting up the column count
        self.side_bar.setFont(self.sidebar_font) #setting up the font

        # sidebar animation
        self.sidebar_animation = QPropertyAnimation(self.side_bar, b"maximumWidth")
        self.sidebar_animation.setDuration(UICONSTANTS.ANIMATION_TIME)
        self.sidebar_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.sidebar_min_animation = QPropertyAnimation(self.side_bar, b"minimumWidth")
        self.sidebar_min_animation.setDuration(UICONSTANTS.ANIMATION_TIME)
        self.sidebar_min_animation.setEasingCurve(QEasingCurve.InOutCubic)

        # button animation
        self.button_animation = QPropertyAnimation(self.toggle_button, b"pos")
        self.button_animation.setDuration(UICONSTANTS.ANIMATION_TIME)
        self.button_animation.setEasingCurve(QEasingCurve.InOutCubic)

        #pages stack
        self.stacked_pages = QStackedWidget()
        self.welcome_page = WelcomePage()
        self.stacked_pages.addWidget(self.welcome_page)
        #Adding stuff to the sidebar

        #Adding the Top level Items
        self.classical_ciphers = self._make_category_item("Classical")
        self.modern_ciphers = self._make_category_item("Modern")

        #Adding the classical ciphers
        for cipher in CLASSICAL_REGISTRY:
            name, key, PageClass = cipher
            tree_item = QTreeWidgetItem(self.classical_ciphers)
            tree_item.setText(0,f"# {name}")
            tree_item.setData(0,Qt.UserRole, key)
            page = PageClass()
            self.stacked_pages.addWidget(page)
            PAGES_DIC[key] = page

        #Adding the widgets to the splitter
        self.side_bar.expandAll()
        self.main_layout.addWidget(self.side_bar)
        self.main_layout.addWidget(self.stacked_pages)

        #Setting the splitter as the central widget
        self.setCentralWidget(self.main_widget)


        self.toggle_button.raise_()
        self.close_button.raise_()

        #signals....
        self.toggle_button.clicked.connect(self.on_toggle_button_clicked)
        self.side_bar_button_shortcut.activated.connect(self.on_toggle_button_clicked)
        self.side_bar.itemClicked.connect(self.on_side_bar_item_clicked)
        self.sidebar_animation.finished.connect(self.on_sidebar_animation_finished)
        self.close_button.clicked.connect(self.on_close_clicked)
        self.stacked_pages.currentChanged.connect(self.on_page_changed)

    def on_close_clicked(self):
        self.stacked_pages.setCurrentWidget(self.welcome_page)

    def on_page_changed(self):
        if self.stacked_pages.currentWidget() == self.welcome_page:
            self.close_button.hide()
        else:
            self.close_button.show()

    def on_side_bar_item_clicked(self, item):
        key = item.data(0, Qt.UserRole)
        if key:
            self.stacked_pages.setCurrentWidget(PAGES_DIC[key])

    def on_toggle_button_clicked(self):
        # Animate min and max in parallel so the widget's actual width
        # (always clamped to min ≤ width ≤ max) follows smoothly.
        if not self.toggle_button.isEnabled():
            return
        self.toggle_button.setEnabled(False)
        if self.side_bar_collapsed:
            start, end = 0, UICONSTANTS.SIDEBAR_WIDTH
            b_start, b_end =  UICONSTANTS.TOGGLE_POS_COLLAPSED, UICONSTANTS.TOGGLE_POS_EXPANDED
        else:
            start, end = UICONSTANTS.SIDEBAR_WIDTH, 0
            b_start, b_end =  UICONSTANTS.TOGGLE_POS_EXPANDED, UICONSTANTS.TOGGLE_POS_COLLAPSED

        self.sidebar_animation.setStartValue(start)
        self.sidebar_animation.setEndValue(end)
        self.sidebar_min_animation.setStartValue(start)
        self.sidebar_min_animation.setEndValue(end)
        self.button_animation.setStartValue(b_start)
        self.button_animation.setEndValue(b_end)

        self.button_animation.start()
        self.sidebar_animation.start()
        self.sidebar_min_animation.start()

        self.side_bar_collapsed = not self.side_bar_collapsed
        if self.side_bar_collapsed:
            self.toggle_button.setIcon(self.chevron_icon)
        else:
            self.toggle_button.setIcon(self.menu_icon)

    def on_sidebar_animation_finished(self):
        self.toggle_button.setEnabled(True)

    def resizeEvent(self, event):
        if self.side_bar_collapsed:
            self.toggle_button.move(UICONSTANTS.TOGGLE_X_COLLAPSED, UICONSTANTS.TOGGLE_Y)
        else:
            self.toggle_button.move(UICONSTANTS.TOGGLE_X_EXPANDED, UICONSTANTS.TOGGLE_Y)
        self.close_button.move(self.width() - 40 - UICONSTANTS.TOGGLE_X_COLLAPSED, UICONSTANTS.TOGGLE_Y)

        super().resizeEvent(event)

    def _make_category_item(self, text):
        top_level_font = QFont()
        top_level_font.setPointSize(9)
        top_level_font.setFamily("Segoe UI")
        top_level_font.setWeight(300)
        top_level_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)
        item = QTreeWidgetItem(self.side_bar)
        item.setText(0, text)
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable )
        item.setFont(0, top_level_font)
        item.setForeground(0, QBrush(QColor("#6B8A99")))
        return item