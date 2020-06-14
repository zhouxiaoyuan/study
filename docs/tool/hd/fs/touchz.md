
##### [touchz](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#touchz)

> Usage: hdfs dfs -touchz URI [URI ...]
```
Create a file of zero length.
Example:
    hdfs dfs -touchz pathname
```

```
(base) [root@master test]# hadoop fs -touchz /touchz
(base) [root@master test]# hadoop fs -text /touchz
(base) [root@master test]# 
```
