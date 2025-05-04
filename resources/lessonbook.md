# micro:bitでブロック崩しゲーム
## 目的
micro:bitを使ってブロック崩しゲームを作る<br>
<mark>fixme</mark> 完成形を差し込む
## 内容目標
- micro:bitでブロック崩しゲームを作る
- micro:bitとはどういうものか、何ができるのかを理解する
- pythonにおける、リスト(配列)の概念を理解する
- 関数についてマスターする
## 目次
## micro:bitとは
BBC micro:bitは、プログラミング可能な小さなコンピューターだ。<br>
学習や教育が楽しく簡単に出来るようにデザインされているよ[[1]](https://groklearning.com/)。<br>
<img src="./image/microbit.jpg" width="50%" height=50%>

## pythonとは
Pythonは、迅速に開発を進め、システムを効果的に統合できるプログラミング言語です[[2]](https://www.python.org/)。<br>
<img src="./image/python.png" width="50%" height=50%>

## コーディング
### プログラム全体図
- 初期位置にブロックを配置<br>
<img src="./gif/step1.gif" width="10%" height="10%">

- 一定時間経過でブロックが落下<br>
<img src="./gif/step2.gif" width="10%" height="10%">

- 一番下まで落ちたら、ブロックをそこに配置<br>
<img src="./gif/step2.gif" width="10%" height="10%">

- 新しいブロックを生成<br>
<img src="./gif/step3.gif" width="10%" height="10%">

- 一列揃ったらその列を消去<br>
<img src="./gif/step4.gif" width="10%" height="10%">

- ★★一旦完成★★
- Ex. 消したブロックより上のブロックを落とす
- Ex. 効果音を付ける
- Ex. ブロックの種類を追加
### micro:bitの紹介(10min)
#### LED表示<br>
- 5×5のLEDディスプレイ（発光ダイオード）<br>
<img src="./gif/led.gif" width="25%" height="25%">

#### ボタン操作<br>
- 2つのボタン（左Aボタン、右Bボタン）<br>
<img src="./gif/button.gif" width="25%" height="25%">

#### 様々なセンサ<br>
- 加速度計<br>
- 磁力計（コンパス）<br>
- 温度センサー<br>
- Bluetooth<br>
- ラジオ通信（他のmicro:bitと通信する）<br>
- 外部入出力ピン（金色のパッド部分）<br>
### 簡単なLED点灯デモ(5min)
#### 指定した場所のLEDを点灯<br>
```python: python
flash(x, y, 明るさ)
```
#### (2, 2) の位置に明るさ9で点灯
```python: demo1.py
flash(2, 2, 9)
```
#### micro:bitで実行
↓のコマンドを TERMINAL で実行する<br>
```bash: TERMINAL
uflash demo.py
```
↓のようにLEDが光れば成功！<br><br>
<img src="./image/demo.png" width="20%" height="20%">

#### x座標とy座標について<br>
- x: よこの位置 0（左）〜4（右）<br>
- y: たての位置 0（上）〜4（下）<br>
<img src="./image/zahyo.png" width="20%" height="20%">

#### 明るさについて<br>
- 0(真っ暗)〜9(一番明るい)<br>
#### 関数について<br>
<mark>fixme</mark> 画像が欲しい<br>

#### (0, 4)の位置に明るさ6で点灯してみよう<br>
<u>demo.py</u>のプログラムを、(0, 4)の位置に明るさ6で点灯させるプログラムに書き換えてください。

↓の画像のように光れば成功!<br><br>
<img src="./image/demo1.png" width="20%" height="20%">

<details><summary>答え</summary>

```python:demo.py
flash(0, 4, 6)
```
</details>

#### 以下のプログラムを実行した時、どのLEDが光るかを考えてみてください<br>
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

### 落ちるブロックを作ろう(20min)
ここでは、ブロックが一定時間ごとに落ちていくプログラムを作っていきます。<br>

#### 初期位置にブロックを表示<br>
まずは、一番上の真ん中(x = 2, y = 0)の位置にLEDを点灯するプログラムを作っていきます。<br>
これが、ゲームを開始したときのブロックの初期位置になります。

- 左上のLEDを点灯<br>
まずは、(0,0)の位置(左上)に、明るさ9で点灯するプログラムを作成してください。<br>
プログラムは<mark>main.py</mark>に記述してください。

- x座標を変数で指定<br>
次に、xに2を代入するプログラムを作成してください。<br>
その後、(x,0)の位置に、明るさ9で点灯するプログラムを作成してください<br>

- x座標のランダム化<br>
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