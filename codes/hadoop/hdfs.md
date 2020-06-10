###### All FS shell commands take path URIs as arguments.
The URI format is scheme://authority/path. For HDFS the scheme is hdfs, and for the Local FS the scheme is file. 
The scheme and authority are optional. If not specified, the default scheme specified in the configuration is used. 
An HDFS file or directory such as /parent/child can be specified as hdfs://namenodehost/parent/child 
  or simply as /parent/child (given that your configuration is set to point to hdfs://namenodehost)
  
##### appendToFile
##### cat
##### chgrp
##### chmod
##### chown
##### copyFromLocal
##### copyToLocal
##### count
##### cp
##### du
##### dus
##### expunge
##### get
##### getfacl
##### getfattr
##### getmerge
##### ls
##### lsr
##### mkdir
##### moveFromLocal
##### moveToLocal
##### mv
##### put
##### rm
##### rmr
##### setfacl
##### setfattr
##### setrep
##### stat
##### tail
##### test
##### text
##### touchz
