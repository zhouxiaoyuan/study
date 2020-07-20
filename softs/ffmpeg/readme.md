

|ffmpeg|ffmpeg-python|
|:-:|:-:|
|[FFmpeg](https://ffmpeg.org/ffmpeg.html)|[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)|

[python利用ffmpeg进行rtmp推流直播](https://blog.csdn.net/rainweic/article/details/94666527)


思路:
  1. FFserver搭建视频流中转服务
  2. 使用python的subprocess模块Popen方法打开一个command，并定义接收管道
  3. 程序将视频帧推送到接收管道中
  
  

组件:
 1. FFserver
 
