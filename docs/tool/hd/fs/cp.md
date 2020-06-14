
#### [cp](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#cp)
```
Usage: hadoop fs -cp [-f] [-p | -p[topax]] URI [URI ...] <dest>
Copy files from source to destination. This command allows multiple sources as well in which case the destination must be a directory.
  ‘raw.*’ namespace extended attributes are preserved if (1) the source and destination filesystems support them (HDFS only),
  and (2) all source and destination pathnames are in the /.reserved/raw hierarchy. 
Determination of whether raw.* namespace xattrs are preserved is independent of the -p (preserve) flag.

Options:
    The -f option will overwrite the destination if it already exists.
    The -p option will preserve file attributes [topx] (timestamps, ownership, permission, ACL, XAttr). 
      If -p is specified with no arg, then preserves timestamps, ownership, permission. If -pa is specified, 
      then preserves permission also because ACL is a super-set of permission. 
      Determination of whether raw namespace extended attributes are preserved is independent of the -p flag.
Example:
    hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2
    hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir
```

##### many files
```
(base) [root@master zxy]# hadoop fs -ls /
Found 12 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
-rwxrwxrwx   1 root test               17 2020-06-14 10:39 /test
-rw-r--r--   1 zxy  supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxrwxrwx   - zxy  test                0 2020-06-14 10:36 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master zxy]# hadoop fs -mkdir /cps
(base) [root@master zxy]# hadoop fs -ls /
Found 13 items
-rw-r--r--   1 root supergroup    1896621 2020-06-11 09:54 /1.data
-rw-r--r--   1 root supergroup     632207 2020-06-11 23:26 /The_Man_of_Property.txt
drwxr-xr-x   - root supergroup          0 2020-06-14 16:42 /cps
drwxr-xr-x   - root supergroup          0 2020-05-29 06:01 /hbase
drwxr-xr-x   - root supergroup          0 2020-06-11 10:02 /output
drwxr-xr-x   - root supergroup          0 2020-06-11 23:51 /output_file_broadcast
drwxr-xr-x   - root supergroup          0 2020-06-08 06:38 /study
-rw-r--r--   1 root supergroup          6 2020-06-13 23:38 /tailln
-rwxrwxrwx   1 root test               17 2020-06-14 10:39 /test
-rw-r--r--   1 zxy  supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxrwxrwx   - zxy  test                0 2020-06-14 10:36 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master zxy]# hadoop fs -cp /test /test1 /cps
(base) [root@master zxy]# hadoop fs -ls -R /cps
-rw-r--r--   1 root supergroup         17 2020-06-14 16:42 /cps/test
-rw-r--r--   1 root supergroup          6 2020-06-14 16:42 /cps/test1
(base) [root@master zxy]# 
```
