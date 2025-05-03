# === これは編集しないこと！ ===
from microbit import *
import random
def flash(x, y, light):
    display.set_pixel(x, y, light)

# === ここから書いてOK ===
while True:
  x = random.randint(0, 4)
  flash(x, 0, 9)
  microbit.sleep(500)