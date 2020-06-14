###### [get](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#get)


> Usage: hdfs dfs -get [-ignorecrc] [-crc] <src> <localdst>
```
Copy files to the local file system. Files that fail the CRC check may be copied with the -ignorecrc option. 
Files and CRCs may be copied using the -crc option.
Example:
    hdfs dfs -get /user/hadoop/file localfile
    hdfs dfs -get hdfs://nn.example.com/user/hadoop/file localfile
```

```
(base) [root@master test]# hadoop fs -get /test
(base) [root@master test]# ls
test
(base) [root@master test]# cat test
test

use stdin 
(base) [root@master test]# rm -rf test
(base) [root@master test]# ls
(base) [root@master test]# hadoop fs -get /test testmy
(base) [root@master test]# ls
testmy
(base) [root@master test]# cat testmy
test

use stdin 
(base) [root@master test]#  
```
