##### one file
```
(base) [root@master mr]# hadoop fs -text /test
test
(base) [root@master mr]# echo 'tail' > tail.txt
(base) [root@master mr]# hadoop fs -appendToFile tail.txt /test
(base) [root@master mr]# hadoop fs -text /test
test
tail
(base) [root@master mr]# 
```

##### two file
```
(base) [root@master mr]# hadoop fs -appendToFile tail1.txt tail2.txt /test
(base) [root@master mr]# hadoop fs -text /test
test
tail
tail1
tail2
(base) [root@master mr]# 
```

##### hdfs URI
```
(base) [root@master mr]# echo "hdfs" > tailhdfs.txt
(base) [root@master mr]# hadoop fs -appendToFile tail1.txt tail2.txt hdfs://master:9000/test
(base) [root@master mr]# hadoop fs -text /test
test
tail
tail1
tail2
hdfs
```

#####  from stdin  
###### use __CTRL+D__ exit from stdin
```
(base) [root@master mr]# hadoop fs -appendToFile - /test
i am zhouxiaoyuan
(base) [root@master mr]# 
(base) [root@master mr]# hadoop fs -text /test
test
tail
tail1
tail2
tail1
tail2
hdfs
i am zhouxiaoyuan
(base) [root@master mr]# 
```

