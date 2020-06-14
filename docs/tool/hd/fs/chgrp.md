
#### [chgrp](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#chgrp)

```
Change group association of files. The user must be the owner of files, or else a super-user.
Additional information is in the Permissions Guide.
```

##### chgrp single file
```
(base) [root@master zxy]# hadoop fs -chgrp test /test
(base) [root@master zxy]# hadoop fs -ls /
Found 11 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
-rw-r--r--   1 root test               17 2020-06-13 23:14 /test
-rw-r--r--   1 root supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master zxy]# 
```



##### add usr
```
首先新建用户，建议用adduser命令
sudo adduser hadoop
passwd hadoop
输入密码后一直按回车即可，最后输入y确定。

在创建hadoop用户的同时也创建了hadoop用户组，下面我们把hadoop用户加入到hadoop用户组
输入
sudo usermod -a -G hadoop hadoop 

前面一个hadoop是组名，后面一个hadoop是用户名。完成后输入一下命令查询结果。
cat  /etc/group
然后再把hadoop用户赋予root权限，让他可以使用sudo命令

切换到可以root的用户输入
sudo gedit /etc/sudoers
sudo vi /etc/sudoers
在图形界面可以用第一个命令，是ubuntu自带的一个文字编辑器，终端命令界面使用第二个命令。有关vi编辑器的使用自行百度。

修改文件如下：
# User privilege specification
root ALL=(ALL) ALL
hadoop ALL=(ALL) ALL
保存退出，hadoop用户就拥有了root权限。
```


