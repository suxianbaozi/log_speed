# log_speed
用来统计日志的输出速度





## 准备工作
```sudo chmod +x log_speed.py```

```sudo cp log_speed.py /usr/local/bin/log_speed```


## 常见用法



### 统计nginx日志的速度
```tail -f /var/log/nginx/access.log | log_speed```

### 统计nginx日志含有爬虫的输出速度

```tail -f /var/log/nginx/access.log |grep spider |log_speed```
