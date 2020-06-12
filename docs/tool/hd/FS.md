
### [File System(FS)](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#put)
#### All FS shell commands take path URIs(scheme://authority/path) as arguments.

##### appendToFile
```
Usage: hadoop fs -appendToFile <localsrc> ... <dst>
Append single src, or multiple srcs from local file system to the destination file system.
Also reads input from stdin and appends to destination file system.
Example:
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

##### copyFromLocal
```
Usage: hadoop fs -copyFromLocal <localsrc> URI
Similar to the fs -put command, except that the source is restricted to a local file reference.
Options:
    -p : Preserves access and modification times, ownership and the permissions. (assuming the permissions can be propagated across filesystems)
    -f : Overwrites the destination if it already exists.
    -l : Allow DataNode to lazily persist the file to disk, Forces a replication factor of 1. This flag will result in reduced durability. Use with care.
    -d : Skip creation of temporary file with the suffix ._COPYING_.
```

##### checksum
```
Usage: hadoop fs -checksum URI
Returns the checksum information of a file.
Example:
    hadoop fs -checksum hdfs://nn1.example.com/file1
    hadoop fs -checksum file:///etc/hosts
```

##### chgrp
```
Usage: hadoop fs -chgrp [-R] GROUP URI [URI ...]
Change group association of files. The user must be the owner of files, or else a super-user. 
Additional information is in the Permissions Guide.
Options
    The -R option will make the change recursively through the directory structure.
```

##### chmod
```
Usage: hadoop fs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI ...]
Change the permissions of files. With -R, make the change recursively through the directory structure. 
The user must be the owner of the file, or else a super-user. 
Additional information is in the Permissions Guide.
Options
    The -R option will make the change recursively through the directory structure.
```

##### chown
```
Usage: hadoop fs -chown [-R] [OWNER][:[GROUP]] URI [URI ]
Change the owner of files. The user must be a super-user. Additional information is in the Permissions Guide.
Options
    The -R option will make the change recursively through the directory structure.
```
