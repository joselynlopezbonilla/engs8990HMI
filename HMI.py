import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow, QSplashScreen, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

class Pages:
    MAIN = 1
    IN_USE = 2
    DONE = 3

def run_app():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    time.sleep(3) # fake ready signal after 3 secs
    w = ReorientationApp()
    w.show()
    splash.finish(w)
    app.exec()


class ReorientationApp(QMainWindow):
    def __init__(self):
        super(ReorientationApp, self).__init__()

        self.setWindowTitle("My App")

        # widget = QLabel("Hello")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        widget = MainPage()

        self.setCentralWidget(widget)
        self.showFullScreen()
        self.setWindowTitle("Reorientation Machine")

class SplashScreen():

    def __init__(self):
        # super(SplashScreen,self).__init__()
        pixmap = QPixmap("./rob.jpg")
        self.splash = QSplashScreen(pixmap)
        self.splash.show()

    def finish(self, window):
        self.splash.finish(window)


class MainPage(QFrame):
    def __init__(self):
        super(MainPage,self).__init__()

        widget = QWidget()
        textLabel = QLabel(widget)
        textLabel.setText("Start Up Completed")
        textLabel.move(110,85)

        button1 = QPushButton(self)
        button1.setText("Chamfer Side-Up")
        button1.move(64,32)
        button1.clicked.connect(button1_clicked)

        button2 = QPushButton(self)
        button2.setText("Chamfer Side-Down")
        button2.move(64,64)
        button2.clicked.connect(button2_clicked)

def button1_clicked():
   print("Button 1 clicked")

def button2_clicked():
   print("Button 2 clicked")



if __name__ == '__main__':
    run_app()