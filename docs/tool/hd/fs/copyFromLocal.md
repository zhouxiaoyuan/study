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
