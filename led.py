import RPi.GPIO as GPIO ## Import GPIO library
import time 


def bbb(x):
    
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT) 

    try:
        numb = int(x)
        delayv = 0.5
        delayf = 0.2
        for num in range(0,x):
            GPIO.output(7, True) ## Turn on GPIO pin 7
            time.sleep(delayv)
            GPIO.output(7, False) ## Turn on GPIO pin 7
            time.sleep(delayf)

    except ValueError:
           print("That's not an int!")
           return False

    

    return True
