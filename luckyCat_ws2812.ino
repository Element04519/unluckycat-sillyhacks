#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(2, 13);

int cat_state  = 0;
bool led_state = false;
long timer = millis();

void setup() {
  Serial.begin(115200);
  pixels.begin();
  pixels.show();

}

void loop() {
  while (Serial.available() > 0) {
    switch (Serial.parseInt()){
      case 0:
        pixels.fill(pixels.Color(0, 0, 0), 0);
        break;
      case 1:
        pixels.fill(pixels.Color(0, 255, 0), 0);
        break;
      case 2:
        pixels.fill(pixels.Color(255, 0, 0), 0);
        break;
      case 3:
        cat_state = 3;
        break;
      case 4:
        cat_state = 4;
        break;
    }
  }

  if(cat_state == 3 && (millis() - timer) > 300){
    led_state = !led_state;
    pixels.fill(pixels.Color(led_state ? 255 : 0, 0, 0), 0);
    timer = millis();
  }
  if(cat_state == 4){
    pixels.fill(pixels.Color((int)random(0,255), (int)random(0,255), 0), (int)random(0,255));
  }

  pixels.show();
}
