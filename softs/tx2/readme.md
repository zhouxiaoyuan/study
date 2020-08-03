

> 备份镜像
```
"sudo ./flash.sh –r –k APP –G my_backup.img rtso-9003 mmcblk0p1
注意：
关于捞取出来的镜像文件应为 ext4 格式，这样才能烧录成功。
文件格式确认：file my_backup.img
simg2img my_backup.img s.img(转换格式后的生成文件)"

```

>恢复镜像
```
sudo cp ../s.img system.img
sudo ./flash.sh realtimes/rtso-9003 mmcblk0p1
```
