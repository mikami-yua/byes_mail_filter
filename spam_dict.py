# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:12:48 2019

@author: Mr.Jia
"""
import jieba
import os
import func
import mail
import bayesfilter


    
    
    
    

def spam_dict1():
    spam_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-spam")
    for s in pathDir:
        new_dir=os.path.join("test-spam",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) : #如果是文件
            
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                #strg=f.read()
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        spam_word_list.append(i)
                pass

    spam_word_list=list(set(spam_word_list))#去重复
    spam_word_list.sort()#排序
    spam_word_dict0=func.get_diction(spam_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    spam_word_dict=func.add_spam_dict(spam_word_list,spam_word_dict0)#将词频添加到字典中
    spam_word_dict=dict(sorted(spam_word_dict0.items(),key=lambda x:x[1],reverse=True))
    
    file=open('spam_dict_all.txt','w') 
    file.write(str(spam_word_dict))
    file.close()
    print('spam diction set up!')
    print('sum words = ',spamdict_count(spam_word_dict))
    
    return spam_word_dict


#######################################################################################
def spam_dict1_1():
    spam_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-spam-1")
    for s in pathDir:
        new_dir=os.path.join("test-spam-1",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) : #如果是文件
            
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                #strg=f.read()
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        spam_word_list.append(i)
                pass

    spam_word_list=list(set(spam_word_list))#去重复
    spam_word_list.sort()#排序
    spam_word_dict0=func.get_diction(spam_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    spam_word_dict=func.add_spam_dict_1(spam_word_dict0)#将词频添加到字典中
    spam_word_dict=dict(sorted(spam_word_dict0.items(),key=lambda x:x[1],reverse=True))
    
    file=open('spam_dict_1-1.txt','w') 
    file.write(str(spam_word_dict))
    file.close()
    print('spam diction set up!')
    print('sum words = ',spamdict_count(spam_word_dict))
    
    return spam_word_dict

def spam_dict1_3():
    spam_word_list=[]
    stop_list=[]

    for line in open ("中文停用词表.txt"):
        stop_list.append(line[:len(line)-1])
        #print(len(stop_list))#打印停用词表长度
    pathDir = os.listdir("test-spam-3")
    for s in pathDir:
        new_dir=os.path.join("test-spam-3",s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(new_dir) : #如果是文件
            
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                #strg=f.read()
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        spam_word_list.append(i)
                pass

    spam_word_list=list(set(spam_word_list))#去重复
    spam_word_list.sort()#排序
    spam_word_dict0=func.get_diction(spam_word_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    spam_word_dict=func.add_spam_dict_3(spam_word_dict0)#将词频添加到字典中
    spam_word_dict=dict(sorted(spam_word_dict0.items(),key=lambda x:x[1],reverse=True))
    
    file=open('spam_dict_1-3.txt','w') 
    file.write(str(spam_word_dict))
    file.close()
    print('spam diction set up!')
    print('sum words = ',spamdict_count(spam_word_dict))
    
    return spam_word_dict

##########################################################################################
 
def spamdict_count(dic1):#统计词典的单词总数
    
     num=0
     for key in dic1:
         num=num+int(dic1[key])
        
     return num
    



def add_spamdict(spamdict,mailpath):
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
    new_spamdict={}
    for key in spamdict:
        if maildict.get(key):
            new_spamdict[key]=spamdict[key]+maildict[key]
        else:
            new_spamdict[key]=spamdict[key]
    for key in maildict:
        if spamdict.get(key):
            pass
        else:
            new_spamdict[key]=maildict[key]
            
    return new_spamdict
            
import get_mail
def add_spamdict1(spamdict):
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
    new_spamdict={}
    for key in spamdict:
        if maildict.get(key):
            new_spamdict[key]=spamdict[key]+maildict[key]
        else:
            new_spamdict[key]=spamdict[key]
    for key in maildict:
        if spamdict.get(key):
            pass
        else:
            new_spamdict[key]=maildict[key]
            
    return new_spamdict






