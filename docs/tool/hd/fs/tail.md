##### [tail](https://hadoop.apache.org/docs/r2.6.5/hadoop-project-dist/hadoop-common/FileSystemShell.html#tail)

> Usage: hdfs dfs -tail [-f] URI

```
Displays last kilobyte of the file to stdout.
Options:
    The -f option will output appended data as the file grows, as in Unix.
Example:
    hdfs dfs -tail pathname
```

```
(base) [root@master test]# hadoop fs -tail /The_Man_of_Property.txt
yon.
“The door was open,” he said. “Might I see your wife for a minute, I have a message for her?”
Soames gave him a strange, sidelong stare.
“My wife can see no one,” he muttered doggedly.
Young Jolyon answered gently: “I shouldn’t keep her a minute.”
Soames brushed by him and barred the way.
“She can see no one,” he said again.
Young Jolyon’s glance shot past him into the hall, and Soames turned. There in the drawing-room doorway stood Irene, her eyes were wild and eager, her lips were parted, her hands outstretched. In the sight of both men that light vanished from her face; her hands dropped to her sides; she stood like stone.
Soames spun round, and met his visitor’s eyes, and at the look he saw in them, a sound like a snarl escaped him. He drew his lips back in the ghost of a smile.
“This is my house,” he said; “I manage my own affairs. I’ve told you once — I tell you again; we are not at home.”
And in young Jolyon’s face he slammed the door.

The End
(base) [root@master test]# 
```
