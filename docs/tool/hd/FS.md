
### [File System(FS)](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#put)
#### All FS shell commands take path URIs(scheme://authority/path) as arguments.

###### 更新到getfacl命令

|命令|功能|
|:-:|:-:|
|appendToFile|Append single src, or multiple srcs from local file system to the destination file system.<br> Also reads input from stdin and appends to destination file system|
|cat||
|checksum||
|chgrp||
|chmod||
|chown||
|copyFromLocal||
|copyToLocal||
|count||
|cp||
|createSnapshot||
|deleteSnapshot||
|df||
|du||
|dus||
|expunge||
|find||
|get||
|getfacl||
|getfattr||
|getmerge||
|head||
|help||
|ls||
|lsr||
|mkdir||
|moveFromLocal||
|moveToLocal||
|mv||
|put||
|renameSnapshot||
|rm||
|rmdir||
|rmr||
|setfacl||
|setfattr||
|setrep||
|stat||
|tail||
|test||
|text||
|touch||
|touchz||
|truncate||
|usage||
|Deleting objects||
|Overwriting Objects||
|Timestamps||
|Security model and operations||
|Commands of limited value||

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

##### find
```
Usage: hadoop fs -find <path> ... <expression> ...
Finds all files that match the specified expression and applies selected actions to them. 
If no path is specified then defaults to the current working directory. 
If no expression is specified then defaults to -print.
The following primary expressions are recognised:
    -name pattern
    -iname pattern
    Evaluates as true if the basename of the file matches the pattern using standard file system globbing. 
    If -iname is used then the match is case insensitive.
    -print
    -print0
    Always evaluates to true. Causes the current pathname to be written to standard output. 
    If the -print0 expression is used then an ASCII NULL character is appended.
The following operators are recognised:
    expression -a expression
    expression -and expression
    expression expression

    Logical AND operator for joining two expressions. Returns true if both child expressions return true. 
    Implied by the juxtaposition of two expressions and so does not need to be explicitly specified. 
    The second expression will not be applied if the first fails.
Example:
hadoop fs -find / -name test -print
```

###### get
```
Usage: hadoop fs -get [-ignorecrc] [-crc] [-p] [-f] <src> <localdst>
Copy files to the local file system. Files that fail the CRC check may be copied with the -ignorecrc option.
Files and CRCs may be copied using the -crc option.
Example:
    hadoop fs -get /user/hadoop/file localfile
    hadoop fs -get hdfs://nn.example.com/user/hadoop/file localfile
Options:
    -p : Preserves access and modification times, ownership and the permissions. 
    (assuming the permissions can be propagated across filesystems)
    -f : Overwrites the destination if it already exists.
    -ignorecrc : Skip CRC checks on the file(s) downloaded.
    -crc: write CRC checksums for the files downloaded.
```

##### getfacl
```
Usage: hadoop fs -getfacl [-R] <path>
Displays the Access Control Lists (ACLs) of files and directories. 
If a directory has a default ACL, then getfacl also displays the default ACL.
Options:
    -R: List the ACLs of all files and directories recursively.
    path: File or directory to list.
Examples:
    hadoop fs -getfacl /file
    hadoop fs -getfacl -R /dir
```

##### copyFromLocal
```
Usage: hadoop fs -copyFromLocal <localsrc> URI
Similar to the fs -put command, except that the source is restricted to a local file reference.
Options:
    -p : Preserves access and modification times, ownership and the permissions. 
    (assuming the permissions can be propagated across filesystems)
    -f : Overwrites the destination if it already exists.
    -l : Allow DataNode to lazily persist the file to disk, Forces a replication factor of 1. 
        This flag will result in reduced durability. Use with care.
    -d : Skip creation of temporary file with the suffix ._COPYING_.
```

##### copyToLocal
```
Usage: hadoop fs -copyToLocal [-ignorecrc] [-crc] URI <localdst>
Similar to get command, except that the destination is restricted to a local file reference
```

##### cp
```
Usage: hadoop fs -cp [-f] [-p | -p[topax]] URI [URI ...] <dest>
Copy files from source to destination. 
This command allows multiple sources as well in which case the destination must be a directory.
‘raw.*’ namespace extended attributes are preserved if (1) the source and destination filesystems support them (HDFS only), 
and (2) all source and destination pathnames are in the /.reserved/raw hierarchy. 
Determination of whether raw.* namespace xattrs are preserved is independent of the -p (preserve) flag.
Options:
    The -f option will overwrite the destination if it already exists.
    The -p option will preserve file attributes [topx] (timestamps, ownership, permission, ACL, XAttr). 
    If -p is specified with no arg, then preserves timestamps, ownership, permission. 
    If -pa is specified, then preserves permission also because ACL is a super-set of permission.
    Determination of whether raw namespace extended attributes are preserved is independent of the -p flag.
Example:
    hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2
    hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir
```

