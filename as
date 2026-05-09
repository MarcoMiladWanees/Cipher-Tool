[1mdiff --git a/utils/UI.py b/utils/UI.py[m
[1mindex bf9bcae..1926df7 100644[m
[1m--- a/utils/UI.py[m
[1m+++ b/utils/UI.py[m
[36m@@ -1,10 +1,12 @@[m
[31m-from PyQt5.QtCore import Qt[m
[31m-from PyQt5.QtGui import QIcon[m
[31m-from PyQt5.QtWidgets import (QMainWindow, QSplitter, QTreeWidget, QStackedWidget, QTreeWidgetItem)[m
[31m-[m
[31m-from constants import resource_path[m
[31m-from registry import CLASSICAL_REGISTRY, PAGES_DIC[m
[32m+[m[32mfrom PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QSize[m
[32m+[m[32mfrom PyQt5.QtGui import QIcon, QFont, QBrush, QColor, QKeySequence, QPainter[m
[32m+[m[32mfrom PyQt5.QtWidgets import (QMainWindow, QTreeWidget, QStackedWidget, QTreeWidgetItem, QPushButton,[m
[32m+[m[32m                             QShortcut, QWidget, QHBoxLayout)[m
 [m
[32m+[m[32mfrom pages.welcome_page import WelcomePage[m
[32m+[m[32mfrom utils.constants import resource_path[m
[32m+[m[32mfrom utils.registry import CLASSICAL_REGISTRY, PAGES_DIC[m
[32m+[m[32mfrom utils.constants import UICONSTANTS[m
 [m
 class MainWindow(QMainWindow):[m
     def __init__(self):[m
[36m@@ -12,7 +14,6 @@[m [mclass MainWindow(QMainWindow):[m
 [m
         # Initializing the UI[m
         self.initUI()[m
[31m-        self.side_bar.itemClicked.connect(self.on_side_bar_clicked)[m
 [m
     def initUI(self):[m
         #Window setup[m
[36m@@ -21,49 +22,155 @@[m [mclass MainWindow(QMainWindow):[m
         self.resize(1200, 750)[m
         self.setMinimumSize(1000, 650)[m
 [m
[32m+[m[32m        #icons[m
[32m+[m[32m        self.icon_menu = QIcon(resource_path("assets/menu.svg"))[m
[32m+[m[32m        self.icon_chevron = QIcon(resource_path("assets/chevron-right.svg"))[m
[32m+[m
         #Defining everything[m
[31m-        self.main_widget   = QSplitter()[m
[31m-        self.side_bar      = QTreeWidget()[m
[31m-        self.side_bar.setHeaderHidden(True)[m
[31m-        self.side_bar.setMinimumWidth(350)[m
[31m-        self.side_bar.setMaximumWidth(400)[m
[31m-        self.side_bar.setColumnCount(1)[m
[31m-        self.stacked_pages = QStackedWidget()[m
[32m+[m[32m        self.main_widget   = QWidget()[m
[32m+[m[32m        self.main_layout = QHBoxLayout()[m
[32m+[m[32m        self.main_layout.setContentsMargins(0, 0, 0, 0)[m
[32m+[m[32m        self.main_layout.setSpacing(0)[m
[32m+[m[32m        self.main_widget.setLayout(self.main_layout)[m
[32m+[m
[32m+[m[32m        #defining the toggle button[m
[32m+[m
[32m+[m[32m        self.toggle_button = QPushButton("x",self)[m
[32m+[m[32m        self.toggle_button.setIcon(self.icon_chevron)[m
[32m+[m[32m        self.toggle_button.setIconSize(QSize(20, 20))[m
[32m+[m[32m        self.toggle_button.setText("")[m
[32m+[m[32m        self.toggle_button.setObjectName("toggleButton")[m
[32m+[m[32m        # toggle button[m
[32m+[m[32m        self.toggle_button.setFixedSize(50, 50)[m
[32m+[m[32m        self.toggle_button.move(UICONSTANTS.TOGGLE_X_COLLAPSED, UICONSTANTS.TOGGLE_Y)[m
[32m+[m[32m        self.toggle_button.raise_()[m
[32m+[m[32m        self.toggle_button.clicked.connect(self.on_toggle_clicked)[m
[32m+[m
[32m+[m[32m        self.side_bar_button_shortcut = QShortcut(QKeySequence("Ctrl+S"), self) #defining the button shortcut[m
[32m+[m
[32m+[m[32m        # items' font[m
[32m+[m[32m        self.sidebar_font = QFont()[m
[32m+[m[32m        self.sidebar_font.setWeight(450)[m
[32m+[m[32m        self.sidebar_font.setPointSize(11)[m
[32m+[m[32m        self.sidebar_font.setFamily("Segoe UI")[m
[32m+[m
[32m+[m[32m        self.side_bar      = QTreeWidget() #defining the sidebar[m
[32m+[m[32m        self.side_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)[m
[32m+[m[32m        self.side_bar_collapsed = True[m
[32m+[m
[32m+[m[32m        self.side_bar.setIndentation(0) #setting up the indentation[m
[32m+[m[32m        self.side_bar.setHeaderHidden(True) # hiding the header[m
[32m+[m
[32m+[m[32m        # Lock sidebar to a fixed width using equal min/max.[m
[32m+[m[32m        # Both must be animated together (see sidebar_animation + sidebar_min_animation)[m
[32m+[m[32m        # so the widget can collapse without the layout fighting back.[m
[32m+[m[32m        self.side_bar.setMinimumWidth(0) #sidebar's min width[m
[32m+[m[32m        self.side_bar.setMaximumWidth(0) #sidebar's max width[m
[32m+[m[32m        self.side_bar.setColumnCount(1) #setting up the column count[m
[32m+[m[32m        self.side_bar.setFont(self.sidebar_font) #setting up the font[m
[32m+[m
[32m+[m[32m        # sidebar animation[m
[32m+[m[32m        self.sidebar_animation = QPropertyAnimation(self.side_bar, b"maximumWidth")[m
[32m+[m[32m        self.sidebar_animation.setDuration(UICONSTANTS.ANIMATION_TIME)[m
[32m+[m[32m        self.sidebar_animation.setEasingCurve(QEasingCurve.InOutCubic)[m
[32m+[m
[32m+[m[32m        self.sidebar_min_animation = QPropertyAnimation(self.side_bar, b"minimumWidth")[m
[32m+[m[32m        self.sidebar_min_animation.setDuration(UICONSTANTS.ANIMATION_TIME)[m
[32m+[m[32m        self.sidebar_min_animation.setEasingCurve(QEasingCurve.InOutCubic)[m
 [m
[32m+[m[32m        # button animation[m
[32m+[m[32m        self.button_animation = QPropertyAnimation(self.toggle_button, b"pos")[m
[32m+[m[32m        self.button_animation.setDuration(UICONSTANTS.ANIMATION_TIME)[m
[32m+[m[32m        self.button_animation.setEasingCurve(QEasingCurve.InOutCubic)[m
[32m+[m
[32m+[m[32m        #pages stack[m
[32m+[m[32m        self.stacked_pages = QStackedWidget()[m
[32m+[m[32m        welcome_page = WelcomePage()[m
[32m+[m[32m        self.stacked_pages.addWidget(welcome_page)[m
         #Adding stuff to the sidebar[m
 [m
         #Adding the Top level Items[m
[31m-        self.classical_ciphers = QTreeWidgetItem(self.side_bar)[m
[31m-        self.classical_ciphers.setText(0,"Classical Ciphers")[m
[31m-        self.modern_ciphers = QTreeWidgetItem(self.side_bar)[m
[31m-        self.modern_ciphers.setText(0,"Modern Ciphers")[m
[32m+[m[32m        self.classical_ciphers = self._make_category_item("Classical")[m
[32m+[m[32m        self.modern_ciphers = self._make_category_item("Modern")[m
 [m
         #Adding the classical ciphers[m
[31m-        for item in CLASSICAL_REGISTRY.keys():[m
[31m-            sub_cat = QTreeWidgetItem(self.classical_ciphers)[m
[31m-            sub_cat.setText(0,item)[m
[31m-            for cipher in CLASSICAL_REGISTRY[item]:[m
[31m-                name, key, PageCLass = cipher[m
[31m-                tree_item = QTreeWidgetItem(sub_cat)[m
[31m-                tree_item.setText(0,name)[m
[31m-                tree_item.setData(0,Qt.UserRole, key)[m
[31m-                page = PageCLass()[m
[31m-                self.stacked_pages.addWidget(page)[m
[31m-                PAGES_DIC[key] = page[m
[32m+[m[32m        for cipher in CLASSICAL_REGISTRY:[m
[32m+[m[32m            name, key, PageClass = cipher[m
[32m+[m[32m            tree_item = QTreeWidgetItem(self.classical_ciphers)[m
[32m+[m[32m            tree_item.setText(0,f"# {name}")[m
[32m+[m[32m            tree_item.setData(0,Qt.UserRole, key)[m
[32m+[m[32m            page = PageClass()[m
[32m+[m[32m            self.stacked_pages.addWidget(page)[m
[32m+[m[32m            PAGES_DIC[key] = page[m
 [m
         #Adding the widgets to the splitter[m
         self.side_bar.expandAll()[m
[31m-        self.main_widget.addWidget(self.side_bar)[m
[31m-        self.main_widget.addWidget(self.stacked_pages)[m
[31m-        self.main_widget.setStretchFactor(0, 1)[m
[31m-        self.main_widget.setStretchFactor(1, 1)[m
[31m-[m
[32m+[m[32m        self.main_layout.addWidget(self.side_bar)[m
[32m+[m[32m        self.main_layout.addWidget(self.stacked_pages)[m
 [m
         #Setting the splitter as the central widget[m
         self.setCentralWidget(self.main_widget)[m
 [m
 [m
[32m+[m[32m        self.side_bar_button_shortcut.activated.connect(self.on_toggle_clicked)[m
[32m+[m[32m        self.side_bar.itemClicked.connect(self.on_side_bar_clicked)[m
[32m+[m[32m        self.sidebar_animation.finished.connect(self.on_sidebar_animation_finished)[m
[32m+[m
[32m+[m
     def on_side_bar_clicked(self, item):[m
         key = item.data(0, Qt.UserRole)[m
         if key:[m
[31m-            self.stacked_pages.setCurrentWidget(PAGES_DIC[key])[m
\ No newline at end of file[m
[32m+[m[32m            self.stacked_pages.setCurrentWidget(PAGES_DIC[key])[m
[32m+[m[32m    def on_toggle_clicked(self):[m
[32m+[m[32m        # Animate min and max in parallel so the widget's actual width[m
[32m+[m[32m        # (always clamped to min ≤ width ≤ max) follows smoothly.[m
[32m+[m[32m        if not self.toggle_button.isEnabled():[m
[32m+[m[32m            return[m
[32m+[m[32m        self.toggle_button.setEnabled(False)[m
[32m+[m[32m        if self.side_bar_collapsed:[m
[32m+[m[32m            start, end = 0, UICONSTANTS.SIDEBAR_WIDTH[m
[32m+[m[32m            b_start, b_end =  UICONSTANTS.TOGGLE_POS_COLLAPSED, UICONSTANTS.TOGGLE_POS_EXPANDED[m
[32m+[m[32m        else:[m
[32m+[m[32m            start, end = UICONSTANTS.SIDEBAR_WIDTH, 0[m
[32m+[m[32m            b_start, b_end =  UICONSTANTS.TOGGLE_POS_EXPANDED, UICONSTANTS.TOGGLE_POS_COLLAPSED[m
[32m+[m
[32m+[m[32m        self.sidebar_animation.setStartValue(start)[m
[32m+[m[32m        self.sidebar_animation.setEndValue(end)[m
[32m+[m[32m        self.sidebar_min_animation.setStartValue(start)[m
[32m+[m[32m        self.sidebar_min_animation.setEndValue(end)[m
[32m+[m[32m        self.button_animation.setStartValue(b_start)[m
[32m+[m[32m        self.button_animation.setEndValue(b_end)[m
[32m+[m
[32m+[m[32m        self.button_animation.start()[m
[32m+[m[32m        self.sidebar_animation.start()[m
[32m+[m[32m        self.sidebar_min_animation.start()[m
[32m+[m
[32m+[m[32m        self.side_bar_collapsed = not self.side_bar_collapsed[m
[32m+[m[32m        if self.side_bar_collapsed:[m
[32m+[m[32m            self.toggle_button.setIcon(self.icon_chevron)[m
[32m+[m[32m        else:[m
[32m+[m[32m            self.toggle_button.setIcon(self.icon_menu)[m
[32m+[m
[32m+[m[32m    def on_sidebar_animation_finished(self):[m
[32m+[m[32m        self.toggle_button.setEnabled(True)[m
[32m+[m
[32m+[m[32m    def resizeEvent(self, event):[m
[32m+[m[32m        if self.side_bar_collapsed:[m
[32m+[m[32m            self.toggle_button.move(8, UICONSTANTS.TOGGLE_Y)[m
[32m+[m[32m        else:[m
[32m+[m[32m            self.toggle_button.move(UICONSTANTS.TOGGLE_X_EXPANDED, UICONSTANTS.TOGGLE_Y)[m
[32m+[m[32m        super().resizeEvent(event)[m
[32m+[m
[32m+[m
[32m+[m[32m    def _make_category_item(self, text):[m
[32m+[m[32m        top_level_font = QFont()[m
[32m+[m[32m        top_level_font.setPointSize(9)[m
[32m+[m[32m        top_level_font.setFamily("Segoe UI")[m
[32m+[m[32m        top_level_font.setWeight(300)[m
[32m+[m[32m        top_level_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)[m
[32m+[m[32m        item = QTreeWidgetItem(self.side_bar)[m
[32m+[m[32m        item.setText(0, text)[m
[32m+[m[32m        item.setFlags(item.flags() & ~Qt.ItemIsSelectable )[m
[32m+[m[32m        item.setFont(0, top_level_font)[m
[32m+[m[32m        item.setForeground(0, QBrush(QColor("#6B8A99")))[m
[32m+[m[32m        return item[m
\ No newline at end of file[m
