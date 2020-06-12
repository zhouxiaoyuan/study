
### [File System(FS)](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#put)
#### All FS shell commands take path URIs(scheme://authority/path) as arguments.

##### appendToFile
```
  Append single src, or multiple srcs from local file system to the destination file system.
  Also reads input from stdin and appends to destination file system.
hadoop fs -appendToFile localfile /user/hadoop/hadoopfile
hadoop fs -appendToFile localfile1 localfile2 /user/hadoop/hadoopfile
hadoop fs -appendToFile localfile hdfs://nn.example.com/hadoop/hadoopfile
hadoop fs -appendToFile - hdfs://nn.example.com/hadoop/hadoopfile Reads the input from stdin.
```
##### cat
```
Usage: hadoop fs -cat [-ignoreCrc] URI [URI ...]
Copies source paths to stdout.
Options
    The -ignoreCrc option disables checkshum verification.
Example:
    hadoop fs -cat hdfs://nn1.example.com/file1 hdfs://nn2.example.com/file2
    hadoop fs -cat file:///file3 /user/hadoop/file4
```
