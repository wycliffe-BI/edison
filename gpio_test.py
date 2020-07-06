# GPIO test for the edison, simple code for turing digital pins on and off.

# To interface with digital/analog pins on the edison, we use a library called MRAA which can act as the equivelant of analogRead(pin), as if we are programming
# with the Arduino IDE.

# !/usr/bin/python

print("Hello world")

import mraa  # For accessing the GPIO
from time import sleep  # For sleeping between blinks

led_pin = 5  # we are using D5 pin

blinkLed = mraa.Gpio(led_pin)  # We make an object, which is the led that we will blink.

blinkLed.dir(
    mraa.DIR_OUT)  # Set the direction as output (i.e) this object has a property where we allocate the INPUT or OUTPUT

ledState = False  # LED is off to begin with

blinkLed.write(0)  # Write the blinking led object to low.

# One infinite loop coming up
while True:
    if ledState == False:
        # LED is off, turn it on
        blinkLed.write(1)
        ledState = True  # LED is on
    else:
        blinkLed.write(0)
        ledState = False

    print("LED is on? \nAns: %s" % (ledState))

    # Wait for some time
    sleep(1)
