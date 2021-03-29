

Selected config:
Port           : 6379
Config file    : /etc/redis/6379.conf
Log file       : /var/log/redis_6379.log
Data dir       : /var/lib/redis/6379
Executable     : /bigdata/installs/redis-6.2.1/bin/redis-server
Cli Executable : /usr/local/bin/redis-cli




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


