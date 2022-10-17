#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:2022/05/12
# desc:nginx服务操作
import os
import subprocess

def operate(type):
    try:
        # 启动nginx
        if type == "start":
            cmd = 'service nginx start'
        # 停止nginx
        elif type == "stop":
            cmd = 'service nginx stop'
        # 重启nginx
        elif type == "restart":
            cmd = 'service nginx restart'
        # 重载nginx
        elif type == "reload":
            cmd = 'service nginx reload'
        # 检查配置文件
        elif type == "check":
            cmd = '/usr/bin/nginx -t'
        else:
            pass
        result = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE,STDOUT=subprocess.PIPE)
        if result.returncode !=0:
            return result.stderr
        return result.stdout
    except Exception as e:
        pass

def getInfo():
    '''
    获取服务器信息:主机名、IP等
    '''
    return ""