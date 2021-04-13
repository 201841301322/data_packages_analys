http是明文传输的，所以通过数据包的十六进制转换可以得到明文内容
可以用tcpdump抓包进
tcpdump tcp port 80 and host 192.168.133.4 -c 20000 -w ./target.cap
80即为http传输的主要端口，192.168.133.4为要监听的端口，2000为要抓取的包的个数， ./target.cap为存储路径


抓包分析目标设备是否运行的APP（目前可以抓取 抖音 快手 微信 微博 网易云 酷安 夸克 飞猪旅行 王者荣耀 知乎 拼多多 支付宝 腾讯自选股 百度网盘 优学院 QQ 运动世界校园）

python3 get_app_state.py


抓包分析目标设备的QQ号

python3 get_qq.py
