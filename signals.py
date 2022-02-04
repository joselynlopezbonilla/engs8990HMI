import gpiod
import time

chip1=gpiod.Chip('gpiochip1')
chip3=gpiod.Chip('gpiochip3')
chip4=gpiod.Chip('gpiochip4')

line_test=chip1.get_lines([ 20 ])


line_test.request(consumer='LED', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 0 ])



while True:
    line_test.set_values([ 1 ])
    time.sleep(1)
    line_test.set_values([ 0 ])
    time.sleep(1)
