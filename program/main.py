# === これは編集しないこと！ ===
from microbit import *
import random
def flash(x, y, light):
    display.set_pixel(x, y, light)

# === ここから書いてOK ===
x = random.randint(0, 4)
y = 0
while True:
  flash(x, y, 9)
  microbit.sleep(500)
  if y < 4: y += 1