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

#### 扩展功能
##### create fs file
```
(base) [root@master mr]# hadoop fs -rm /test
20/06/13 22:43:53 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
Deleted /test
(base) [root@master mr]# hadoop fs -ls /
Found 7 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master mr]# hadoop fs -appendToFile - /test
test    

(base) [root@master mr]# hadoop fs -text /test
test

(base) [root@master mr]# 
```

