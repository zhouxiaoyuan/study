

##### [getmerge](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#getmerge)

> Usage: hdfs dfs -getmerge <src> <localdst> [addnl]

```
Takes a source directory and a destination file as input and concatenates files in src into the destination local file. 
Optionally addnl can be set to enable adding a newline character at the end of each file.
```

##### merge to local file 
```
(base) [root@master test]# hadoop fs -appendToFile - /tests/merge
merge
(base) [root@master test]# hadoop fs -ls -R /tests
-rw-r--r--   1 root test          6 2020-06-14 21:05 /tests/merge
-rwxrwxrwx   1 zxy  test          5 2020-06-14 10:31 /tests/test
(base) [root@master test]# hadoop fs -cat /tests/merge
merge
(base) [root@master test]# hadoop fs -getmerge /tests /merge.txt
(base) [root@master test]# cat /merge.txt 
merge
test
(base) [root@master test]#
```

##### can merge many file
```
(base) [root@master test]# hadoop fs -getmerge /tests/test  /tests/merge /tests/merge1  /merge1.txt
(base) [root@master test]# cat /merge1.txt
test
merge
merge1
(base) [root@master test]#
```

