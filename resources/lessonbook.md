# micro:bitでブロック崩しゲーム
# 目的
micro:bitを使ってブロック崩しゲームを作る<br>
<mark>fixme</mark> 完成形を差し込む

# 内容目標
- micro:bitでブロック崩しゲームを作る
- micro:bitとはどういうものか、何ができるのかを理解する
- pythonにおける、リスト(配列)の概念を理解する
- 関数についてマスターする
# 目次
# micro:bitとは
BBC micro:bitは、プログラミング可能な小さなコンピューターだ。<br>
学習や教育が楽しく簡単に出来るようにデザインされているよ[[1]](https://groklearning.com/)。<br>
<img src="./image/microbit.jpg" width="50%" height=50%>

# pythonとは
Pythonは、迅速に開発を進め、システムを効果的に統合できるプログラミング言語です[[2]](https://www.python.org/)。<br>
<img src="./image/python.png" width="50%" height=50%>

# コーディング
## プログラム全体図
- ①初期位置にブロックを配置<br>
<img src="./gif/step1.gif" width="10%" height="10%">

- ②一定時間経過でブロックが落下<br>
<img src="./gif/step2.gif" width="10%" height="10%">

- ③一番下まで落ちたら、ブロックをそこに配置<br>
<img src="./gif/step2.gif" width="10%" height="10%">

- ④新しいブロックを生成<br>
<img src="./gif/step3.gif" width="10%" height="10%">

- ⑤一列揃ったらその列を消去<br>
<img src="./gif/step4.gif" width="10%" height="10%">

- ★★一旦完成★★
- Ex. 消したブロックより上のブロックを落とす
- Ex. 効果音を付ける
- Ex. ブロックの種類を追加

Exは順不同。<br>
## micro:bitの紹介(10min)
### LED表示<br>
- 5×5のLEDディスプレイ（発光ダイオード）<br>
<img src="./gif/led.gif" width="25%" height="25%">

### ボタン操作<br>
- 2つのボタン（左Aボタン、右Bボタン）<br>
<img src="./gif/button.gif" width="25%" height="25%">

### 様々なセンサ<br>
- 加速度計<br>
- 磁力計（コンパス）<br>
- 温度センサー<br>
- Bluetooth<br>
- ラジオ通信（他のmicro:bitと通信する）<br>
- 外部入出力ピン（金色のパッド部分）<br>
## 簡単なLED点灯デモ(5min)
### 指定した場所のLEDを点灯<br>
```python: python
flash(x, y, 明るさ)
```
### (2, 2) の位置に明るさ9で点灯
```python: demo1.py
flash(2, 2, 9)
```
### micro:bitで実行
↓のコマンドを TERMINAL で実行する<br>
```bash: TERMINAL
uflash demo.py
```
↓のようにLEDが光れば成功！<br><br>
<img src="./image/demo.png" width="20%" height="20%">

### x座標とy座標について<br>
- x: よこの位置 0（左）〜4（右）<br>
- y: たての位置 0（上）〜4（下）<br>
<img src="./image/zahyo.png" width="20%" height="20%">

### 明るさについて<br>
- 0(真っ暗)〜9(一番明るい)<br>
### 関数について<br>
<mark>fixme</mark> 画像が欲しい<br>

### Work. (0, 4)の位置に明るさ6で点灯してみよう<br>
<u>demo.py</u>のプログラムを、(0, 4)の位置に明るさ6で点灯させるプログラムに書き換えてください。

↓の画像のように光れば成功!<br><br>
<img src="./image/demo1.png" width="20%" height="20%">

<details><summary>答え</summary>

```python:demo.py
flash(0, 4, 6)
```
</details>

### Work. 以下のプログラムを実行した時、どのLEDが光るかを考えてみてください<br>
```python:python
flash(2, 0, 9)
flash(2, 1, 9)
flash(2, 2, 9)
flash(2, 3, 9)
flash(2, 4, 9)
```
<details><summary>答え</summary>
<img src="./image/prac1.png" width="20%" height="20%">
</details>

## Work①,②: 落ちるブロックを作ろう(10min)
ここでは、ブロックが一定時間ごとに落ちていくプログラムを作っていきます。<br>
↓完成形<br><br>
<img src="./gif/main1.gif" width="25%" height="25%">

このために、<br>
#### ①初期位置(一番上の真ん中)にブロックを表示<br>
#### ②そのブロックを一定時間ごとに落とす<br>

という順番でプログラミングをしていきます！<br>

### ①初期位置にブロックを表示<br>
まずは、一番上の真ん中(x = 2, y = 0)の位置にLEDを点灯するプログラムを作っていきます。<br>
これが、ゲームを開始したときのブロックの初期位置になります。<br>

#### 1. main.pyを開く<br>
今までは練習のため、demo.pyというファイルにプログラムを書いていました。<br>
ここからは実際にブロック崩しゲームを作っていくので、本番用のファイル(main.py)を開いてください。<br>
ここからは、プログラムはこの<mark>main.py</mark>に記述していきます。<br>

#### 2. 座標を変数で指定できるようにする<br>
これまではflashの引数には直接数字を入れていました(ex. flash(2, 2, 6))。<br>
しかし、今後のために、LEDを点灯する座標は変数で指定できるようにしておきましょう。<br>
なので、x と y という変数を作成し、初期値を代入してください。<br>
初期値は、一番上の真ん中の位置に表示できるような値にしてください。<br>
<details><summary>答え</summary>

```python:demo.py
x = 2
y = 0
```
</details>

その後、(x,y)の位置に、明るさ9で点灯するプログラムを作成してください<br>

<details><summary>答え</summary>

```python:demo.py
x = 2
y = 0
flash(x, y, 9)
```
</details>

#### 3. 繰り返し処理

現時点のプログラムは、<font color="red">(x, y)を指定し、その座標のLEDを明るさ9で点灯させる</font>というものです。

このプログラムでは、**LEDを一回光らせたらプログラムが終了**しています。<br>
点灯し続けているので**繰り返している**と錯覚するかもしれませんが、 PC から電源が供給され続けているので光っているだけです。<br>
一定時間経過ごとにブロックを落とすためにはプログラムは**終了してほしくない**ので、**繰り返し処理**を追加します<br>
pythonには二種類の繰り返し(ループ)があったのを覚えていますか？<br>
<details><summary>答え</summary>

**for(回数ループ)**
```python:demo.py
for i in range(10):
```
**while(条件ループ)**
```python:demo.py
while True:
```
</details>
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
- 繰り返し処理<br>
今のプログラムでは、LEDを光らせて、プログラムが終了しています。<br>
まずは、LEDを光らせるプログラムをずっと繰り返すようにしましょう<br>
"ずっと繰り返す"は、pythonではどう書いていたでしょうか。<br>
```python
while True:
  処理①
  処理②
  ...
```
- クイズ<br>
以下のプログラムを実行すると、横一列にLEDが全て点灯します。なぜでしょうか？<br>
```python
while True:
  x = random.randint(0, 4)
  flash(x, 0, 9)
```
ヒントは、以下のプログラムを実行すると、縦一列にLEDが点灯します。<br>
```python:python
flash(2, 0, 9)
flash(2, 1, 9)
flash(2, 2, 9)
flash(2, 3, 9)
flash(2, 4, 9)
```

- y座標を変数で指定する<br>
現在のプログラムでは、flash関数のy座標は数値の0を入れています。<br>
 y という変数に0を代入し、flash関数のy座標には変数の y を入れてください<br>
変数への代入は、willeループより上部分で行ってください<br>

- y座標を1ずつ足す(インクリメント)<br>
whileループの中で、LEDを表示した後に、yの数値を +1 してください。<br>

- クイズ<br>
上記のプログラムで上手くいかない理由を考えてみてください<br>

- 
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
[2] https://www.python.org/<br>
[3] https://microbit.org/ja/<br>
[4] https://microbit-micropython.readthedocs.io/en/v2-docs/<br>
[5] https://microbit-micropython.readthedocs.io/ja/latest/<br>


This material benefited from the assistance of ChatGPT.

Kazuma Aoyama(bloodtune65@gmail.com)