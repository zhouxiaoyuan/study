

##### [rmr](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#rmr)

> Usage: hdfs dfs -rmr [-skipTrash] URI [URI ...]
```
Recursive version of delete.
Note: This command is deprecated. Instead use hdfs dfs -rm -r
```

```
(base) [root@master test]# hadoop fs -put puts /
(base) [root@master test]# hadoop fs -ls -R /puts
-rw-r--r--   1 root supergroup          0 2020-06-14 22:45 /puts/1.txt
(base) [root@master test]# hadoop fs -rmr /puts
rmr: DEPRECATED: Please use 'rm -r' instead.
20/06/14 22:45:26 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
Deleted /puts
(base) [root@master test]# 
```

