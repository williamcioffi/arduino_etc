/***************************************************
  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  MIT license, all text above must be included in any redistribution
 ****************************************************/

#include "Adafruit_EPD.h"
#include <Adafruit_GFX.h> // Core graphics library
#include <SdFat.h>
#include <Adafruit_ImageReader_EPD.h>

// non kitten items
// #include "nki.h"

// pinout
#define ECS 5
#define DC 6
#define SRCS 9
#define SDCS 10
#define RST 11
#define BSY 12

// 3 minutes in milliseconds
#define FIVE_MINUTES_MILLIS 300000
#define THREE_MINUTES_MILLIS 180000

// define sd card and image reader
SdFat SD;
Adafruit_ImageReader_EPD reader(SD);

Adafruit_SSD1675 display(250, 122, DC, RST, ECS, SRCS, BSY, &SPI);

// dtb1.bmp
// sjgd.bmp
// gm.bmp
// k.bmp
// j.bmp

void setup(void) {
  if(!SD.begin(SDCS, SD_SCK_MHZ(10))) {
    // fatal error
    while(true);
  }

  display.begin();

  display.clearBuffer();
  reader.drawBMP((char *)"/j.bmp", display, 0, 0);
  display.setCursor(75, 0);
  display.setTextSize(2);
  display.print(F("hello world..."));
  display.display();

  // delay(THREE_MINUTES_MILLIS);

  // display.clearBuffer();
  // reader.drawBMP((char *)"/j.bmp", display, 0, 0);
  // display.display(); 

  
  // delay(THREE_MINUTES_MILLIS);

  // display.clearBuffer();
  // reader.drawBMP((char *)"/gm.bmp", display, 0, 0);
  // display.display();

  
  // delay(THREE_MINUTES_MILLIS);

  // display.clearBuffer();
  // reader.drawBMP((char *)"/k.bmp", display, 0, 0);
  // display.display();

  // delay(THREE_MINUTES_MILLIS);

  // display.clearBuffer();
  // reader.drawBMP((char *)"/j.bmp", display, 0, 0);
  // display.display();
}

void loop() { 
  // rotate through the quotes
  // for(int i = 0; i < NUMBER_OF_NKI; i++) {
  // // display that quote
  // display.setRotation(0);
  // display.clearBuffer();
  // display.setTextWrap(true);
  // display.setCursor(10, 10);
  // display.setTextSize(1);
  // display.print((__FlashStringHelper *)pgm_read_word(&msgs[i]));
  // display.display();

  // // delay for 5 minutes before another refresh
  // delay(FIVE_MINUTES_MILLIS);

  // delay(FIVE_MINUTES_MILLIS); 
  // }
}
