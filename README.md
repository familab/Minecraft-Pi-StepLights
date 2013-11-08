Minecraft-Pi-StepLights
=======================

Built and coded on the floor of Minecon 2013, in Orlando, FL. Credit for build goes to Theodore Wahrburg, Eli Rutan, and Mac Rutan.
For use with MCPIPY (https://github.com/brooksc/mcpipy)

Simple Instructions:

Connect Neopixel lights (http://www.adafruit.com/products/1138) to pin 6 of Arduino.
Change Arduino sketch to reflect number of Neopixel lights connected.
Flash Arduino with Arduino sketch.
Change Python script to serial port of connected Arduino.
Start Minecraft, and enter game world.
Execute Python script. If all successful, the Neopixel lights should begin changing color to current block being stood on by player.


Arduino communications is done with 9600 Baud Speed
Connected Neopixel lights will change color immediately following being sent a valid character
 R - Red
 G - Green
 B - Blue
 P - Purple
 W - White
 Y - Yellow
 O - Orange
 D - Gray
 U - Brown
 M - All LEDs off
 
 Block color is currently determined by a very long if/else statement of hardcoded colors.

