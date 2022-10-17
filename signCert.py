#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:2022/05/12
# desc:生成ssl证书
# 参考:https://blog.csdn.net/weixin_40292043/article/details/122698756
import os
import OpenSSL
from datetime import datetime,timedelta
from cryptography.hazmat.primitives import serialization

SSL_PATH=''
def createSSL(data,cert_name='xx.cert',key_name='xx.key'):
    '''
    参数:data--dict(json数据),创建证书的必要信息
        cert_name--cert文件名称
        key_name--key文件名称
    '''
    assert isinstance(data, dict)
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import rsa
    # 私钥
    pkey = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    # 使用者信息
    subject = x509.Name([
        # 组织名称
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, data["organization_name"]),
        # 域名或IP
        x509.NameAttribute(NameOID.COMMON_NAME, data["common_name"]),
        # 国家
        x509.NameAttribute(NameOID.COUNTRY_NAME, data["country_name"])
    ])
    # 颁发者信息
    issuer = x509.Name([
        # 组织名称
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, data["organization_name"]),
        # 域名或IP
        x509.NameAttribute(NameOID.COMMON_NAME, data["common_name"]),
        # 国家
        x509.NameAttribute(NameOID.COUNTRY_NAME, data["country_name"])
    ])
    # 私钥签名
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(pkey.public_key())
        .serial_number(x509.random_serial_number())
        # 开始时间
        .not_valid_before(datetime.utcnow() + timedelta())
        # 结束时间,默认1年
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .sign(pkey, hashes.SHA256(), default_backend())
    )
    # 将证书转换为pem格式
    cert_text = cert.public_bytes(serialization.Encoding.PEM)
    # 写入文件
    with open(os.path.join(SSL_PATH,cert_name), mode='wb') as cert_file:
        cert_file.write(cert_text)
    # 将私钥转换为pem格式
    pkey_text = pkey.private_bytes(
        encoding=serialization.Encoding.PEM, 
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
        )
    # 写入文件
    with open(os.path.join(SSL_PATH,key_name), mode='wb') as pkey_file:
        pkey_file.write(pkey_text)