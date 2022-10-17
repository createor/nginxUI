#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:2022/05/12
# desc:设置服务端头部
from flask import make_response

def getResp(status,data):
    '''
    参数:status--状态码
         data--响应信息
    '''
    response = make_response(data)
    response.status = status
    response.headers["server"] = "*"
    return response