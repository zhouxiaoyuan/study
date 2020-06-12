
#### 设置hostname
```
hostnamectl set-hostname  master
```


#### SSH互信
```
ssh-keygen -t rsa
ssh-copy-id -i ip
```


#### 关闭防火墙
```
systemctl stop firewalld.service #停止firewall
systemctl disable firewalld.service #禁止firewall开机启动
```
