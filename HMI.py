import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow, QSplashScreen, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


# Machine to HMI (To showcase whether an error has occurred) (Hard-coded for now)
# Global variables
start_up_flag = 1
roll_flag = 1
orient_flag = 1
place_flag = 1
load_flag = 1
full = 0

class Pages:
    MAIN = 1
    IN_USE = 2
    DONE = 3

def run_app():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    time.sleep(1) # fake ready signal after 1 secs
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
        widget = MainPage(self.changeWidget)

        self.setCentralWidget(widget)
        self.showFullScreen()
        self.setWindowTitle("Reorientation Machine")

    def changeWidget(self, widget):
        self.setCentralWidget(widget)

class SplashScreen():

    def __init__(self):
        # super(SplashScreen,self).__init__()
        pixmap = QPixmap("./rob.jpg")
        self.splash = QSplashScreen(pixmap)
        self.splash.show()

    def finish(self, window):
        self.splash.finish(window)


class MainPage(QFrame):
    def __init__(self, callback):
        super(MainPage,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Start Up Completed")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(20)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea

        self.button1 = QPushButton(self)
        self.button1.setText("Chamfer Side-Up")
        self.button1.move(64,200)
        self.button1.clicked.connect(self.button1_clicked)

        self.button2 = QPushButton(self)
        self.button2.setText("Chamfer Side-Down")
        self.button2.move(64,300)
        self.button2.clicked.connect(self.button2_clicked)

        # page = ErrorDisplay(self.button1, self.button2)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)
        print("Button 1 clicked")
        chamfer = 1 # Chamfer side up

    def button2_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)
        print("Button 2 clicked")
        chamfer = 2 # Chamfer side down


class ErrorDisplay(QFrame):
    def __init__(self):
        super(ErrorDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Machine in use")
        textLabel.move(64,85)
# #         if start_up_flag == 1 and roll_flag == 1 and orient_flag == 1 and place_flag == 1 and load_flag == 1 and full != 1:
# #             # Everything is normal
# #             textLabel.setText("Machine in Use")


if __name__ == '__main__':
    run_app()