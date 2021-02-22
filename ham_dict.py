# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:51:50 2019

@author: Mr.Jia
"""

import jieba
import os
import func
import mail

def ham_dict1():
    ham_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-ham")
    for s in pathDir:
        new_dir=os.path.join("test-ham",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        ham_word_list.append(i)
                pass

    ham_word_list=list(set(ham_word_list))#去重复
    ham_word_list.sort()#排序
    ham_word_dict0=func.get_diction(ham_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    ham_word_dict=func.add_ham_dict(ham_word_list,ham_word_dict0)#将词频添加到字典中
    ham_word_dict=dict(sorted(ham_word_dict.items(),key=lambda x:x[1],reverse=True))
    
    file=open('ham_dict_all.txt','w') 
    file.write(str(ham_word_dict))
    file.close()
    print('ham diction set up!')
    print('sum words = ',hamdict_count(ham_word_dict))
    
    return ham_word_dict

###############################################
def ham_dict1_1():
    ham_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-ham-1")
    for s in pathDir:
        new_dir=os.path.join("test-ham-1",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        ham_word_list.append(i)
                pass

    ham_word_list=list(set(ham_word_list))#去重复
    ham_word_list.sort()#排序
    ham_word_dict0=func.get_diction(ham_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    ham_word_dict=func.add_ham_dict_1(ham_word_dict0)#将词频添加到字典中
    ham_word_dict=dict(sorted(ham_word_dict.items(),key=lambda x:x[1],reverse=True))
    
    file=open('ham_dict_1_1.txt','w') 
    file.write(str(ham_word_dict))
    file.close()
    print('ham diction set up!')
    print('sum words = ',hamdict_count(ham_word_dict))
    
    return ham_word_dict
def ham_dict1_3():
    ham_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-ham-3")
    for s in pathDir:
        new_dir=os.path.join("test-ham-3",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        ham_word_list.append(i)
                pass

    ham_word_list=list(set(ham_word_list))#去重复
    ham_word_list.sort()#排序
    ham_word_dict0=func.get_diction(ham_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    ham_word_dict=func.add_ham_dict_3(ham_word_dict0)#将词频添加到字典中
    ham_word_dict=dict(sorted(ham_word_dict.items(),key=lambda x:x[1],reverse=True))
    
    file=open('ham_dict_1_3.txt','w') 
    file.write(str(ham_word_dict))
    file.close()
    print('ham diction set up!')
    print('sum words = ',hamdict_count(ham_word_dict))
    
    return ham_word_dict
###################################################
def hamdict_count(dic1):#统计词典的单词总数
    num=0
    for key in dic1:
        num=num+int(dic1[key])
        
    return num

def add_hamdict(hamdict,mailpath):
    #建立邮件字典
    stop_list=func.get_stop_list()
    mail_list=[]
    if os.path.isfile(mailpath) :         #如果是文件
            with open(mailpath,"r") as f:
                strg=mail.mail_api(f)
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        mail_list.append(i)
                        
    mail_dict0=func.get_diction(mail_list)#初始化字典
    if os.path.isfile(mailpath) :         
        with open(mailpath,"r") as f:
               dict_word=mail.mail_api(f)
               time_str=list(jieba.cut(dict_word))
               for i in time_str:
                   if i in mail_dict0.keys():
                       mail_dict0[i]=int(mail_dict0[i])+1
                  
    maildict=dict(sorted(mail_dict0.items(),key=lambda x:x[1],reverse=True))
    
    

    #合并字典
    new_hamdict={}
    for key in hamdict:
        if maildict.get(key):
            new_hamdict[key]=hamdict[key]+maildict[key]
        else:
            new_hamdict[key]=hamdict[key]
    for key in maildict:
        if hamdict.get(key):
            pass
        else:
            new_hamdict[key]=maildict[key]
            
    return new_hamdict

import get_mail
def add_hamdict1(hamdict):
    #建立邮件字典
    stop_list=func.get_stop_list()
    mail_list=[]
    strg=get_mail.get_content()
    temp_list=list(jieba.cut(strg))
    for i in temp_list:
        if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
            mail_list.append(i)
    mail_dict0=func.get_diction(mail_list)#初始化字典
    dict_word=get_mail.get_content()
    time_str=list(jieba.cut(dict_word))
    for i in time_str:
        if i in mail_dict0.keys():
            mail_dict0[i]=int(mail_dict0[i])+1
                  
    maildict=dict(sorted(mail_dict0.items(),key=lambda x:x[1],reverse=True))
    

    #合并字典
    new_hamdict={}
    for key in hamdict:
        if maildict.get(key):
            new_hamdict[key]=hamdict[key]+maildict[key]
        else:
            new_hamdict[key]=hamdict[key]
    for key in maildict:
        if hamdict.get(key):
            pass
        else:
            new_hamdict[key]=maildict[key]
            
    return new_hamdict
