
### [File System(FS)](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#put)
#### All FS shell commands take path URIs(scheme://authority/path) as arguments.
```
Append single src, or multiple srcs from local file system to the destination file system. Also reads input from stdin and appends to destination file system.
```

##### appendToFile
```
hadoop fs -appendToFile localfile /user/hadoop/hadoopfile
hadoop fs -appendToFile localfile1 localfile2 /user/hadoop/hadoopfile
hadoop fs -appendToFile localfile hdfs://nn.example.com/hadoop/hadoopfile
hadoop fs -appendToFile - hdfs://nn.example.com/hadoop/hadoopfile Reads the input from stdin.
```
