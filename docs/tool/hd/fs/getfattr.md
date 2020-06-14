
#### [getfattr](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#getfattr)

> Usage: hdfs dfs -getfattr [-R] -n name | -d [-e en] <path>

```
Displays the extended attribute names and values (if any) for a file or directory.
Options:
    -R: Recursively list the attributes for all files and directories.
    -n name: Dump the named extended attribute value.
    -d: Dump all extended attribute values associated with pathname.
    -e encoding: Encode values after retrieving them. Valid encodings are "text", "hex", and "base64". Values encoded as text strings are enclosed in double quotes ("), and values encoded as hexadecimal and base64 are prefixed with 0x and 0s, respectively.
    path: The file or directory.
Examples:
    hdfs dfs -getfattr -d /file
    hdfs dfs -getfattr -R -n user.myAttr /dir
```

```
(base) [root@master test]# hadoop fs -getfattr -d  /test1
# file: /test1
```

    
    
