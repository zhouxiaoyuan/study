#### 卸载旧版本
 ```
 sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

#### 设置仓库
```
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```  

>使用以下命令来设置稳定的仓库。
```
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

### Docker安装
#### 安装 Docker Engine-Community
```
sudo yum install -y docker-ce docker-ce-cli containerd.io
```
