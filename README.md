# robosys
2021年度ロボットシステム学の課題2です。

# 動作環境
Ubuntu20.04

Raspberry Pi 4

ROS

# 実行

Ubuntuを3つ立ち上げておく
---
## branchの変更
 ```
 git branch Douseki
 ```

## count.pyを立ち上げる

ロスコアを立ち上げる
 ```
roscore &
 ```
 ```
chmod +x count.py
 ```
  ```
source ~/.bashrc
 ```
 実行
 ```
rosrun mypkg count.py
 ```
 経過秒数のみを見る
 ```
rostopic echo /count_up
 ```
## twice.pyを立ち上げる
  ```
chmod +x twice.py
 ```
  ```
source ~/.bashrc
 ```
 実行
 ```
rosrun mypkg twice.py
 ```
 実行中の内容を見る
 ```
rostopic echo /twice
 ```
## third.pyを立ち上げる
  ```
chmod +x third.py
 ```
  ```
source ~/.bashrc
 ```
 実行
 ```
rosrun mypkg third.py
 ```
 実行中の内容を見る
 ```
rostopic echo /third
 ```
# デモ動画

https://youtu.be/OMmtrcRYW1M

# ライセンス
Copyright (c) 2022 Ryuichi Ueda

Copyright (c) 2022 Douseki Tei

ライセンスについて：[LISENCE](https://github.com/hiro2001/mypkg/blob/main/LICENSE)
