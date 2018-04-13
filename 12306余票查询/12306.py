#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhonghong time:2017/8/24
import urllib2
import urllib
import ssl
import cookielib
import json

c = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)

ssl._create_default_https_context = ssl._create_unverified_context


#为URL添加头部信息和途径
def geturl(url='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4478772662477484'):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    req.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
    return req

#下载验证码图片
def downloadcode(req=geturl()):
    codeing = opener.open(req).read()
    with open('C:/Users/17895/Pictures/Camera Roll/code.png','wb') as f:
        f.write(codeing)

#验证验证码
def provecode(req='https://kyfw.12306.cn/passport/captcha/captcha-check'):
    code = raw_input('>>>>>>')
    data = {
               'answer':code,
               'login_site':'E',
               'rand':'sjrand'
    }
    data = urllib.urlencode(data)
    geturl(req)
    html = opener.open(req,data=data).read()
    print html

#实现登录
def Login(req='https://kyfw.12306.cn/passport/web/login'):
    data = {
        'username':'15579872216',
        'password':'970815thl',
        'appid':'otn'
    }
    data = urllib.urlencode(data)
    geturl(req)
    html = opener.open(req,data=data).read()
    print html


if __name__ == '__main__':
    geturl()
    downloadcode()
    provecode()
    Login()



