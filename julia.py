void julia(float c_r, float c_i, float zoom) {

  tft.setCursor(0,0);
  float new_r = 0.0, new_i = 0.0, old_r = 0.0, old_i = 0.0;

  /* Pour chaque pixel en X */

  for(int16_t x = SCREEN_WIDTH/2 - 1; x >= 0; x--) { // Rely on inverted symmetry
    /* Pour chaque pixel en Y */
    for(uint16_t y = 0; y < SCREEN_HEIGHT; y++) {      
      old_r = 1.5 * (x - SCREEN_WIDTH / 2) / (0.5 * zoom * SCREEN_WIDTH);
      old_i = (y - SCREEN_HEIGHT / 2) / (0.5 * zoom * SCREEN_HEIGHT);
      uint16_t i = 0;

      while ((old_r * old_r + old_i * old_i) < 4.0 && i < MAX_ITERATION) {
        new_r = old_r * old_r - old_i * old_i ;
        new_i = 2.0 * old_r * old_i;

        old_r = new_r+c_r;
        old_i = new_i+c_i;
        
        i++;
      }
      /* Affiche le pixel */
      if (i < 100){
        tft.drawPixel(x,y,tft.color565(255,255,map(i,0,100,255,0)));
        tft.drawPixel(SCREEN_WIDTH - x - 1,SCREEN_HEIGHT - y - 1,tft.color565(255,255,map(i,0,100,255,0)));
      }if(i<200){
        tft.drawPixel(x,y,tft.color565(255,map(i,100,200,255,0),0));
        tft.drawPixel(SCREEN_WIDTH - x - 1,SCREEN_HEIGHT - y - 1,tft.color565(255,map(i,100,200,255,0),0));
      }else{
        tft.drawPixel(x,y,tft.color565(map(i,200,300,255,0),0,0));
        tft.drawPixel(SCREEN_WIDTH - x - 1,SCREEN_HEIGHT - y - 1,tft.color565(map(i,200,300,255,0),0,0));
      }
    }
  }
}
