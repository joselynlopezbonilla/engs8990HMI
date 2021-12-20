import sys
import time
from PyQt5.QtWidgets import QApplication
from pages import STATES, ReorientationApp, SplashScreen, MainPage, ErrorDisplay
from PyQt5.QtCore import QTimer, QThread


STATE = None

# Machine to HMI (To showcase whether an error has occurred) (Hard-coded for now)
# Global variables
start_up_flag = 1
roll_flag = 1
orient_flag = 1
place_flag = 1
load_flag = 1
full = 0

class AThread(QThread):
    def run(self):
        main_page_stopper = 0
        while True:
            print("coom")
            if STATE == STATES.MAIN:
                if main_page_stopper == 0:
                    w = ReorientationApp()
                    w.show()
                    splash.finish(w)
                    main_page_stopper = 1
                # if start_up_flag == 1 and roll_flag == 1 and orient_flag == 1 and place_flag == 1 and load_flag == 1 and full != 1::
                #     STATE = STATES.IN_USE
                # elif full == 1:
                #     STATE = STATES.DONE   
            elif STATE == STATES.IN_USE:
                widget = ErrorDisplay()
            elif STATE == STATES.DONE:
                pass
            time.sleep(1)

def run_app():
    global STATE, start_up_flag, roll_flag, orient_flag, place_flag, load_flag, full
    app = QApplication(sys.argv)
    splash = SplashScreen()
    startSuccess = splash.startUp()
    if startSuccess == True: STATE = STATES.MAIN
    else: exit(10)
    print('wahoo')
    thread = AThread()
    thread.start()
    # app.exec()

if __name__ == '__main__':
    
    run_app()