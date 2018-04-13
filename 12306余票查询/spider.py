#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 钟洪 time:2017/9/13
import urllib2
import ssl
import json
from cones import station_list,seatnumber,m
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ssl._create_default_https_context = ssl._create_unverified_context

train_date = raw_input('请输入乘车日期（如：2017-09-25）:')
from_station = station_list[raw_input('请输入出发地（如：南昌）:')]
to_station = station_list[raw_input('请输入目的地（如：瑞金）:')]
start = raw_input('请输入你要查询的座次（如：硬卧，硬座,一等座）：')
number = int(seatnumber[start])

def getlist():
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&lef'
                          'tTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'
                          % (train_date,from_station,to_station))
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    req.add_header('Cookie','JSESSIONID=C8BBFF7F6535F378235860A44479200F; fp_ver=4.5.1; RAIL_EXPIRATION='
                            '1506117084959; RAIL_DEVICEID=Kz1cIGgHXdGHTUAttL6sdRa8EaN3UApOcOBUGK-emznw7jxJ'
                            'XCPpyRT_-CGxziAZGustylqGbW9LdY3pijXFFqPAxo1tOKXd_AYclRam-SFod_Ak-MX7ou-5EX0Jl-A'
                            'xSa3N8M3Ogfr7lbnzXrcuxMkGYN-mpVo2; route=495c805987d0f5c8c84b14f60212447d; BIGi'
                            'pServerotn=1910046986.64545.0000; _jc_save_fromStation=%u5357%u660C%2CNCG; _jc_'
                            'save_toStation=%u676D%u5DDE%2CHZH; _jc_save_fromDate=2017-10-02; _jc_save_toDate'
                            '=2017-09-20; _jc_save_wfdc_flag=dc')
    html = urllib2.urlopen(req).read()
    dict = json.loads(html)
    return dict['data']['result']

def check():
    for i in getlist():
        temp_list = i.split('|')
        if (temp_list[28] == u'无' or temp_list[28] == '') and (temp_list[29] == u'无' or temp_list[29] == '')and \
                (temp_list[30] == u'无' or temp_list[30] == '') and (temp_list[31] == u'无' or temp_list[31] == '')\
                and (temp_list[32] == u'无' or temp_list[32] == '') and \
                (temp_list[21] == u'无' or temp_list[21] == '') and (temp_list[23] == u'无' or temp_list[23] == ''):
            print '\n车次:%s 无票，已售空!'% temp_list[3]
        elif temp_list[number] == u'有' or temp_list[number] > 0:
            print '\n有票\n车次:%s\n出发地:%s\n目的地:%s\n出发时间:%s\n达到时间:%s\n历时:%s\n出发日期:%s'\
                    %(temp_list[3],m[temp_list[6]],m[temp_list[7]],temp_list[8],temp_list[9],temp_list[10],temp_list[13])
        else:
            print '该座次已售空，请选择其他座次！'


if __name__ == '__main__':
    getlist()
    check()
