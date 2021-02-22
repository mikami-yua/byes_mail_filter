# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:52:46 2019

@author: Mr.Jia
"""




malist=[]
banlist=[]
####################################
#贝叶斯的实现函数
def bayes(worddict,spamdict,hamdict):#此处的worddict应为词频前15个单词的dict
    
    #首先对垃圾邮件进行处理
    dict0={}
    dict1={}
    for key in worddict:
        if key in spamdict:
            #print(key,spamdict[key])
            dict0[key]=spamdict[key]
        else:
            #print(key,'1')
            dict0[key]=1
    #print('$'*20)       
    for key in worddict:
        if key in hamdict:
            #print(key,hamdict[key])
            dict1[key]=hamdict[key]
        else:
            #print(key,'1')
            dict1[key]=1
    #得到前15个词在单词表中的词频        
    #计算两个词典的单词总数
    spam_num=spam_dict.spamdict_count(spamdict)
    ham_num=ham_dict.hamdict_count(hamdict)
    print(ham_num)
    if int(ham_num)<10000:
        prob=0.42
    if int(ham_num)>630000:
        prob=0.476
    if ham_num>10000  and ham_num<500000:
        prob=0.479
    
    #print(spam_num,ham_num)
    #print(dict0,dict1)
    #两个num中存放两个字典的总字数，dict0中存放spam的前15个
    p1dict={}
    p2dict={}
    for key in dict0:
        p1dict[key]=dict0[key]/spam_num
    #print(p1dict)
    for key in dict1:
        p2dict[key]=dict1[key]/ham_num
    #print(p2dict)
    p1=0
    p2=0
    for key in p1dict:
        p1=p1+math.log(p1dict[key])
    #print(p1)
    for key in p2dict:
        p2=p2+math.log(p2dict[key])
    #print(p2)
    print(prob)
    p1=(math.e**p1)*prob
    p2=(math.e**p2)*(1-prob)
    print('两种情况的概率分别为：')
    print(p1,p2)
    print('判断结论：')
    if len(worddict)<15:
        print('这封邮件过短，是可疑邮件')
        say='这封邮件过短，是可疑邮件'
        return say#####################################################################可以再想想

    
    if p1>p2:
        print('是垃圾邮件！')
        print(' ')
        return False
    else:
        print('非垃圾邮件')
        print(' ')
        return True
    
###########################################################
#贝叶斯方式2  已概率方式计算 word——dict spam-dict ham-dict
        
    
    
    
    
    

def get_probdict(worddict,spamdict,hamdict):
    wordprobdict={}
    for word,num in worddict.items():
            
            if word in spamdict.keys() and word in hamdict.keys():
                #该文件中包含词个数
                pw_s=spamdict[word]/spam_dict.spamdict_count(spamdict)
                pw_n=hamdict[word]/ham_dict.hamdict_count(hamdict)
                ps_w=pw_s/(pw_s+pw_n) 
                wordprobdict[word]=ps_w
            if word in spamdict.keys() and word not in hamdict.keys():
                pw_s=spamdict[word]/spam_dict.spamdict_count(spamdict)
                pw_n=2.0409797330712506e-05
                
                ps_w=pw_s/(pw_s+pw_n) 
                wordprobdict[word]=ps_w
            if word not in spamdict.keys() and word in hamdict.keys():
                pw_s=4.517012197187658e-05
                
                pw_n=hamdict[word]/ham_dict.hamdict_count(hamdict)
                ps_w=pw_s/(pw_s+pw_n) 
                wordprobdict[word]=ps_w
            if word not in spamdict.keys() and word not in hamdict.keys():
                ps_w=0.44419625422613#若该词不在脏词词典中，概率设为0.4
                
                wordprobdict[word]=ps_w
                
            #print(word,' ',ps_w)
            #print(pw_s,pw_n)
            #print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    
    #print(wordprobdict)
    return wordprobdict
def bayes2(wordprobdict,spamdict,hamdict):
     
    ps_w=1
    ps_n=1
         
    for word,prob in wordprobdict.items() :
            #print(word+"/"+str(prob))
            ps_w=ps_w*wordprobdict[word]
            ps_n=ps_n*(1-wordprobdict[word])
    #print(ps_w,ps_n)
    p=ps_w/(ps_w+ps_n)
#           print(str(ps_w)+"////"+str(ps_n))
    #print(p)    
    return p  




##########################################################
#词频排列统计函数
import os
import jieba
import func
import spam_dict
import ham_dict
import math
import count
import mail
import get_mail


this_path=' '

def count_words(num3):#对测试邮件的字频统计，并按降序输出key值的dict
    global this_path  
    mail_num=str(num3)
    stop_list=func.get_stop_list()
    mail_list=[]
    new_dir=count.get_path(mail_num)
    if os.path.isfile(new_dir) :         #如果是文件
            with open(new_dir,"r") as f:
                strg=mail.mail_api(f)
                this_path=new_dir
                temp_list=list(jieba.cut(strg))
                #print(len(temp_list))#打印邮件长度
                for i in temp_list:
                    if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
                        mail_list.append(i)
    else:
        return False
                
    ###########得到maillist
    global malist
    malist=mail_list
    
            
    
    
   
    
    #mail_list=list(set(mail_list))#去重复
    #print(mail_list)
    #mail_list.sort()#排序
    mail_dict0=func.get_diction(mail_list)#初始化字典
    #long1=len(spam_word_dict0)#获得字典长度
    #将词频添加到字典
    if os.path.isfile(new_dir) :         
        with open(new_dir,"r") as f:
               dict_word=mail.mail_api(f)
               time_str=list(jieba.cut(dict_word))
               for i in time_str:
                   if i in mail_dict0.keys():
                       mail_dict0[i]=int(mail_dict0[i])+1
                  
    count_mail_dict=dict(sorted(mail_dict0.items(),key=lambda x:x[1],reverse=True))
    #return count_mail_dict
    
        
    #print(count_mail_dict)#打印按value从大到小排序的字典
    cnt = 0 
    dict1={}
    for key, value in count_mail_dict.items():
        cnt += 1
        dict1[key]=value
        if cnt > 15:
            break
    #print(dict1)#打印前15词频的字典
    top_mail_dict=dict1
    return top_mail_dict


#################
def count_words1():#对测试邮件的字频统计，并按降序输出key值的dict
    stop_list=func.get_stop_list()
    mail_list=[]
    strg=get_mail.get_content()
    temp_list=list(jieba.cut(strg))
    for i in temp_list:
        if (i not in stop_list) and i.strip()!='' and func.filter_words(i):
            mail_list.append(i)
   
    global malist
    malist=mail_list
  
    mail_dict0=func.get_diction(mail_list)#初始化字典
    dict_word=get_mail.get_content()
    time_str=list(jieba.cut(dict_word))
    for i in time_str:
        if i in mail_dict0.keys():
            mail_dict0[i]=int(mail_dict0[i])+1
                  
    count_mail_dict=dict(sorted(mail_dict0.items(),key=lambda x:x[1],reverse=True))
    cnt = 0 
    dict1={}
    for key, value in count_mail_dict.items():
        cnt += 1
        dict1[key]=value
        if cnt > 15:
            break
    #print(dict1)#打印前15词频的字典
    top_mail_dict=dict1
    return top_mail_dict    

###################
















def this_mail():
    global this_path
    return this_path
    

    
        
        


    


   
def ban(banlist):
    global malist
    mlist=malist
    blist=banlist
    
    if list(set(mlist).intersection(set(blist))):
        return True
    else:
        return False
        
    

































































