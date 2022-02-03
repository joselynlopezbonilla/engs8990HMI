import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow, QSplashScreen, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt
from Status import Status

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
        widget = MainPage(self.changeWidget)
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")

        self.setCentralWidget(widget)
        self.showFullScreen()
        self.setWindowTitle("Reorientation Machine")

    def changeWidget(self, widget):
        self.setCentralWidget(widget)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q: #When Q is pressed, rolling accuracy is 0
            widget = RollingDisplay(self.changeWidget)
            widget.setStyleSheet(" background-color: rgb(171, 0, 0);")
            self.setCentralWidget(widget)
            print("Keyboard Q was clicked")
        elif event.key() == Qt.Key_W: #When W is pressed, orienting accuracy is 0
            # Detection warning
            # No chamfer detected
            widget = OrientDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            widget.setStyleSheet("background-color: rgb(171, 94, 0);")
            print("Keyboard W was clicked")
        elif event.key() == Qt.Key_A: #When A is pressed, placing accuracy is 0
            # Camera Failure
            # Status.CAMERA_FATAL
            widget = PlacingDisplay(self.changeWidget)
            self.setCentralWidget(widget)  
            widget.setStyleSheet("background-color: rgb(171, 0, 0);")      
            print("Keyboard A was clicked")       
        elif event.key() == Qt.Key_Z: #When Z is pressed, full is 1
            widget = FullDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            widget.setStyleSheet("background-color: rgb(0, 0, 148);") 
            print("Keyboard Z was clicked")
        elif event.key() == Qt.Key_X: #When X is pressed, emergency stop
            widget = EmerStopDisplay()
            self.setCentralWidget(widget)
            widget.setStyleSheet(" background-color: rgb(171, 0, 0);")
            print("Keyboard X was clicked")   
        elif event.key() == Qt.Key_S: #When W is pressed, orienting accuracy is 0
            # Detection warning
            # No part detected
            widget = OrientPartDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            widget.setStyleSheet("background-color: rgb(171, 94, 0);")
            print("Keyboard W was clicked")
        elif event.key() == Qt.Key_C: #When W is pressed, orienting accuracy is 0
            # Pause
            widget = PauseDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            widget.setStyleSheet("background-color: rgb(171, 94, 0);")
            print("Keyboard W was clicked")           
        else: 
            self.proceed()
        event.accept()

    def proceed(self):
        print ("Call Enter Key")

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
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea
        widget.setStyleSheet("color: rgb(255, 255, 255);")
        print(repr(Status.READY))
        
        self.button1 = QPushButton(self)
        self.button1.setText("Chamfer Side-Up")
        self.button1.move(50,300)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

        self.button2 = QPushButton(self)
        self.button2.setText("Chamfer Side-Down")
        self.button2.move(500,300)
        self.button2.resize(100, 300)
        self.button2.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button2.clicked.connect(self.button2_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        print("Button 1 clicked")
        chamfer = 1 # Chamfer side up
        print(repr(Status.SET))

    def button2_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        print("Button 2 clicked")
        chamfer = 2 # Chamfer side down
        print(repr(Status.SET))

# Using Keyboard strokes to represent signals coming from the machine
class ErrorDisplay(QFrame):
    def __init__(self):
        super(ErrorDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Machine in use")
        textLabel.move(150,300)
        font = textLabel.font()
        font.setPointSize(70)
        textLabel.setFont(font) 
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")
        print(repr(Status.IN_USE))

class RollingDisplay(QFrame):
    def __init__(self, callback):
        super(RollingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Part cannot be placed in")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font) 
        textLabel.adjustSize()
        widget.setStyleSheet(" color: rgb(250, 250, 250);")

        textLabel1 = QLabel(widget)
        textLabel1.setText("rolling manner. Please fix.")
        textLabel1.move(64,160) 
        font = textLabel1.font()
        font.setPointSize(50)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Error cleared")
        self.button1.move(300,300)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)

class OrientDisplay(QFrame):
    def __init__(self, callback):
        super(OrientDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Warning: Part cannot be")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")

        textLabel1 = QLabel(widget)
        textLabel1.setText("oriented appropriately.")
        textLabel1.move(64,160) 
        font = textLabel1.font()
        font.setPointSize(50)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        textLabel2 = QLabel(widget)
        textLabel2.setText("No chamfer detected.")
        textLabel2.move(64,240) 
        font = textLabel2.font()
        font.setPointSize(50)
        textLabel2.setFont(font)
        textLabel2.adjustSize()
        print(repr(Status.INVALID_CHAMFER))

        self.button1 = QPushButton(self)
        self.button1.setText("Understood")
        self.button1.move(300,350)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)

class PlacingDisplay(QFrame):
    def __init__(self, callback):
        super(PlacingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Part cannot be")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")

        textLabel1 = QLabel(widget)
        textLabel1.setText("placed onto tray.")
        textLabel1.move(64,150) 
        font = textLabel1.font()
        font.setPointSize(50)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        textLabel2 = QLabel(widget)
        textLabel2.setText("Camera malfunction.")
        textLabel2.move(64,230) 
        font = textLabel2.font()
        font.setPointSize(50)
        textLabel2.setFont(font)
        textLabel2.adjustSize()
        print(repr(Status.CAMERA_FATAL))

        self.button1 = QPushButton(self)
        self.button1.setText("Error cleared")
        self.button1.move(300,350)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)

class FullDisplay(QFrame):
    def __init__(self, callback):
        super(FullDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Finish: Loading tray is full.")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")
        print(repr(Status.TRAY_FULL))

        textLabel2 = QLabel(widget)
        textLabel2.setText("Please load an empty tray.")
        textLabel2.move(64,160) 
        font = textLabel2.font()
        font.setPointSize(50)
        textLabel2.setFont(font)
        textLabel2.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("New tray loaded")
        self.button1.move(300,300)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)


class EmerStopDisplay(QFrame):
    def __init__(self):
        super(EmerStopDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Emergency Stop")
        textLabel.move(150,300)
        font = textLabel.font()
        font.setPointSize(70)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")
        print(repr(Status.EMERGENCY))

class OrientPartDisplay(QFrame):
    def __init__(self, callback):
        super(OrientPartDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Warning: Part cannot be")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")

        textLabel1 = QLabel(widget)
        textLabel1.setText("oriented appropriately.")
        textLabel1.move(64,160) 
        font = textLabel1.font()
        font.setPointSize(50)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        textLabel2 = QLabel(widget)
        textLabel2.setText("No part detected.")
        textLabel2.move(64,240) 
        font = textLabel2.font()
        font.setPointSize(50)
        textLabel2.setFont(font)
        textLabel2.adjustSize()
        print(repr(Status.IVALID_PART))

        self.button1 = QPushButton(self)
        self.button1.setText("Understood")
        self.button1.move(300,350)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)
    
class PauseDisplay(QFrame):
    def __init__(self, callback):
        super(PauseDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Pause")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(50)
        textLabel.setFont(font)
        textLabel.adjustSize()
        widget.setStyleSheet("color: rgb(250, 250, 250);")
        print(repr(Status.PAUSE))

        self.button1 = QPushButton(self)
        self.button1.setText("Resume")
        self.button1.move(300,350)
        self.button1.resize(100, 300)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 30px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        print(repr(Status.FIXED))
        widget.setStyleSheet(" background-color: rgb(0, 110, 0);")
        self.callback(widget)

if __name__ == '__main__':
    run_app()
