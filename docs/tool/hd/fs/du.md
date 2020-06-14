##### [du](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#du)

>Usage: hdfs dfs -du [-s] [-h] URI [URI ...]

```
Displays sizes of files and directories contained in the given directory or the length of a file in case its just a file.
Options:
    The -s option will result in an aggregate summary of file lengths being displayed, rather than the individual files.
    The -h option will format file sizes in a "human-readable" fashion (e.g 64.0m instead of 67108864)
Example:
    hdfs dfs -du /user/hadoop/dir1 /user/hadoop/file1 hdfs://nn.example.com/user/hadoop/dir1
 ```
 
#### demo
```
(base) [root@master fs]# hadoop fs -du /
1896621  /1.data
632207   /The_Man_of_Property.txt
23       /cps
18496    /hbase
183609   /output
31       /output_file_broadcast
0        /study
6        /tailln
17       /test
6        /test1
6        /test2
8        /tests
650090   /tmp
(base) [root@master fs]# hadoop fs -du -s  /
3381120  /
(base) [root@master fs]# hadoop fs -du -h  /
1.8 M    /1.data
617.4 K  /The_Man_of_Property.txt
23       /cps
18.1 K   /hbase
179.3 K  /output
31       /output_file_broadcast
0        /study
6        /tailln
17       /test
6        /test1
6        /test2
8        /tests
634.9 K  /tmp
```
