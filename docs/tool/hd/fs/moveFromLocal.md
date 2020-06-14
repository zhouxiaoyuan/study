

##### [moveFromLocal](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#moveFromLocal)

> Usage: hdfs dfs -moveFromLocal <localsrc> <dst>
```
Similar to put command, except that the source localsrc is deleted after it's copied.
```

##### copy file 
```
(base) [root@master test]# mkdir moveFromLocal
(base) [root@master test]# ls
merge  mergefile.txt  moveFromLocal  testmy
(base) [root@master test]# hadoop fs -moveFromLocal moveFromLocal /moveFromLocal1
(base) [root@master test]# hadoop fs -ls /
Found 10 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-14 22:08 /moveFromLocal1
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master test]# ls
merge  mergefile.txt  testmy
(base) [root@master test]# 
```

##### single file
```
(base) [root@master test]# echo 'moveTo' > moveto.txt
(base) [root@master test]# hadoop fs -moveToFile /moveFromLocal1/moveto.txt
-moveToFile: Unknown command
(base) [root@master test]# hadoop fs -moveFromLocal moveto.txt  /moveFromLocal1/moveto.txt
(base) [root@master test]# ls
merge  mergefile.txt  testmy
(base) [root@master test]# hadoop fs -lsr /moveFromLocal1
lsr: DEPRECATED: Please use 'ls -R' instead.
-rw-r--r--   1 root supergroup          7 2020-06-14 22:10 /moveFromLocal1/moveto.txt
(base) [root@master test]# 
```
