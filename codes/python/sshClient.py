
#paramiko

import paramiko

# 创建一个ssh的客户端，用来连接服务器
ssh = paramiko.SSHClient()
# 创建一个ssh的白名单
know_host = paramiko.AutoAddPolicy()
# 加载创建的白名单
ssh.set_missing_host_key_policy(know_host)

# 连接服务器
ssh.connect(
    hostname="172.16.17.51",
    port=22,
    username="zxy",
    password="zxy"
)

class sshClient:
    host = ""
    port = 22
    username = "root"
    password = ""
    ssh = paramiko.SSHClient()
    # 创建一个ssh的白名单
    know_host = paramiko.AutoAddPolicy()
    # 加载创建的白名单
    ssh.set_missing_host_key_policy(know_host)

    def __init__( self,host ,port , username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        ssh.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password
        )
        print(f'connect {host}:{port} by{username}/{password} success!')

    def exec(self,command):
        stdin, stdout, stderr =  ssh.exec_command(command)
        return stdin, stdout, stderr

sshClient = sshClient("172.16.17.51",22,"root","zxy")
# 执行命令
# sshClient.exec("echo 'exec' > /exec.text")
stdin, stdout, stderr = sshClient.exec("tail /exec.text")
# stdin  标准格式的输入，是一个写权限的文件对象
# stdout 标准格式的输出，是一个读权限的文件对象
# stderr 标准格式的错误，是一个写权限的文件对象
print(stdout.read().decode())
ssh.close()
