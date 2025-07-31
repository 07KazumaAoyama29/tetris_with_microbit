# === これは編集しないこと！ ===
from microbit import *

def flash(x, y, light):
    display.set_pixel(x, y, light)

# === ここから書いてOK ===
# (2, 2) の位置に明るさ9で点灯
flash(2, 2, 9)