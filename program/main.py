# === これは編集しないこと！ ===
from microbit import *
import random
def flash(x, y, light):
    display.set_pixel(x, y, light)
def clear():
    display.clear()

# === ここから書いてOK ===
x = 2
y = 0
while True:
  flash(x, y, 9)
  sleep(500)
  clear()
  y += 1