##### count
```
Usage: hadoop fs -count [-q] [-h] [-v] [-x] [-t [<storage type>]] [-u] [-e] <paths>
Count the number of directories, files and bytes under the paths that match the specified file pattern. 
Get the quota and the usage. The output columns with -count are: DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME
The -u and -q options control what columns the output contains. -q means show quotas, -u limits the output to show quotas and usage only.
The output columns with -count -q are: QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME
The output columns with -count -u are: QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, PATHNAME
The -t option shows the quota and usage for each storage type. The -t option is ignored if -u or -q option is not given. 
The list of possible parameters that can be used in -t option(case insensitive except the parameter ""): 
    "", “all”, “ram_disk”, “ssd”, “disk” or “archive”.
The -h option shows sizes in human readable format.
The -v option displays a header line.
The -x option excludes snapshots from the result calculation. Without the -x option (default), 
    the result is always calculated from all INodes, including all snapshots under the given path. 
    The -x option is ignored if -u or -q option is given.
The -e option shows the erasure coding policy for each file.
The output columns with -count -e are: DIR_COUNT, FILE_COUNT, CONTENT_SIZE, ERASURECODING_POLICY, PATHNAME
The ERASURECODING_POLICY is name of the policy for the file. If a erasure coding policy is setted on that file, 
    it will return name of the policy. If no erasure coding policy is setted, 
    it will return "Replicated" which means it use replication storage strategy.
Example:
    hadoop fs -count hdfs://nn1.example.com/file1 hdfs://nn2.example.com/file2
    hadoop fs -count -q hdfs://nn1.example.com/file1
    hadoop fs -count -q -h hdfs://nn1.example.com/file1
    hadoop fs -count -q -h -v hdfs://nn1.example.com/file1
    hadoop fs -count -u hdfs://nn1.example.com/file1
    hadoop fs -count -u -h hdfs://nn1.example.com/file1
    hadoop fs -count -u -h -v hdfs://nn1.example.com/file1
    hadoop fs -count -e hdfs://nn1.example.com/file1
```

##### df
```
Usage: hadoop fs -df [-h] URI [URI ...]
Displays free space.
Options:
    The -h option will format file sizes in a “human-readable” fashion (e.g 64.0m instead of 67108864)
```

##### du
```
Usage: hadoop fs -du [-s] [-h] [-v] [-x] URI [URI ...]
Displays sizes of files and directories contained in the given directory or the length of a file in case its just a file.
Options:
    The -s option will result in an aggregate summary of file lengths being displayed, rather than the individual files. 
        Without the -s option, calculation is done by going 1-level deep from the given path.
    The -h option will format file sizes in a “human-readable” fashion (e.g 64.0m instead of 67108864)
    The -v option will display the names of columns as a header line.
    The -x option will exclude snapshots from the result calculation. Without the -x option (default), 
    the result is always calculated from all INodes, including all snapshots under the given path.
The du returns three columns with the following format:
size disk_space_consumed_with_all_replicas full_path_name
Example:
    hadoop fs -du /user/hadoop/dir1 /user/hadoop/file1 hdfs://nn.example.com/user/hadoop/dir1
```

##### dus
```
Usage: hadoop fs -dus <args>
Displays a summary of file lengths.
Note: This command is deprecated. Instead use hadoop fs -du -s.
```

##### expunge
```
Usage: hadoop fs -expunge [-immediate]
Permanently delete files in checkpoints older than the retention threshold from trash directory, and create new checkpoint.
When checkpoint is created, recently deleted files in trash are moved under the checkpoint. 
Files in checkpoints older than fs.trash.interval will be permanently deleted on the next invocation of -expunge command.
If the file system supports the feature, users can configure to create and delete checkpoints periodically 
    by the parameter stored as fs.trash.checkpoint.interval (in core-site.xml). 
This value should be smaller or equal to fs.trash.interval.
If the -immediate option is passed, all files in the trash for the current user are immediately deleted, 
    ignoring the fs.trash.interval setting.
Refer to the HDFS Architecture guide for more information about trash feature of HDFS.
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
