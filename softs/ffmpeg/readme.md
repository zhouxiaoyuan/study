

|ffserver|ffmpeg|ffmpeg-python|mkvserver_mk2|
|:-:|:-:|:-:|:-:|
|[FFserver](https://trac.ffmpeg.org/wiki/ffserver)|[FFmpeg](https://ffmpeg.org/ffmpeg.html)|[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)|[mkvserver_mk2](https://github.com/klaxa/mkvserver_mk2)|

> [ideo_stream_convert+环境安装](https://github.com/yywbxgl/rtsp_opencv_demo) <br>
> [ffmpeg+ffserver搭建rtsp服务器](https://blog.csdn.net/FPGATOM/article/details/98782202) <br>
> [python利用ffmpeg进行rtmp推流直播](https://blog.csdn.net/rainweic/article/details/94666527) <br>
> [FFMPEG常用命令](https://www.jianshu.com/p/80d40dd670d4)


搭建:
  1. ffmpeg 安装
  2.

思路:
  1. FFserver搭建视频流中转服务   
  ```
  ffserver -f /opt/ffserver.conf
  
  HttpPort 8090
  RtspPort 8554
  HttpBindAddress 0.0.0.0
  MaxClients 1000
  MaxBandwidth 10000
  CustomLog -
  NoDaemon

  <Feed feed1.ffm>
  File ./feed1.ffm
  FileMaxSize 500M
  #ffmpeg http://172.16.17.119:8090/feed1.ffm
  </Feed>

  <Stream test.h264>
  Feed feed1.ffm
  Format rtp
  #VideoCodec libx264
  VideoCodec mpeg4
  HttpPort 8090
  RtspPort 8554
  HttpBindAddress 0.0.0.0
  MaxClients 1000
  MaxBandwidth 10000
  CustomLog -
  NoDaemon

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
 ```
 Warning: ffserver has been removed on 2018-01-06. If you still need it checkout commit 2ca65fc or use the 3.4 release branch. The original documentation has been archived and can be downloaded as ​HTML or ​PDF while the sample ffserver configuration file can be found below. We can provide no support for ffserver.
Or try an alternative such as ​mkvserver_mk2.
```
```
Input sources (I)
Feeds (F)
Streams (S)
Media players (P)
```
 
 命令:
 ```
 通过ffprobe命令识别并输出视频信息
 ffprobe -v error -show_streams -print_format json <input>  
 ```
 
