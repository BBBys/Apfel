// Based on sketch here:
// https://github.com/OpenHDZ/Arduino-experimentation
// Adapted for TFT_eSPI library

// Note: a high number of floating point calculations are needed
// for each pixel so rendering will be quite slow.
// For best performance use a Teensy 4.x (600MHz CPU clock).

#include <TFT_eSPI.h> // Hardware-specific library

TFT_eSPI tft = TFT_eSPI(); // Invoke custom library

const uint16_t MAX_ITERATION = 300; // Nombre de couleurs

#define SCREEN_WIDTH tft.width()   //
#define SCREEN_HEIGHT tft.height() // Taille de l'écran

static float zoom = 0.5;

/* Fonction setup */
void setup()
{
  /* Initialise l'écran LCD */
  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  tft.setFreeFont(&FreeMono9pt7b);
}

/* Fonction loop() */
void loop()
{
  /* Dessine la fractale */
  draw_Julia(-0.8, +0.156, zoom);
  tft.fillRect(0, 0, 150, 20, TFT_BLACK);
  tft.setCursor(0, 15);
  tft.setTextColor(TFT_WHITE);
  tft.print(" Zoom = ");
  tft.println(zoom);
  delay(2000);
  zoom *= 1.5;
  if (zoom > 100)
    zoom = 0.5;
}

/*
  Dessine une fractale de Julia
 */
