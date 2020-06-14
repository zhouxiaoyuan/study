
#### [mkdir](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#mkdir)

> Usage: hdfs dfs -mkdir [-p] <paths>

```
Takes path uri's as argument and creates directories.
Options:
    The -p option behavior is much like Unix mkdir -p, creating parent directories along the path.
Example:
    hdfs dfs -mkdir /user/hadoop/dir1 /user/hadoop/dir2
    hdfs dfs -mkdir hdfs://nn1.example.com/user/hadoop/dir hdfs://nn2.example.com/user/hadoop/dir
```

##### create remote hdfs directory 
```  
(base) [root@master test]# hadoop fs -mkdir hdfs://39.103.157.181:9000/zxy20200614
(base) [root@master test]# 
````

#####  -p  `creating parent directories along the path `
```
(base) [root@master test]# hadoop fs -mkdir  /mkdir/mkdir1/mkdir2
mkdir: `/mkdir/mkdir1/mkdir2': No such file or directory
(base) [root@master test]# hadoop fs -mkdir -p  /mkdir/mkdir1/mkdir2
(base) [root@master test]# hadoop fs -ls -R /mkdir
drwxr-xr-x   - root supergroup          0 2020-06-14 22:01 /mkdir/mkdir1
drwxr-xr-x   - root supergroup          0 2020-06-14 22:01 /mkdir/mkdir1/mkdir2
(base) [root@master test]# 
```

##### create many directory 
```
(base) [root@master test]# hadoop fs -mkdir /mkdir1 /mkdir2 /mkdir3
(base) [root@master test]# hadoop fs -ls /
Found 16 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-14 21:59 /mkdir1
drwxr-xr-x   - root supergroup          0 2020-06-14 21:59 /mkdir2
drwxr-xr-x   - root supergroup          0 2020-06-14 21:59 /mkdir3
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
-rwxrwxrwx   1 root test               17 2020-06-14 10:39 /test
-rw-r--r--   1 zxy  supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxrwxrwx   - zxy  test                0 2020-06-14 21:49 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master test]# 
```

