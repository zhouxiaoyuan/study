
##### [chmod](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#chmod)

> Usage: hadoop fs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI ...]
```
Change the permissions of files. With -R, make the change recursively through the directory structure. 
The user must be the owner of the file, or else a super-user. Additional information is in the Permissions Guide.
```

###### single file 
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
-rw-r--r--   1 root test               17 2020-06-14 10:39 /test
-rw-r--r--   1 root supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxr-xr-x   - root test                0 2020-06-14 10:36 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
(base) [root@master zxy]# hadoop fs -chmod 777 /test
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
-rw-r--r--   1 root supergroup          6 2020-06-13 23:05 /test1
-rw-r--r--   1 root supergroup          6 2020-06-13 23:07 /test2
drwxr-xr-x   - root test                0 2020-06-14 10:36 /tests
drwx-wx-wx   - root supergroup          0 2020-06-11 10:02 /tmp
```

##### directory
```
(base) [root@master zxy]# hadoop fs -chmod -R 777 /tests
(base) [root@master zxy]# hadoop fs -ls -R  /tests
drwxrwxrwx   - root test          0 2020-06-14 10:36 /tests/d
-rwxrwxrwx   1 root test          3 2020-06-14 10:36 /tests/d/d
-rwxrwxrwx   1 root test          5 2020-06-14 10:31 /tests/test
(base) [root@master zxy]# 
```

