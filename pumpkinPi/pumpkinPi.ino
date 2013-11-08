#include <Adafruit_NeoPixel.h>

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_RGB     Pixels are wired for RGB bitstream
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ400  400 KHz bitstream (e.g. FLORA pixels)
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(55, 6, NEO_GRB + NEO_KHZ800);
char buffer = 0;
int currentPos = 0;
char color = 0;

void setup() {
  strip.begin();
  Serial.begin(9600);
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  
  while(Serial.available()){
   currentPos = 0;
   buffer = Serial.read();
 
   if (buffer != '\n')
    color = buffer;
   
  }
   
   if (color == 'R' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 255,0,0);
    delay(5);
    strip.show();    
   }
   
   else if (color == 'G' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 0,255,0);
    delay(5);
    strip.show();    
   }
   
   else if (color == 'U' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 139,69,19);
    delay(5);
    strip.show();    
   }
   
   else if (color == 'B' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 0,0,255);
    delay(5);
    strip.show();    
   }   
   
   else if (color == 'P' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 255,0,255);
    delay(5);
    strip.show();    
   }  
   
   else if (color == 'Y' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 255,255,0);
    delay(5);
    strip.show();    
   }     
   
   else if (color == 'O' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 255,100,0);
    delay(5);
    strip.show();    
   }  
   
   else if (color == 'D' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 80,80,80);
    delay(5);
    strip.show();    
   }  
   
   else if (color == 'W' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 255,255,255);
    delay(5);
    strip.show();    
   }  
   
   else if (color == 'M' && currentPos < strip.numPixels()){    
    strip.setPixelColor(currentPos++, 0,0,0);
    delay(5);
    strip.show();    
   } 
   
}
