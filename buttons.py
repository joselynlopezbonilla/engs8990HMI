import gpiod
import time

chip1=gpiod.Chip('gpiochip1')
chip3=gpiod.Chip('gpiochip3')
chip4=gpiod.Chip('gpiochip4')

LED_line=chip1.get_lines([ 7 ]) # Pin 21
button1_line=chip1.get_lines([ 9 ]) # Pin 23
#button2_line=chip1.get_lines([ 21 ])
#button3_line=chip4.get_lines([ 24 ])
#button4_line=chip1.get_lines([ 8 ])
#button5_line=chip1.get_lines([ 7 ])

# Testing
LED_line.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 0 ])
button1_line.request(consumer='button1', type=gpiod.LINE_REQ_DIR_IN)
#button1_line.request_input()
# button1_output=button1_line.request_bulk_rising_edge_events
counter = 0

while True:
    #LED_line.set_values([ 1 ])
    time.sleep(1)
    #LED_line.set_values([ 0 ])

    button1 = button1_line.get_values()
    print(counter, button1)
    #counter = counter + 1
    if (button1[0] == 0):
       LED_line.set_values([ 0 ])
       # time.sleep(.1)

       print("Switch is low", button1)

    elif (button1[0] == 1):
       LED_line.set_values([ 1 ])
       #time.sleep(.1)
       print("SWitch is high", button1)

    counter =  counter + 1

