

|ffserver|ffmpeg|ffmpeg-python|mkvserver_mk2|
|:-:|:-:|:-:|:-:|
|[NVIDIA DeepStream](https://developer.nvidia.com/deepstream-sdk)||||
|[FFserver](https://trac.ffmpeg.org/wiki/ffserver)|[FFmpeg](https://ffmpeg.org/ffmpeg.html)|[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)|[mkvserver_mk2](https://github.com/klaxa/mkvserver_mk2)|

> [ideo_stream_convert+环境安装](https://github.com/yywbxgl/rtsp_opencv_demo) <br>
> [ffmpeg+ffserver搭建rtsp服务器](https://blog.csdn.net/FPGATOM/article/details/98782202) <br>
> [python利用ffmpeg进行rtmp推流直播](https://blog.csdn.net/rainweic/article/details/94666527) <br>
> [FFMPEG常用命令](https://www.jianshu.com/p/80d40dd670d4) <br><br>

> [https://blog.csdn.net/u014162133/article/details/81188410](https://blog.csdn.net/u014162133/article/details/81188410)

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
FileMaxSize 5M
</Feed>

<Stream test.h264>
Feed feed1.ffm
Format rtp
#VideoCodec libx264
VideoCodec mpeg4
VideoFrameRate 30
VideoBufferSize 80000
VideoBitRate 1000
VideoSize 1280x720
VideoQMin 1
VideoQMax 5
#AVPresetVideo default
#AVPresetVideo baseline
#AVOptionVideo flags +global_header
PreRoll 0
NoAudio
</Stream>


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
 参数
```
-c:v：指定编码器，编码器列表可以使用ffmpeg -codecs查看
-vf scale：指定输出视频的宽高，高-1代表按照比例自动适应
-b:v：指定输出视频的码率，即输出视频每秒的bit数
libx264支持的其他参数请使用ffmpeg -h encoder=libx264命令查询，如转码为其他编码，也可使用类似命令查询可用参数
```


直播地址

```
香港卫视：http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8

CCTV1高清：http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8

CCTV3高清：http://ivi.bupt.edu.cn/hls/cctv3hd.m3u8

CCTV5高清：http://ivi.bupt.edu.cn/hls/cctv5hd.m3u8

CCTV5+高清：http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8

CCTV6高清：http://ivi.bupt.edu.cn/hls/cctv6hd.m3u8
```


TX2 GPU <br>
[使用GPU硬件加速FFmpeg视频转码](https://www.jianshu.com/p/59da3d350488) <br>
[FFmpeg 编译支持NVIDIA硬件编解码-windows平台](https://www.jianshu.com/p/032b47c48ada)
