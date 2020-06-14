
##### [ls](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#ls)

> Usage: hdfs dfs -ls [-R] <args>

```
Options:
    The -R option will return stat recursively through the directory structure.
For a file returns stat on the file with the following format:
permissions number_of_replicas userid groupid filesize modification_date modification_time filename
For a directory it returns list of its direct children as in Unix. A directory is listed as:
permissions userid groupid modification_date modification_time dirname
Example:
    hdfs dfs -ls /user/hadoop/file1
```

```
(base) [root@master test]# hadoop fs -ls / /tests
Found 13 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
-rwxrwxrwx   1 root test               17 2020-06-14 10:39 /test
-rw-r--r--   1 zxy  supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxrwxrwx   - zxy  test                0 2020-06-14 21:11 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
Found 3 items
-rw-r--r--   1 root test                6 2020-06-14 21:05 /tests/merge
-rw-r--r--   1 root test                7 2020-06-14 21:30 /tests/merge1
-rwxrwxrwx   1 zxy  test                5 2020-06-14 10:31 /tests/test
(base) [root@master test]# 
```

##### The -R option will return stat recursively through the directory structure.
```
(base) [root@master test]# hadoop fs -ls -R /tests
-rw-r--r--   1 root test          6 2020-06-14 21:05 /tests/merge
-rw-r--r--   1 root test          7 2020-06-14 21:30 /tests/merge1
-rwxrwxrwx   1 zxy  test          5 2020-06-14 10:31 /tests/test
drwxr-xr-x   - root test          0 2020-06-14 21:49 /tests/testin
-rw-r--r--   1 root test         21 2020-06-14 21:49 /tests/testin/1.txt
(base) [root@master test]# 
```
