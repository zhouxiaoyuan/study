
#### [offical demo](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#cat) 
##### one file
```
(base) [root@master mr]# hadoop fs -cat /test
test

(base) [root@master mr]# 
```

##### many files
```
(base) [root@master mr]# hadoop fs -cat /test /test1 /test2
test

test1
test2
(base) [root@master mr]#
```

##### hdfs URI
```
(base) [root@master mr]# hadoop fs -cat hdfs://master:9000/test  hdfs://master:9000/test1
test

test1
(base) [root@master mr]# 
```

##### local file
```
(base) [root@master mr]# hadoop fs -cat file:///usr/study/codes/mr/tail1.txt   hdfs://master:9000/test
tail1
test
```
