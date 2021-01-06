# Robosys2020_ROS
ロボットシステム学課題2

## 環境構築
```
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_create_pkg mypkg rospy 
$ cd mypkg
$ mkdir scripts
$ cd script
```
moji.pyとtype.pyを作成する。

## 動作環境
・ROS Melodic Morenia

・Ubuntu20.04

・Python 3.8.5

## 実行方法
```
端末① $ roscore
端末② $ rosrun [mypkg] moji.py
端末③ $ rosrun [mypkg] type.py
```

## 動作内容
`$ rosrun [pkg_name] moji.py` を起動し、`$ rosrun [pkg_name] type.py` を起動すると、banana(絵文字)の後ろにfruitが、rose(絵文字)の後ろにflowerが、basket(絵文字)の後ろにsportが出力される。  
banana(絵文字)、rose(絵文字)、basket(絵文字)はランダムに出力される。


## ライセンス
BSD 3-Clause License


## 動画URL
作成したROSのデモ動画
[YouTube](https://youtu.be/LWMRvgoxdrM)

