
##### [put](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#put)

> Usage: hdfs dfs -put <localsrc> ... <dst>
```
Copy single src, or multiple srcs from local file system to the destination file system. 
Also reads input from stdin and writes to destination file system.
    hdfs dfs -put localfile /user/hadoop/hadoopfile
    hdfs dfs -put localfile1 localfile2 /user/hadoop/hadoopdir
    hdfs dfs -put localfile hdfs://nn.example.com/hadoop/hadoopfile
    hdfs dfs -put - hdfs://nn.example.com/hadoop/hadoopfile Reads the input from stdin.
```

##### put single file 
```
(base) [root@master test]# echo 'put' > put.txt
(base) [root@master test]# hadoop fs -put put.txt /
(base) [root@master test]# hadoop fs -ls /
Found 1 items
-rw-r--r--   1 root supergroup          4 2020-06-14 22:28 /put.txt
(base) [root@master test]# hadoop fs -text /put.txt
put
(base) [root@master test]# 
```
##### put directory 
```
(base) [root@master test]# touch puts/1.txt
(base) [root@master test]# ls
merge  mergefile.txt  move  puts  put.txt  testmy
(base) [root@master test]# ls -R puts
puts:
1.txt
(base) [root@master test]# hadoop fs -put puts /
(base) [root@master test]# hadoop fs -ls -R /puts
-rw-r--r--   1 root supergroup          0 2020-06-14 22:34 /puts/1.txt
(base) [root@master test]# 
```

##### put stdin
```
(base) [root@master test]# hadoop fs -put - /putstdin
1234
3242
hello world
(base) [root@master test]# hadoop fs -ls /
Found 10 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
-rw-r--r--   1 root supergroup         22 2020-06-14 22:37 /putstdin
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master test]# hadoop fs -text /putstdin
1234
3242
hello world
(base) [root@master test]# 
```


