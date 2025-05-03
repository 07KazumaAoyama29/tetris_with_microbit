# micro:bitでブロック崩しゲーム
## 目的
micro:bitを使ってブロック崩しゲームを作る
## 内容目標
- micro:bitでブロック崩しゲームを作る
- micro:bitとはどういうものか、何ができるのかを理解する
- pythonにおける、リスト(配列)の概念を理解する
- 関数についてマスターする
## 目次
## micro:bitとは
BBC micro:bitは、プログラミング可能な小さなコンピューターだ。<br>
学習や教育が楽しく簡単に出来るようにデザインされているよ[[1]](https://groklearning.com/)。<br>
![err](./image/microbit.jpg)
## pythonとは
## コーディング
### プログラム全体図
初期位置にブロックを配置<br>
![err](./gif/step1.gif)
        ↓<br>
一定時間経過でブロックが落下<br>
        ↓<br>
一番下まで落ちたら、ブロックをそこに配置<br>
        ↓<br>
新しいブロックを生成<br>
        ↓<br>
一列揃ったらその列を消去<br>
        ↓<br>
★★一旦完成★★<br>
        ↓<br>
Ex. 消したブロックより上のブロックを落とす<br>
        ↓<br>
Ex. 効果音を付ける<br>
        ↓<br>
Ex. ブロックの種類を追加<br>
### micro:bitの紹介(10min)
#### LED表示<br>
- 5×5のLEDディスプレイ（発光ダイオード）<br>
#### ボタン操作<br>
- 2つのボタン（左Aボタン、右Bボタン）<br>
#### 様々なセンサ<br>
- 加速度計<br>
- 磁力計（コンパス）<br>
- 温度センサー<br>
- Bluetooth<br>
- ラジオ通信（他のmicro:bitと通信する）<br>
- 外部入出力ピン（金色のパッド部分）<br>
### 簡単なLED点灯デモ(5min)
#### 指定した場所のLEDを点灯<br>
```python:python
flash(x, y, 明るさ)
```
```python:demo1.py
# (2, 2) の位置に明るさ9で点灯
flash(2, 2, 9)
```
```bash:TERMINAL
uflash demo.py
```
#### x座標とy座標について<br>
- x: よこの位置 0（左）〜4（右）<br>
- y: たての位置 0（上）〜4（下）<br>
![err](./image/zahyo.png)
#### 明るさについて<br>
- 0(真っ暗)〜9(一番明るい)<br>
#### 関数について<br>
fixme 画像が欲しい<br>
#### (0, 4)の位置に明るさ6で点灯してみよう<br>
demo.pyのプログラムを、(0, 4)の位置に明るさ6で点灯させるプログラムに書き換えてください。<br>
#### 以下のプログラムを実行した時、どのLEDが光るかを考えてみてください<br>
```python:python
flash(2, 0, 9)
flash(2, 1, 9)
flash(2, 2, 9)
flash(2, 3, 9)
flash(2, 4, 9)
```
### 落ちるブロックを作ろう(20min)
#### 初期位置にブロックを表示<br>
ここでは、一番上(y = 0)のランダムな位置に点灯するプログラムを作っていきます。<br>
これが、ゲームを開始したときのブロックの初期位置になります。

- 左上のLEDを点灯
まずは、(0,0)の位置(左上)に、明るさ9で点灯するプログラムを作成してください。<br>
プログラムは **main.py** に記述してください。

- x座標を変数で指定
次に、xに2を代入するプログラムを作成してください。<br>
その後、(x,0)の位置に、明るさ9で点灯するプログラムを作成してください<br>

- x座標のランダム化
最後に、xに乱数を代入するプログラムを作成してください。<br>
xの範囲は 0 ~ 4 ですので、それ以外の座標を指定するとエラーが出るので注意してください(しかもmicro:bitはエラーが見ずらい)。<br>
```python:ヒント
import random
#5 ~ 10 の乱数を生成
random.randint(5, 10)
```

- 実行して確認
```bash:TERMINAL
uflash main.py
```
micro:bitをパソコンに繋げて、上記のコマンドを実行してみてください。<br>
プログラムが合っていれば、実行する度に光る位置が変わるはずです。<br>

#### ブロックが落下するようにする
- y座標を1ずつ増やして下に落ちる
#### A/Bボタンで左右に動かす

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
[1] https://groklearning.com/<br>
[2] https://microbit.org/ja/<br>
[3] https://microbit-micropython.readthedocs.io/en/v2-docs/<br>
[4] https://microbit-micropython.readthedocs.io/ja/latest/<br>


This material benefited from the assistance of ChatGPT.

Kazuma Aoyama(bloodtune65@gmail.com)