#### [copyToLocal](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#copyToLocal)

>Usage: hadoop fs -copyToLocal [-ignorecrc] [-crc] URI <localdst>

`Similar to get command, except that the destination is restricted to a local file reference.`

##### single file
```
[zxy@master ~]$ hadoop fs -copyToLocal /test
[zxy@master ~]$ ll
total 12
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Desktop
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Documents
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Downloads
-rw-r--r--. 1 root root    0 Jun  7 11:41 –generate-config
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Music
-rw-r--r--. 1 root root 6140 Nov 12  2015 mysql-community-release-el7-5.noarch.rpm
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Pictures
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Public
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Templates
-rw-r--r--. 1 zxy  zxy    17 Jun 14 11:50 test
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Videos
```

##### directory
```
[zxy@master ~]$ hadoop fs -copyToLocal /tests
[zxy@master ~]$ ll
total 12
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Desktop
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Documents
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Downloads
-rw-r--r--. 1 root root    0 Jun  7 11:41 –generate-config
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Music
-rw-r--r--. 1 root root 6140 Nov 12  2015 mysql-community-release-el7-5.noarch.rpm
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Pictures
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Public
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Templates
-rw-r--r--. 1 zxy  zxy    17 Jun 14 11:50 test
drwxrwxr-x. 3 zxy  zxy    27 Jun 14 11:50 tests
drwxr-xr-x. 2 zxy  zxy     6 May 22 07:33 Videos

```
