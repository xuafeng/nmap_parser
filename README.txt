# 20140825--fengxuan

# 调用nmap -sV -O -T4 -d ip -oX output.xml扫描某IP段

# 该程序用来从Namp扫描结果中解析出相应的设备

# 使用示例：python test.py result.xml "HIK JYD-E9201/X";可以从扫描结果识别相应设备并打印出IP

# 该代码还可以识别服务等其他项，可以很好的解析Nmap扫描结果。
