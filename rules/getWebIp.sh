#!/bin/bash
# 获取nginx的access.log的日志中访问IP，将结果输出到visit_ip临时文件中
# 参数:$1 开始时间,$2 结束时间

# 日志路径
LOG_PATH=''
# 时间，默认5分钟
TIME=5
if [ ! -n $1 ];then
  START=$(date +)
else
  START=$1
fi
if [ ! -n $2 ];then
  END=$(date +)
else
  END=$2
fi
# ip,状态码
cat /var/log/nginx/access.log | awk '{if($9!="\"-\"") {print $1,$9}}'
