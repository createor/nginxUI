#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:2022/05/12
# desc:设置nginx限速
from flask import Blueprint
from .header import getResp

limit_rate = Blueprint("limitRate", __name__)

@limit_rate.route("/api/v1/nginx/config/limit_rate",methods=['POST'])
def nginxLimitRate():
    # 操作类型:0--创建操作,1--更新操作,2--删除操作
    operateType = "0"
    if operateType == "0":
        pass
    elif operateType == "1":
        pass
    elif operateType == "2":
        pass
    else:
        pass

    return ""