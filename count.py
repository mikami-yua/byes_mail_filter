# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:56:39 2019

@author: Mr.Jia
"""
###############################处理处理路径函数，得到各个路径后调用相应函数
import os

'''
def get_path(choose):##处理处理路径函数，得到各个路径后调用相应函数
    path1='C:\\迅雷下载\\test-spam'
    path2='C:\\迅雷下载\\test-ham'
    path3='C:\\迅雷下载\\test-mail'
    if choose==1:
        return path1
    if choose==2:
        return path2
    else:
        print('请输入希望测试的邮件号：')
        test_num=input()
        print('待测试邮件为',test_num,'号邮件！')
        test_list=[path3,'\\',test_num]
        test_path=''
        test_path=test_path.join(test_list)
        return test_path
'''       

        
def get_path(choose):##处理处理路径函数，得到各个路径后调用相应函数
    
    path3='C:\\迅雷下载\\test-mail'
    test_num=choose
    print('待测试邮件为',test_num,'号邮件！')
    test_list=[path3,'\\',test_num]
    test_path=''
    test_path=test_path.join(test_list)
    return test_path
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    