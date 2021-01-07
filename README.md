# Robosys2020_ROS
ロボットシステム学課題2

## 動作環境
・OS Melodic Morenia

・Ubuntu20.04

・python 3.8.5


## 環境構築
```
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_create_pkg msgpkg rospy 
$ cd msgpkg
$ mkdir scripts
$ cd scripts
```
moji.pyとtype.pyを作成する。


## 実行方法
```
端末① $ roscore
端末② $ rosrun [msgpkg] moji.py
端末③ $ rosrun [msgpkg] type.py
```

## 動作内容
`$ rosrun [msgpkg] moji.py` を起動し、`$ rosrun [msgpkg] type.py` を起動すると、banana(絵文字)の後ろにfruitが、rose(絵文字)の後ろにflowerが、basket(絵文字)の後ろにsportが出力される。  
banana(絵文字)、rose(絵文字)、basket(絵文字)はランダムに出力される。


## ライセンス
BSD 3-Clause License


## 動画URL
作成したROSのデモ動画
[YouTube](https://youtu.be/LWMRvgoxdrM)

