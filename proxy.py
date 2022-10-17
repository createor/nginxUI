#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:2022/05/12
# desc:设置nginx代理
from flask import Blueprint

proxy = Blueprint("proxy", __name__)

@proxy.route("/api/v1/nginx/config/proxy",methods=["POST"])
def nginxProxy():
    # 代理类型:0--正向代理,1--反向代理
    proxyType = "0"
    # 操作类型:0--创建操作,1--更新操作,2--删除操作
    operateType = "0"
    if proxyType == "0":
        pass
    elif proxyType == "1":
        pass
    else:
        pass
    return ""