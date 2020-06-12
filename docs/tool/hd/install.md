
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

#### 设置/etc/profile
```
export HADOOP_HOME=/usr/local/src/hadoop-2.6.1
export SCALA_HOME=/usr/local/src/scala-2.13.2
export ZOOKEEPER_HOME=/usr/local/src/zookeeper-3.4.5
export JAVA_HOME=/usr/local/src/jdk1.8.0_251
export CLASSPATH=.:${JAVA_HOME}/lib/tools.jar
export SPARK_HOME=/usr/local/src/spark-1.6.3-bin-hadoop2.6
export PATH=$SCALA_HOME/bin:$SPARK_HOME/sbin:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${JAVA_HOME}/bin:$PATH:${ZOOKEEPER_HOME}/bin
```
