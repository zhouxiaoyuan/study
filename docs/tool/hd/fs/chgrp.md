
#### [chgrp](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#chgrp)

```
Change group association of files. The user must be the owner of files, or else a super-user.
Additional information is in the Permissions Guide.
```

##### offical demo




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


