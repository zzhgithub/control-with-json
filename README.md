# 简单的文件时间控制


## 思路：
启动一个服务。传文件地址来读取文件之后创建定时任务。
文件示例在example.json中。offset的单位为s


在视频播放时同时调用/run接口比如:
```ssh
ffmpeg test.mp4 && curl 0.0.0.0:5000/run?file=example.json 
```

其中解释命令的处理和硬件的交互处理在
core_dealer.py中


## 思路2
使用vlc播放用python控制监听事件

安装依赖 vlc pyqt5
PS:这个mac上安装好费劲！