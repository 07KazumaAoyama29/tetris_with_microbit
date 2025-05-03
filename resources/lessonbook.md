# micro:bitでブロック崩しゲーム
## 目的
## 内容目標
## 目次
## micro:bitとは
## pythonとは
## コーディング
### micro:bitの紹介(10min)
- LED表示
- ボタン操作
- など
### 簡単なLED点灯デモ(5min)
- 指定した場所のLEDを点灯<br>
```python
from microbit import *

# (2, 2) の位置に明るさ9で点灯
display.set_pixel(2, 2, 9)
```
- x座標とy座標について
- 関数について
- (0, 4)の位置に明るさ6で点灯してみよう<br>
demo.pyのプログラムを、(0, 4)の位置に明るさ6で点灯させるプログラムに書き換えてください。
### 落ちるブロックを作ろう(20min)
- 初期位置にブロックを表示
- A/Bボタンで左右に動かす
- y座標を1ずつ増やして下に落ちる
### 着地したブロックを記録しよう(20min)
- 落ちたブロックを「床」として記録
- 落ちたらその場所にブロックを固定し、次のブロックを出す
### 一列揃ったら消そう(15min)
### リスト(配列とは)
- リストと配列は厳密には違うけど、同じものだと思ってくれていい
### 一列揃ったら消すプログラムを書こう
### 一列消したらブロックが降ってくるようにしよう

## まとめ
## 参考文献
https://microbit-micropython.readthedocs.io/en/v2-docs/<br>
https://microbit-micropython.readthedocs.io/ja/latest/<br>


This material benefited from the assistance of ChatGPT.

Kazuma Aoyama(bloodtune65@gmail.com)