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
#### Docker安装Cloudera 
[docker搭建CDH集群](https://blog.csdn.net/eyeofeagle/article/details/85159600)
>端口分配规则: 端口加10000,如果超过65535,则加1000
```
docker pull cloudera/quickstart:latest

 docker run \
 -id \
 --hostname=quickstart.cloudera \
--privileged=true  \
 -p 18020:8020 -p 7180:7180 -p 31050:21050 -p 60070:50070 -p 60075:50075 \
 -p 60010:50010 -p 60020:50020 -p 18890:8890 -p 61010:60010 -p 20002:10002  \
 -p 35010:25010 -p 35020:25020 -p 28088:18088 -p 18088:8088 -p 29888:19888 \
 -p 17187:7187 -p 21000:11000 -t -p 18888:8888 \
 --name=mycdh3 \
 cloudera/quickstart /usr/bin/docker-quickstart 
 
 docker exec -it mycdh3 bash
 /home/cloudera/cloudera-manager --enterprise
 
`配置host映射`
root@wang-pc:/home/wang# cat /etc/hosts
127.0.0.1	localhost wang-pc quickstart.cloudera
```
