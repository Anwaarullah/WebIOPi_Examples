# WebIOPi_Examples
WebIOPi (http://webiopi.trouch.com/, an IoT framework for Raspberry Pi) Sample Examples and Writeup

The Example_1 folder contains an html and python file that initializes two GPIOs and toggles them.
The Example_2 folder also contains another set of html and python file that show the process of creating a custom macro/function in Python can be called from within the Webpage.

Please make note that WebIOPi doesn't work out of the box for Pi 2 yet. 

Patch for Pi 2/3: https://github.com/doublebind/raspi

However, using info found from this link https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=98981  , WebIOPi can be hacked around to run on Pi 2:

This method from the above link worked for me:

1.python/native/cpuinfo.c,change "BCM2708" to "BCM2709";

2.python/native/gpio.c, change "#define BCM2708_PERI_BASE 0x20000000" to "#define BCM2708_PERI_BASE 0x3f000000";

3.run setup.sh again.

