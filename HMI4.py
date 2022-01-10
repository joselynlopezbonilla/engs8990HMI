import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow, QSplashScreen, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

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

        self.setCentralWidget(widget)
        #self.showFullScreen()
        self.setFixedWidth(1000)
        self.setFixedHeight(550)
        self.setWindowTitle("Reorientation Machine")

    def changeWidget(self, widget):
        self.setCentralWidget(widget)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q: #When Q is pressed, rolling accuracy is 0
            widget = RollingDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            print("Keyboard Q was clicked")
        elif event.key() == Qt.Key_W: #When W is pressed, orienting accuracy is 0
            widget = OrientDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            print("Keyboard W was clicked")
        elif event.key() == Qt.Key_A: #When A is pressed, placing accuracy is 0
            widget = PlacingDisplay(self.changeWidget)
            self.setCentralWidget(widget)        
            print("Keyboard A was clicked")       
        elif event.key() == Qt.Key_Z: #When Z is pressed, full is 1
            widget = FullDisplay(self.changeWidget)
            self.setCentralWidget(widget)
            print("Keyboard Z was clicked")
        elif event.key() == Qt.Key_X: #When X is pressed, emergency stop
            widget = EmerStopDisplay()
            self.setCentralWidget(widget)
            print("Keyboard X was clicked")            
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
        font.setPointSize(20)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea

        self.button1 = QPushButton(self)
        self.button1.setText("Chamfer Side-Up")
        self.button1.move(64,200)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

        self.button2 = QPushButton(self)
        self.button2.setText("Chamfer Side-Down")
        self.button2.move(64,300)
        self.button2.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
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

# Using Keyboard strokes to represent signals coming from the machine
class ErrorDisplay(QFrame):
    def __init__(self,):
        super(ErrorDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Machine in use")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font) 
        textLabel.adjustSize() 

class RollingDisplay(QFrame):
    def __init__(self, callback):
        super(RollingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Part cannot be placed in rolling manner. Please fix.")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font) 
        textLabel.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Error has been cleared.")
        self.button1.move(64,200)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

class OrientDisplay(QFrame):
    def __init__(self, callback):
        super(OrientDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Warning: Part cannot be oriented appropriately.")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font)
        textLabel.adjustSize()

        textLabel1 = QLabel(widget)
        textLabel1.setText("No chamfer can be detected.")
        textLabel1.move(64,120) 
        font = textLabel1.font()
        font.setPointSize(15)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Understood.")
        self.button1.move(64,200)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

class PlacingDisplay(QFrame):
    def __init__(self, callback):
        super(PlacingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Pick and place subsystem cannot place part onto tray")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font)
        textLabel.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Error has been cleared.")
        self.button1.move(64,200)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

class FullDisplay(QFrame):
    def __init__(self, callback):
        super(FullDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Finish: Pick and place subsystem has loaded full tray.")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font)
        textLabel.adjustSize()

        textLabel1 = QLabel(widget)
        textLabel1.setText("Please load empty tray.")
        textLabel1.move(64,120) 
        font = textLabel1.font()
        font.setPointSize(15)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("New empty tray loaded")
        self.button1.move(64,200)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 22px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

class EmerStopDisplay(QFrame):
    def __init__(self):
        super(EmerStopDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Emergency Stop")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(15)
        textLabel.setFont(font)
        textLabel.adjustSize()

if __name__ == '__main__':
    run_app()