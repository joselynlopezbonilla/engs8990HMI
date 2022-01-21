import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow, QSplashScreen, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPalette
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
    def __init__(self, callback, color=QColor("green")):
        super(MainPage,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Start Up Completed")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font)
        textLabel.adjustSize() #seems like a bad idea
        #widget.setStyleSheet(" background-color: rgb(43, 135, 42);")
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        #pal.setColor(QPalette.Base, color)
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)
        

        self.button1 = QPushButton(self)
        self.button1.setText("Chamfer Side-Up")
        self.button1.move(50,200)
        self.button1.resize(100, 100)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

        self.button2 = QPushButton(self)
        self.button2.setText("Chamfer Side-Down")
        self.button2.move(50,350)
        self.button2.resize(100, 100)
        self.button2.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
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
    def __init__(self, color=QColor("green")):
        super(ErrorDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Machine in use")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font) 
        textLabel.adjustSize()
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class RollingDisplay(QFrame):
    def __init__(self, callback, color=QColor("red")):
        super(RollingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Part cannot be placed in")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font) 
        textLabel.adjustSize()
        self.setColor(color) # Try to figure out which one looks better
        #widget.setStyleSheet(" background-color: rgb(248, 42, 42);")

        textLabel1 = QLabel(widget)
        textLabel1.setText("rolling manner. Please fix.")
        textLabel1.move(64,150) 
        font = textLabel1.font()
        font.setPointSize(30)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Error has been cleared.")
        self.button1.move(50,300)
        self.button1.resize(100, 100)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class OrientDisplay(QFrame):
    def __init__(self, callback, color=QColor("orange")):
        super(OrientDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Warning: Part cannot be oriented")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font)
        textLabel.adjustSize()
        self.setColor(color)

        textLabel1 = QLabel(widget)
        textLabel1.setText("appropriately.")
        textLabel1.move(64,150) 
        font = textLabel1.font()
        font.setPointSize(30)
        textLabel1.setFont(font)
        textLabel1.adjustSize()
        self.setColor(color)

        textLabel2 = QLabel(widget)
        textLabel2.setText("No chamfer can be detected.")
        textLabel2.move(64,215) 
        font = textLabel2.font()
        font.setPointSize(30)
        textLabel2.setFont(font)
        textLabel2.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Understood.")
        self.button1.move(50,350)
        self.button1.resize(100, 100)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class PlacingDisplay(QFrame):
    def __init__(self, callback, color=QColor("red")):
        super(PlacingDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Error: Pick and place subsystem.")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font)
        textLabel.adjustSize()
        self.setColor(color)

        textLabel1 = QLabel(widget)
        textLabel1.setText("cannot place part onto tray.")
        textLabel1.move(64,150) 
        font = textLabel1.font()
        font.setPointSize(30)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("Error has been cleared.")
        self.button1.move(50,350)
        self.button1.resize(100, 100)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class FullDisplay(QFrame):
    def __init__(self, callback, color=QColor("blue")):
        super(FullDisplay,self).__init__()
        self.callback = callback
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Finish: Pick and place subsystem")
        textLabel.move(64,85) 
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font)
        textLabel.adjustSize()
        self.setColor(color)

        textLabel1 = QLabel(widget)
        textLabel1.setText("loaded full tray.")
        textLabel1.move(64,150) 
        font = textLabel1.font()
        font.setPointSize(30)
        textLabel1.setFont(font)
        textLabel1.adjustSize()

        textLabel2 = QLabel(widget)
        textLabel2.setText("Please load empty tray.")
        textLabel2.move(64,215) 
        font = textLabel2.font()
        font.setPointSize(30)
        textLabel2.setFont(font)
        textLabel2.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText("New empty tray loaded")
        self.button1.move(50,300)
        self.button1.resize(100, 100)
        self.button1.setStyleSheet(" background-color: rgb(171, 171, 171); \
        border-style: outset; \
        border-width: 2px;\
        border-radius: 10px; \
        border-color: beige; \
        font: bold 50px; \
        min-width: 10em; \
        padding: 6px;")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        widget = ErrorDisplay()
        self.callback(widget)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class EmerStopDisplay(QFrame):
    def __init__(self, color=QColor("red")):
        super(EmerStopDisplay,self).__init__()
        widget = QWidget(self)
        textLabel = QLabel(widget)
        textLabel.setText("Emergency Stop")
        textLabel.move(64,85)
        font = textLabel.font()
        font.setPointSize(30)
        textLabel.setFont(font)
        textLabel.adjustSize()
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

if __name__ == '__main__':
    run_app()