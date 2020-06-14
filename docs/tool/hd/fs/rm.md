
#### [rm](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#rm)

> Usage: hdfs dfs -rm [-f] [-r|-R] [-skipTrash] URI [URI ...]

```
Delete files specified as args.
Options:
    The -f option will not display a diagnostic message or modify the exit status to reflect an error if the file does not exist.
    The -R option deletes the directory and any content under it recursively.
    The -r option is equivalent to -R.
    The -skipTrash option will bypass trash, if enabled, and delete the specified file(s) immediately. 
    This can be useful when it is necessary to delete files from an over-quota directory.
Example:
    hdfs dfs -rm hdfs://nn.example.com/file /user/hadoop/emptydir
```

```
(base) [root@master test]# hadoop fs -ls -R /study
-rw-r--r--   1 root supergroup         13 2020-06-14 22:41 /study/1.txt
(base) [root@master test]# hadoop fs -rm -R -f /study
20/06/14 22:41:40 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
Deleted /study
(base) [root@master test]# hadoop fs -ls /
Found 9 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
-rw-r--r--   1 root supergroup         22 2020-06-14 22:37 /putstdin
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master test]# 
```
