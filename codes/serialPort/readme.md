##### 功能
###### 1. 构造方法，前面三个必填    port, baurate , deviceName ,serialPortDataListener ,checkSepTime
###### 2. 消息读取基于回调方法  ,串口消息可能会粘包、半包
|类型|功能|
|:-|:-|
|NormalDataListener|用于接收以换行和回车的消息监听类|
|FixLengthDataListener|用于接收固定长度的消息监听类|
|MessageListener|用于接收指定byte结尾的消息监听类|
###### 3. 连接状态监控  默认5秒检查一次连接状态和DSR(对方连接是否正常)，并触发对应的回调
|类型|功能|
|:-|:-|
|isConnected|串口是否连接|
|isDsr|对方是否连接|
|conncetSuccess|连接成功|
|conncetFail|连接成功|
|dsrSuccess|dsr成功|
|dsrFail|dsr成功|
