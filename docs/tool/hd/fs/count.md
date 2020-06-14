
#### [count](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/CommandsManual.html)

>Usage: `hadoop fs -count [-q] [-h] [-v] [-x] [-t [<storage type>]] [-u] [-e] <paths>`
```
Count the number of directories, files and bytes under the paths that match the specified file pattern. 
  Get the quota and the usage. 
The output columns with -count are: DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME
The -u and -q options control what columns the output contains. -q means show quotas, 
  -u limits the output to show quotas and usage only.
The -h option shows sizes in human readable format.
```

> hadoop 3.0+
```
The output columns with -count -q are: QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, 
  DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME
The output columns with -count -u are: QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, PATHNAME
The -t option shows the quota and usage for each storage type. The -t option is ignored if -u or -q option is not given.
  The list of possible parameters that can be used in -t option(case insensitive except the parameter ""): 
  "", “all”, “ram_disk”, “ssd”, “disk” or “archive”.

The -v option displays a header line.
The -x option excludes snapshots from the result calculation. 
  Without the -x option (default), the result is always calculated from all INodes, 
  including all snapshots under the given path.
The -x option is ignored if -u or -q option is given.
The -e option shows the erasure coding policy for each file.
The output columns with -count -e are: DIR_COUNT, FILE_COUNT, CONTENT_SIZE, ERASURECODING_POLICY, PATHNAME
The ERASURECODING_POLICY is name of the policy for the file. 
  If a erasure coding policy is setted on that file, it will return name of the policy. 
  If no erasure coding policy is setted, it will return "Replicated" which means it use replication storage strategy.
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
  
 ##### default `DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME`
 ```
  (base) [root@master zxy]# hadoop fs -count /
          55           55            3381120 /
 ```

##### -q  `QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, DIR_COUNT, FILE_COUNT, CONTENT_SIZE, PATHNAME`
```
(base) [root@master zxy]# hadoop fs -count -q  /
9223372036854775807 9223372036854775697            none             inf           55           55            3381120 /
```

##### -h `The -h option shows sizes in human readable format`
```
(base) [root@master zxy]# hadoop fs -count -h  /
          55           55              3.2 M /
(base) [root@master zxy]# 
```

##### -q -h 
```
(base) [root@master zxy]# hadoop fs -count -q -h  /
       8.0 E           8.0 E            none             inf           55           55              3.2 M /
(base) [root@master zxy]# 
```


#####  -u `QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, PATHNAME`
