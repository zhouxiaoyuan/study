

> make ; make PREFIX=/bigdata/installs/redis-6.2.1 install ; utils install_server.sh 
```
Selected config:
Port           : 6379
Config file    : /etc/redis/6379.conf
Log file       : /var/log/redis_6379.log
Data dir       : /var/lib/redis/6379
Executable     : /bigdata/installs/redis-6.2.1/bin/redis-server
Cli Executable : /usr/local/bin/redis-cli
Is this ok? Then press ENTER to go on or Ctrl-C to abort.
Copied /tmp/6379.conf => /etc/init.d/redis_6379
Installing service...
Successfully added to chkconfig!
Successfully added to runlevels 345!
Starting Redis server...
Installation successful!
```


> 布隆过滤器启动 redis-server  /etc/redis/6379.conf --loadmodule /bigdata/installs/redis-6.2.1/bin/redisbloom.so


运行脚本install_server.sh可能会报如下错误：

| This systems seems to use systemd.
| Please take a look at the provided example service unit files in this directory, and adapt and install them. Sorry!


#bail if this system is managed by systemd
_pid_1_exe="$(readlink -f /proc/1/exe)"
if [ "${_pid_1_exe##*/}" = systemd ]
then
        echo "This systems seems to use systemd."
        echo "Please take a look at the provided example service unit files in this directory, and adapt and install them. Sorry!"
        exit 1
fi
unset _pid_1_exe


