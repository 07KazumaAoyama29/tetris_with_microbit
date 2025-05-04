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
## micro:bitの紹介(3min)
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
<ins>demo.py</ins>のプログラムを、(0, 4)の位置に明るさ6で点灯させるプログラムに書き換えてください。

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
今までは練習のため、<ins>demo.py</ins>というファイルにプログラムを書いていました。<br>
ここからは実際にブロック崩しゲームを作っていくので、本番用のファイル(<ins>main.py</ins>)を開いてください。<br>
ここからは、プログラムはこの<ins>main.py</ins>に記述していきます。<br>

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

現時点のプログラムは、**(x, y)を指定し、その座標のLEDを明るさ9で点灯させる**というものです。

このプログラムでは、**LEDを一回光らせたらプログラムが終了**しています。<br>
点灯し続けているので**繰り返している**と錯覚するかもしれませんが、 PC から電源が供給され続けているので光っているだけです。<br>
一定時間経過ごとにブロックを落とすためにはプログラムは**終了してほしくない**ので、**繰り返し処理**を追加します<br>
pythonには**二種類**の繰り返し(ループ)があったのを覚えていますか？<br>
<details><summary>答え</summary>

**for(回数ループ)**
```python:demo.py
for i in range(10):
```
**while(条件ループ)**
```python:demo.py
while 条件式:
```
</details>

ブロック崩しゲームの場合、どちらのループを使う方が良いでしょうか？
<details><summary>答え</summary>

一般的には、ゲームが終了するまで何回ループをするかは分からない(時と場合による)ので、本レッスンでは while を使います。<br>
ゲームの終了条件を今の進捗で入れるのは難しいので、とりあえず無限ループにしましょう。<br>
**while(無限)**
```python:demo.py
x = 2
y = 0
while True:
  flash(x, y, 9)
```
</details>

これで繰り返し処理の実装も完了しました。<br>
- 実行して確認
```bash:TERMINAL
uflash main.py
```
micro:bitをパソコンに繋げて、上記のコマンドを実行してみてください。<br>
↓のように初期位置が光っていたら成功です！<br>
<img src="./image/prac2.png" width="20%" height="20%">


### ②ブロックが落下するようにする
準備が整ったので、いよいよ本題の**落下するプログラム**を書いていきます！<br>
#### 1. フローチャート
現時点のプログラムは、**同じ場所のLEDを点灯し続ける**プログラムです。<br>
フローチャートは以下になります。<br>
```
(2, 0)の位置のLEDを点灯
↓
(2, 0)の位置のLEDを点灯
↓
(2, 0)の位置のLEDを点灯
↓
...
```
落ちているように見せるためには、フローチャートは以下である必要があります。<br>
```
(2, 0)の位置のLEDを点灯
↓
(2, 1)の位置のLEDを点灯
↓
(2, 2)の位置のLEDを点灯
↓
...
```
つまり、yの座標を1ずつ増やしていけばいいわけです。<br>
これを見据えて、上記ではyの変数化を行いました。<br>
プログラムのフローチャートを詳しく書くと、以下になります。<br>
```
xに2を、yに0を代入
↓
(x, y)の位置のLEDを点灯
↓
yの数字を+1する
↓
(x, y)の位置のLEDを点灯
↓
yの数字を+1する
↓
...
```
となるようにプログラムを変更すればよさそうですね。<br>
#### 2. フローチャートを基にプログラム作成
上記のフローチャートを参考にしながら、落下するプログラムを自力で作ってみてください。<br>
<details><summary>(とりあえずの)答え</summary>

```python:demo.py
x = 2
y = 0
while True:
  flash(x, y, 9)
  y += 1(もしくは、 y = y + 1)
```
フローチャート通りに素直に書くと、こうなるはずです。<br>

#### クイズ
上記のプログラムを実行すると、↓のように一瞬で一列が光るはずです。なぜでしょうか？<br>
<img src="./image/prac3.png" width="20%" height="20%">

<details><summary>答え</summary>

少し前に下記のようなクイズをしたのを覚えていますか？<br>
### Work. 以下のプログラムを実行した時、どのLEDが光るかを考えてみてください<br>
```python:python
flash(2, 0, 9)
flash(2, 1, 9)
flash(2, 2, 9)
flash(2, 3, 9)
flash(2, 4, 9)
```
<img src="./image/prac1.png" width="20%" height="20%">
この時に、flash関数は、指定した座標を光らせる(だけ)の関数だと説明しました。<br>
つまり、LEDを消すためには、LEDを消す関数(clear)を使わなければいけません。<br>
ということは、上記で考えたフローチャートが間違っていたというわけです。間違っていたというよりも、見積りが甘かったという方が適切かもしれません。<br>
```
(2,0)を点灯
↓
LEDを消す
↓
(2,1)を点灯
↓
...
```
となればいいので、
```python
flash(2, 0, 9)
clear()
flash(2, 1, 9)
clear()
flash(2, 2, 9)
clear()
flash(2, 3, 9)
clear()
flash(2, 4, 9)
```
という風に、flash関数の間にclear関数を挟んであげればよさそうです。<br>
しかし、実行すると↓のように、一番下だけが点灯します。なぜでしょうか？<br>
<img src="./image/prac4.png" width="20%" height="20%">
<details><summary>答え</summary>

