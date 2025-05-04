# === これは編集しないこと！ ===
from microbit import *
import random
def flash(x, y, light):
    display.set_pixel(x, y, light)
def clear():
    display.clear()
def flashm(list):
   for i in range(5):
      for j in range(5):
         if list[j][i] != 0 : flash(i, j, 9)

blocks = [
  [0, 0, 0, 0, 1],  # y=0
  [0, 0, 0, 0, 0],  # y=1
  [0, 0, 1, 0, 0],  # y=2
  [0, 0, 0, 0, 0],  # y=3
  [0, 0, 0, 0, 1],  # y=4
]

# === ここから書いてOK ===
x = 2
y = 0
timer = 0
while True:
  flash(x, y, 9)
  timer += 1
  if timer % 10000 == 0:
    clear()
    y += 1
    if y > 4 : y = 0
  if button_a.was_pressed() and x > 0:
        x -= 1
        clear()
  if button_b.was_pressed() and x < 4:
        x += 1
        clear()
flashm(blocks)