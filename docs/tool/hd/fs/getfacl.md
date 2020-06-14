
##### [getfacl](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#getfacl)
```
Usage: hdfs dfs -getfacl [-R] <path>
Displays the Access Control Lists (ACLs) of files and directories.
If a directory has a default ACL, then getfacl also displays the default ACL.
Options:
    -R: List the ACLs of all files and directories recursively.
    path: File or directory to list.
Examples:
    hdfs dfs -getfacl /file
    hdfs dfs -getfacl -R /dir
```

##### demo
```
(base) [root@master test]# hadoop fs -getfacl /test
# file: /test
# owner: root
# group: test
user::rwx
group::rwx
other::rwx

(base) [root@master test]# 
```
    
    
    
