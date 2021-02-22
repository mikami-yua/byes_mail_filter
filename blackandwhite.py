# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:53:30 2019

@author: Mr.Jia
"""

import mail
import email
import get_mail

black_list=[]
white_list=[]

def get_black_list():
    return black_list

def black_name(path):
    global black_list
    mail_path=path
    fp = open(mail_path, "r")
    mssg = email.message_from_file(fp)
    bname=mail.get_from(mssg)
    if bname in black_list:
        print('这封邮件由黑名单中的用户',bname,'发送')
        return True
    else:
        return False


def add_black(path) :
    global black_list
    mail_path=path
    fp = open(mail_path, "r")
    mssg = email.message_from_file(fp)
    bname=mail.get_from(mssg)
    black_list.append(bname)
    black_list=list(set(black_list))
    print('已更新黑名单')

def add_black1() :
    global black_list
    bname=get_mail.get_from()
    black_list.append(bname)
    black_list=list(set(black_list))
    print('已更新黑名单')


   

def get_white_list():
    return black_list

def white_name(path):
    global white_list
    mail_path=path
    fp = open(mail_path, "r")
    mssg = email.message_from_file(fp)
    wname=mail.get_from(mssg)
    if wname in black_list:
        print('这封邮件由白名单中的用户',wname,'发送')
        return True
    else:
        return False


def add_white(path) :
    global white_list
    mail_path=path
    fp = open(mail_path, "r")
    mssg = email.message_from_file(fp)
    wname=mail.get_from(mssg)
    white_list.append(wname)
    white_list=list(set(white_list))
    print('已更新白名单')
    
def add_white1() :
    global white_list
    wname=get_mail.get_from()
    white_list.append(wname)
    white_list=list(set(white_list))
    print('已更新白名单')