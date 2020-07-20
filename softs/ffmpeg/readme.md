

|ffmpeg|ffmpeg-python|
|:-:|:-:|
|[FFmpeg](https://ffmpeg.org/ffmpeg.html)|[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)|

[python利用ffmpeg进行rtmp推流直播](https://blog.csdn.net/rainweic/article/details/94666527)


思路:
  1. FFserver搭建视频流中转服务   
  ```
  ffserver -f /opt/ffserver.conf
  ```
  2. 使用python的subprocess模块Popen方法打开一个command，并定义接收管道
  ```
    import subprocess as sp

    # ffmpeg command
    command = ['ffmpeg',
             '-y',
             '-an',
             '-f', 'rawvideo',
             '-pix_fmt', 'bgr24',
             '-s', "1920x1200",
             '-r', '20',
             '-i', '-',
             '-c:v', 'mpeg4',
             '-b:v', '500k',
             '-preset', 'ultrafast',
             '-tune', 'zerolatency',
             '-muxrate', '1250k',
             '-qmax', '51',
             '-filter_threads', '4', 
             rtmpUrl]

    # 管道配置
    p = sp.Popen(command, stdin=sp.PIPE)   
  ```
  
  3. 程序将视频帧推送到接收管道中
  ```
    # write to pipe
    p.stdin.write(frame.tostring())
  ```
  
  

组件:
 1. FFserver
 
