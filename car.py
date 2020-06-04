# import curses and GPIO
import curses
import os  # added so we can shut down OK
import time  # import time module

import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
l1 = 7
l2 = 11
l3 = 13
l4 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            if char == ord('S'): # Added for shutdown on capital S
                os.system ('sudo shutdown now') # shutdown right now!
            elif char == curses.KEY_UP:
                GPIO.output(l1,False)
                GPIO.output(l2,True)
                GPIO.output(l3,False)
                GPIO.output(l4,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(l1,True)
                GPIO.output(l2,False)
                GPIO.output(l3,True)
                GPIO.output(l4,False)
            elif char == curses.KEY_LEFT:
                GPIO.output(l1,True)
                GPIO.output(l2,False)
                GPIO.output(l3,False)
                GPIO.output(l4,True)
            elif char == curses.KEY_RIGHT:
                GPIO.output(l1,False)
                GPIO.output(l2,True)
                GPIO.output(l3,True)
                GPIO.output(l4,False)
            elif char == 10:
                GPIO.output(l1,False)
                GPIO.output(l2,False)
                GPIO.output(l3,False)
                GPIO.output(l4,False)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
