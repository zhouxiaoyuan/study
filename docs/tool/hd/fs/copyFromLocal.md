##### [copyFromLocal](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#copyFromLocal)

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

##### single file
```
(base) [root@master zxy]# hadoop fs -copyFromLocal test /tests
(base) [root@master zxy]# hadoop fs -ls  /tests
Found 1 items
-rw-r--r--   1 root supergroup          5 2020-06-14 10:31 /tests/test
(base) [root@master zxy]# 
```

#### directory
```
(base) [root@master zxy]# ls
d        Documents  –generate-config  mysql-community-release-el7-5.noarch.rpm  Public     test
Desktop  Downloads  Music             Pictures                                  Templates  Videos
(base) [root@master zxy]# hadoop fs -copyFromLocal d /tests
(base) [root@master zxy]# hadoop fs -lsr /tests
lsr: DEPRECATED: Please use 'ls -R' instead.
drwxr-xr-x   - root supergroup          0 2020-06-14 10:36 /tests/d
-rw-r--r--   1 root supergroup          3 2020-06-14 10:36 /tests/d/d
-rw-r--r--   1 root supergroup          5 2020-06-14 10:31 /tests/test
(base) [root@master zxy]# 
```


