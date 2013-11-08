Minecraft-Pi-StepLights
=======================

Built and coded on the floor of Minecon 2013, in Orlando, FL. 
Credit for build goes to:
Theodore Wahrburg (python, Arduino DE, hardware)
IanStarGem (mcpe api, python) 
John Cope (Jack-o-Lantern design)
Mac Rutan (concept)


Simple Instructions:

Connect Neopixel lights (http://www.adafruit.com/products/1138) to pin 6 of Arduino.
Change Arduino sketch to reflect number of Neopixel lights connected.
Flash Arduino with Arduino sketch.
Download and place mineLight.py in the python directory of your Minecraft Pi edition API folder on your Raspberry Pi.
Change Python script to include the serial port of connected Arduino and save script.
Start Minecraft, and enter game world.
Execute Python script "mineLight.py"
If all successful, the Neopixel lights should begin changing color to current block being stood on by player.

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
  

 
Minecraft hint:
In Minecraft, type "E" to enter your inventory, 
add some wool blocks to your Hot Bar and hit "esc" to return to the game.
place some colorful blocks to walk on and go! Check out your LEDs!

Special Thanks to:
Raspberry Pi Foundation
Mojang
FamiLAB
Adafruit
GadgetCat




 
 
 


