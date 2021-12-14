import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

class ToolButton(QMainWindow):

    def __init__(self):
        super(ToolButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400,400,300,260)

        self.toolbar = self.addToolBar("toolBar")
        self.statusBar()

        self._detailsbutton = QToolButton()                                     
        self._detailsbutton.setCheckable(True)                                  
        self._detailsbutton.setChecked(False)                                   
        self._detailsbutton.setArrowType(Qt.RightArrow)
        self._detailsbutton.setAutoRaise(True)
        #self._detailsbutton.setIcon(QIcon("test.jpg"))
        self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._detailsbutton.clicked.connect(self.showDetail)
        self.toolbar.addWidget(self._detailsbutton)

    def showDetail(self):
        if self._detailsbutton.isChecked():
            self.statusBar().showMessage("Show Detail....")
        else:
            self.statusBar().showMessage("Close Detail....")

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(400,400,300,260)
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(100,100)

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Start ")
   textLabel.move(110,85)

   button1 = QPushButton(widget)
   button1.setText("Button1")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

def button1_clicked():
   print("Button 1 clicked")

if __name__ == '__main__':
   #window()

   #app = QApplication(sys.argv)
   #ex = PushButton()
   #ex.show()
   #sys.exit(app.exec_()) 

   app = QApplication(sys.argv)
   ex = ToolButton()
   ex.show()
   sys.exit(app.exec_()) 