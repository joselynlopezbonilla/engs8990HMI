import sys
import time
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QToolButton,
    QMainWindow,
    QSplashScreen,
    QFrame,
    QGridLayout,
)
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt

ChamferMode = 0

def run_app():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    time.sleep(1) # fake ready signal after 1 secs
    w = ReorientationApp()
    w.show()
    splash.finish(w)
    app.exec()

class SplashScreen():
    def __init__(self):
        # super(SplashScreen,self).__init__()
        pixmap = QPixmap("./rob.jpg")
        self.splash = QSplashScreen(pixmap)
        self.splash.show()

    def finish(self, window):
        self.splash.finish(window) 

class ReorientationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        self.showFullScreen()
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.addWidget(MainPage(self.changeWidget), 0, 0, 3, 1)
        layout.addWidget(QPushButton("Picture"), 0, 1)
        layout.addWidget(ChamfUpPushButton(), 4, 0)
        layout.addWidget(ChamfDownPushButton(), 4, 1)
        layout.addWidget(QPushButton("Clear Errors"), 2, 1)
        # Set the layout on the application's window
        self.setLayout(layout)

    def changeWidget(self, widget):
        self.setCentralWidget(widget)

class MainPage(QFrame):
    def __init__(self, callback):
        super(MainPage,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Start Up Completed")
        # textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(20)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea  

        self.button1 = QPushButton(self)
        self.button1.setText("Next")
        self.button1.move(64,200)
        self.button1.clicked.connect(self.button_clicked)

    def button_clicked(self):
        widget = ModeDisplay()
        self.callback(widget)

class ModeDisplay(QFrame):
    def __init__(self,):
        super(ModeDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Please select mode")
        # textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(20)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea     

class ChamfUpPushButton(QPushButton):
    def __init__(self):
        super(ChamfUpPushButton,self).__init__()
        self.setGeometry(400,400,300,260)
        self.setText("Chamfer Side-Up")
        self.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        global ChamferMode
        if ChamferMode == 0:
            self.setStyleSheet("background-color: rgb(73, 153, 79); \
            border-width: 2px;\
            border-radius: 10px; \
            border-color: beige; \
            font: bold 22px; \
            min-width: 10em; \
            padding: 6px;")
            print("Button 1 clicked")
            ChamferMode = 1 # Chamfer side up

class ChamfDownPushButton(QPushButton):
    def __init__(self):
        super(ChamfDownPushButton,self).__init__()
        self.setGeometry(400,400,300,260)
        self.setText("Chamfer Side-Down")
        self.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        global ChamferMode
        if ChamferMode == 0:
            self.setStyleSheet("background-color: rgb(73, 153, 79); \
            border-width: 2px;\
            border-radius: 10px; \
            border-color: beige; \
            font: bold 22px; \
            min-width: 10em; \
            padding: 6px;")
            print("Button 1 clicked")
            ChamferMode = 2 # Chamfer side down
     
if __name__ == "__main__":

    run_app()