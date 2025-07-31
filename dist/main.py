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
      flash(i, j, list[j][i] * 9)

blocks = [
  [0, 0, 0, 0, 0],  # y=0
  [0, 0, 0, 0, 0],  # y=1
  [0, 0, 0, 0, 0],  # y=2
  [0, 0, 0, 0, 0],  # y=3
  [0, 0, 0, 0, 0],  # y=4
  [1, 1, 1, 1, 1],  # 地面
]
# === ここから書いてOK ===
