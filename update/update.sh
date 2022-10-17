#!/bin/bash
# date:2022/05/12
# desc:此脚本用于升级nginx时编译新版本nginx源码
# usage:sh update.sh nginx-xxx.tar.gz

if [ ! -n $1 ];then
  echo "ERROR:请选择更新文件"
  echo "USAGE:sh update.sh nginx-xxx.tar.gz"
  exit
fi

# 判断操作是否执行成功
function isSucc {
  if [ $(echo $?) -eq 0 ];then
    echo "INFO:执行成功"
  else
    echo "ERROR:执行失败,退出操作"
    exit
  fi
}

# 获取当前服务路径
BASE_DIR=$(pwd)
# 文件路径
FILE=${BASE_DIR}/$1
echo "INFO:正在解压文件"
tar -zcvf ${FILE} -C ${BASE_DIR}/nginx-update >>/dev/null
isSucc
# 进入解压后文件夹
cd ${BASE_DIR}/nginx-update
# 编译
echo "INFO:正在编译文件"
./configure xxx