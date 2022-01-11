# ロボットシステム学課題２
2021年ロボットシステム学の講義で作成したROSのパッケージをベースに、作成・改造したものです。

コマンドを入力することによって数値が出力されます。

下に実行した様子を撮った動画のURLを載せているので是非見てください。

# 動作環境
今回は以下の環境で動作を行いました。

〇Raspberry Pi 3 Model B

〇Os:ubuntu 20.04 server

〇ROS:noetic

# 利用したもの
〇Raspberry Pi 3 Model B

# インストール
以下の手順に従って入力してください。

① $ cd catkin_ws/src

② $ git clone git@github.com:itsukiueno/kadai2.git

③ $ cd ..

④ $ catkin_make


# 実行
以下のコマンドを打ち実行することができます。

### 手順１
まずは４つの端末を用意してそれぞれの端末で以下の表のコマンドを打ってください。

|  | 端末① | 端末② | 端末３ | 端末④ |
| :---: | :---: | :---: | :---: | :---: |
| コマンド | $ cd catkin_ws/src | $ cd catkin_ws | $ cd catkin_ws/src/mypkg/scripts | - |

### 手順２
端末①で　$ roscore　と打ちます。

### 手順３
端末②で　$ rosrun mypkg count.py　と打ちます。

### 手順４
端末③で　$ rosrun mypkg twice.py　と打ちます。

### 手順５
端末④で　$ rostopic echo /twice　と打ちます。

### 実行内容
以上のコマンドを打つことによって、0から200までの数字が0から100の間では２の倍数が連続で、100から200の間では４の倍数が連続で出力されます。順番に数が出力され200まで行くと次は0に戻り同じくループします。


# 実行動画

# ライセンス
GNU General Public License v3.0


# コントリビューション

