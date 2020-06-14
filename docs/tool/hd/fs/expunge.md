



##### [expunge](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#expunge)
```
Usage: hdfs dfs -expunge
Empty the Trash. Refer to the HDFS Architecture Guide for more information on the Trash feature.
```

###### demo
```
(base) [root@master fs]# hadoop fs -expunge 
20/06/14 20:24:47 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
(base) [root@master fs]# 
```
