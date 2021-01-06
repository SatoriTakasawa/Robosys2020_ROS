# Robosys2020_ROS
ロボットシステム学課題2

## インストール方法
```
$ makdir -p catkin_ws/src
$ cd ~/catkin_ws/src


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

