# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:04:10 2019

@author: Mr.Jia
"""
import jieba
import os
import re
import mail
import bayesfilter

def bool_number(number_str):#判断数字是否是小数
    float_number = number_str

    value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')       # 定义正则表达式
    result = value.match(float_number)
    if result:
        return True
    if number_str.isdigit():
        return True
    else:
        return False
    
    
def alpha(alpha_num):#去除过长或过短的数字英文字符串
    if alpha_num.isalnum() and len(alpha_num)>10:
        return True
    if alpha_num.isalnum() and len(alpha_num)<=2:
        return True
    else:
        return False


        
def filter_words(words):#过滤规则2.1--过滤制表符 整数 小数 超过长短规定的alnum
    if words.isdigit():
        return False
    #if words=='\t' or words=='\n' or words==' ':
      #  return False
    if bool_number(words):
        return False
    if bool_chinese(words):
        return True
    if alpha(words):
        return False
    else:
        return True
        


def get_diction(word_list):###list转词典的函数
    long=len(word_list)
    num_list0=['0']*long
    diction=dict(zip(word_list,num_list0))
    return diction



def bool_chinese(words):
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')   #检查非中文
    contents = words
    match = zhmodel.search(contents)
    if match:
        return True
    else:
        return False
    
def add_spam_dict(time_str,dict0):
    
    pathDir = os.listdir("test-spam")
    for s in pathDir:
        new_dir=os.path.join("test-spam",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0    
##############################################################################
def add_spam_dict_1(dict0):
    
    pathDir = os.listdir("test-spam-1")
    for s in pathDir:
        new_dir=os.path.join("test-spam-1",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():######################待加入过滤规则
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0 


def add_spam_dict_3(dict0):
    
    pathDir = os.listdir("test-spam-3")
    for s in pathDir:
        new_dir=os.path.join("test-spam-3",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():######################待加入过滤规则
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0 





##############################################################################
def add_ham_dict(time_str,dict0):
    
    pathDir = os.listdir("test-ham")
    for s in pathDir:
        new_dir=os.path.join("test-ham",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0    

########################################################
def add_ham_dict_1(dict0):
    
    pathDir = os.listdir("test-ham-1")
    for s in pathDir:
        new_dir=os.path.join("test-ham-1",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0    

def add_ham_dict_3(dict0):
    
    pathDir = os.listdir("test-ham-3")
    for s in pathDir:
        new_dir=os.path.join("test-ham-3",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                dict_word=mail.mail_api(f)
                time_str=list(jieba.cut(dict_word))
                for i in time_str:
                    if i in dict0.keys():
                        dict0[i]=int(dict0[i])+1
                pass
    return dict0  
###########################################################
def get_stop_list():#得停用词词表
    stop_list=[]
    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
    return stop_list

#############################################################计算正确率
def account_right(spdict,hadict):
    if len(spdict)==0 or len(hadict)==0:
        say='没有训练集不能计算准确度！'
        return say
    
    
    count=0
    pdd3=[]
    testdict6={}
    path3='C:\\迅雷下载\\test-mail'
    for i in range(1,201):
        test_num=i
        test_num=str(test_num)
        test_list=[path3,'\\',test_num]
        test_path=''
        test_path=test_path.join(test_list)
        if os.path.isfile(test_path):
            filename = os.path.basename(test_path)
            testdict6[filename]=0
            count=count+1
    #############################################################################     
    #mail_dict=bayesfilter.count_words()
            mail_dict=bayesfilter.count_words(i)
            #mail_path=bayesfilter.this_mail()#mail_path中存放当前待测试邮件的路径
            p2=bayesfilter.bayes(mail_dict,spdict,hadict)
            mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
        
            p=bayesfilter.bayes2(mail_dict2,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
            
            
            if len(hadict)<10000:
                if p>0.9:
                    testdict6[i]=1
                else:
                    testdict6[i]=0 
            if len(hadict)>10000:
                if p2!=True:
                    testdict6[i]=1
                else:
                    testdict6[i]=0
               
            if  int(i)<1000 and testdict6[i]==1:
                pdd3.append(i)
                pdd3.append(p)
                pdd3.append(p2)
        
        #################################################################################################
    for i in range(7801,8001):
        test_num=i
        test_num=str(test_num)
        test_list=[path3,'\\',test_num]
        test_path=''
        test_path=test_path.join(test_list)
        filename = os.path.basename(test_path)
        if os.path.isfile(test_path):
            testdict6[filename]=0
            count=count+1
    #############################################################################     
    #mail_dict=bayesfilter.count_words()
            mail_dict=bayesfilter.count_words(i)
            #mail_path=bayesfilter.this_mail()#mail_path中存放当前待测试邮件的路径
            mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
            p2=bayesfilter.bayes(mail_dict,spdict,hadict)
            p=bayesfilter.bayes2(mail_dict2,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
            ############################################################分析为什么这么多垃圾找不到
            if len(hadict)<10000:
                if p>0.9:
                    testdict6[i]=1
                else:
                    testdict6[i]=0 
            if len(hadict)>10000:
                if p2!=True:
                    testdict6[i]=1
                else:
                    testdict6[i]=0
               
            if  int(i)>1000 and testdict6[i]==0:
                pdd3.append(i)
                pdd3.append(p)
                pdd3.append(p2)    
    rightCount=0
    errorCount=0
    for i in range(1,201):
        test_num=i
        test_num=str(test_num)
        test_list=[path3,'\\',test_num]
        test_path=''
        test_path=test_path.join(test_list)
        if os.path.isfile(test_path):
            if testdict6[i]==1:
                errorCount+=1
            if testdict6[i]==0:
                rightCount+=1
    for i in range(7801,8001):
        test_num=i
        test_num=str(test_num)
        test_list=[path3,'\\',test_num]
        test_path=''
        test_path=test_path.join(test_list)
        if os.path.isfile(test_path):
            if testdict6[i]==0:
                errorCount+=1
            if testdict6[i]==1:
                rightCount+=1
        
    rt=rightCount/(rightCount+errorCount)
    #print(pdd3)
    return rt









