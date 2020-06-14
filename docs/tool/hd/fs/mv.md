

##### [mv](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#mv)

> Usage: hdfs dfs -mv URI [URI ...] <dest>
```
Moves files from source to destination. 
This command allows multiple sources as well in which case the destination needs to be a directory. 
Moving files across file systems is not permitted.
Example:
    hdfs dfs -mv /user/hadoop/file1 /user/hadoop/file2
    hdfs dfs -mv hdfs://nn.example.com/file1 hdfs://nn.example.com/file2 hdfs://nn.example.com/file3 hdfs://nn.example.com/dir1
```

##### move 
```
(base) [root@master test]# hadoop fs -mv /moveFromLocal1/moveto.txt /moveTo
(base) [root@master test]# hadoop fs -ls /
Found 11 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-14 22:18 /moveFromLocal1
-rw-r--r--   1 root supergroup          7 2020-06-14 22:10 /moveTo
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master test]# hadoop fs -ls -R /moveTo
-rw-r--r--   1 root supergroup          7 2020-06-14 22:10 /moveTo
(base) [root@master test]# hadoop fs -ls -R /moveFromLocal1
(base) [root@master test]# 
```

##### Moving files across file systems is not permitted.
```
(base) [root@master test]# hadoop fs -mv /moveTo  hdfs://39.103.157.181:9000/
mv: `/moveTo': Does not match target filesystem
(base) [root@master test]# hadoop fs -ls  hdfs://39.103.157.181:9000/
Found 17 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 hdfs://39.103.157.181:9000/1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 hdfs://39.103.157.181:9000/The_Man_of_Property.txt
-rw-r--r--   1 root supergroup        495 2020-06-12 14:25 hdfs://39.103.157.181:9000/a.txt
-rw-r--r--   1 root supergroup        404 2020-06-12 14:25 hdfs://39.103.157.181:9000/b.txt
-rw-r--r--   1 root supergroup       2541 2020-06-12 14:42 hdfs://39.103.157.181:9000/cookie_ip.txt
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 hdfs://39.103.157.181:9000/hbase
-rw-r--r--   1 root supergroup   12224421 2020-06-12 14:43 hdfs://39.103.157.181:9000/ip.lib.txt
drwxr-xr-x   - root supergroup          0 2020-06-12 13:43 hdfs://39.103.157.181:9000/output
drwxr-xr-x   - root supergroup          0 2020-06-12 16:33 hdfs://39.103.157.181:9000/output_cachearchive_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-12 14:07 hdfs://39.103.157.181:9000/output_cachefile_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-12 14:43 hdfs://39.103.157.181:9000/output_ip_lib
drwxr-xr-x   - root supergroup          0 2020-06-12 14:26 hdfs://39.103.157.181:9000/output_sort
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 hdfs://39.103.157.181:9000/study
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 hdfs://39.103.157.181:9000/tmp
-rw-r--r--   1 root supergroup        321 2020-06-12 14:10 hdfs://39.103.157.181:9000/w.tar.gz
-rw-r--r--   1 root supergroup         24 2020-06-12 14:06 hdfs://39.103.157.181:9000/white_list
drwxr-xr-x   - root supergroup          0 2020-06-14 21:57 hdfs://39.103.157.181:9000/zxy20200614
(base) [root@master test]# hadoop fs -mv /moveTo  /move1
(base) [root@master test]# 
```