**プログラムはあっています。**<br>
しかし、**プログラムは一行0.05秒ぐらいで処理される**ので、**一瞬で一番下まで行ってしまった**ということです。<br>
ただし、これだと動きが速すぎて目で追えないので、**少し待機してもらいましょう**。<br>
待機する関数は、**sleep**です。引数の単位は秒ではなく**ミリ秒**(秒/1000)なので気を付けてください。
```
(2,0)を点灯
↓
0.5秒待機
↓
LEDを消す
↓
(2,1)を点灯
↓
0.5秒待機
↓
...
```
となればいいので、
```python
flash(2, 0, 9)
sleep(500)
clear()
flash(2, 1, 9)
sleep(500)
clear()
flash(2, 2, 9)
sleep(500)
clear()
flash(2, 3, 9)
sleep(500)
clear()
flash(2, 4, 9)
```
このプログラムを実行すると、↓のように期待通りに動いてくれます。<br>
<img src="./gif/main1.gif" width="25%" height="25%">
上記のプログラムを参考にして、<ins>main.py</ins>のプログラムを修正していきましょう！<br>
</details>
</details>
</details>

#### 3. フローチャートの修正
上記で、先ほど作ったフローチャートに二つミスがあることが発覚しました。<br>
- 消灯する処理が抜けていた<br>
- 待機する処理が抜けていた<br>

#### Ex. プログラミングの面白さ
皆さんはプログラムが間違っていたりエラーが出たりすると失敗したと思って落ち込むかもしれません。<br>
しかし、これからは間違っていたりエラーが出たりしたときは**喜んで**ください。<br>
プログラミングの一番の醍醐味は、(私の意見では)トライ&エラーです。<br>
少し考えただけでは一発でうまくいかないような難題を、何が足りていないか、どういう機能を追加したらよいか、もっと改善する方法はないか…と考え挑戦することで、立派な作品を作ることができます。<br>
これは難しい作品であればあるほど、完成したときの喜びは大きいです。<br>
作品の難しさは、間違った回数やエラーが出た回数だと思っています<br>
つまり、間違っていたりエラーが出たりすればするほど完成したときの喜びが大きくなっていくのです。<br>
なので、プログラムが間違っていたりエラーが出たりしても笑顔で、その原因を一つずつつぶしていきましょう。<br>

#### 3. フローチャートの修正
話が脱線しましたが、フローチャートの修正を行っていきます。<br>
修正すべきポイントは、以下の２点でした。<br>
- 消灯する処理を追加する<br>
- 待機する処理を追加する<br>

今回は２つ一気に修正できそうです。修正したフローチャートは以下です。<br>
```
xに2を、yに0を代入
↓
(x, y)の位置のLEDを点灯
↓
0.5秒待つ
↓
clear()
↓
yの数字を+1する
↓
(x, y)の位置のLEDを点灯
↓
0.5秒待つ
↓
clear()
↓
yの数字を+1する
↓
...
```
このフローチャート通りにプログラムを書けば、落ちるプログラムが完成します！やってみましょう！<br>
- 0.5秒待つ: sleep(500)
- clear(): clear()
<details><summary>答え</summary>

```python:demo.py
x = 2
y = 0
while True:
  flash(x, y, 9)
  sleep(500)
  clear()
  y += 1
```
</details>
下まで行くと変なマークが表示されますが、今は気にしないでおきましょう。<br>

## 着地したブロックを記録しよう(20min)
- 落ちたブロックを「床」として記録
- 落ちたらその場所にブロックを固定し、次のブロックを出す
## A/Bボタンでブロックを左右に動かそう
## 一列揃ったら消そう(15min)
### リスト(配列とは)
- リストと配列は厳密には違うけど、同じものだと思ってくれていい
### 一列揃ったら消すプログラムを書こう
## Ex. 一列消したらブロックが降ってくるようにしよう

## まとめ
## 参考文献
[1] https://groklearning.com/<br>
[2] https://www.python.org/<br>
[3] https://microbit.org/ja/<br>
[4] https://microbit-micropython.readthedocs.io/en/v2-docs/<br>
[5] https://microbit-micropython.readthedocs.io/ja/latest/<br>


This material benefited from the assistance of ChatGPT.

Kazuma Aoyama(bloodtune65@gmail.com)