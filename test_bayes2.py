# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:21:27 2019

@author: Mr.Jia
"""

import bayesfilter
import mail
import email
import spam_dict
import ham_dict
import blackandwhite
import os
pdd=[]#两种bayes判断不同的
pdd1=[]#判断结果1
pdd2=[]#判断结果2
pdd3=[]#判断失误的
pdd4={}#分析垃圾失误的原因
pdd5={}#分析垃圾失误的原因
print('欢迎使用垃圾邮件分类系统')
print('输入1 进入系统 输入0 退出系统')
user_di=input()
while int(user_di)==1:
    spdict={}
    hadict={}
    count=0
    spdict=spam_dict.spam_dict1()
    hadict=ham_dict.ham_dict1()
    ############################################################################
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
            mail_path=bayesfilter.this_mail()#mail_path中存放当前待测试邮件的路径
            p2=bayesfilter.bayes(mail_dict,spdict,hadict)
            mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
        
            p=bayesfilter.bayes2(mail_dict2,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
            if (p>0.9 and p2==True) or (p<0.9 and p2!=True):
                pdd2.append(i)
                pdd2.append(p2)
                pdd2.append(p)
            
            ####################################################################
            #part1 bayes2效果最好
            #part2&part3 bayes1效果好
            '''
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
            '''
            
            if (p>0.9 and p2!=True) :
                testdict6[i]=1
            if p<0.9 and p2==True:
                testdict6[i]=0
            if (p>0.9 and p2==True) or (p<0.9 and p2!=True):
                testdict6[i]=2
                
            
            
           ########################################################################
            '''
            if p2!=True:#p>0.9 p2==False
               testdict6[i]=1
               
            else:
               testdict6[i]=0
            ''' 
            
            '''
            if  int(i)<1000 and testdict6[i]==1:
                pdd3.append(i)
                #pdd3.append(p)
                pdd3.append(p2)
        '''
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
            mail_path=bayesfilter.this_mail()#mail_path中存放当前待测试邮件的路径
            mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
            p2=bayesfilter.bayes(mail_dict,spdict,hadict)
            p=bayesfilter.bayes2(mail_dict2,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
            ############################################################分析为什么这么多垃圾找不到
            if p2==True:
                pdd4[i]=p2
            if p<=0.9:
                pdd5[i]=p
            
            ############################################################
            if (p>0.9 and p2==True) or (p<0.9 and p2!=True):
                pdd2.append(i)
                pdd2.append(p2)
                pdd2.append(p)
           
            
            
            
            if (p>0.9 and p2!=True) :
                testdict6[i]=1
            if p<0.9 and p2==True:
                testdict6[i]=0
            if (p>0.9 and p2==True) or (p<0.9 and p2!=True):
                testdict6[i]=2
            
            
            ##########################################################################
            '''
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
            '''
            ########################################################################
            '''
            if p2!=True:#p>0.9 p2==False
               testdict6[i]=1
             
            else:
               testdict6[i]=0
            '''   
            
            '''
            if  int(i)>1000 and testdict6[i]==0:
                pdd3.append(i)
                #pdd3.append(p)
                pdd3.append(p2)
        '''
        
     
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
    
    
    print(rightCount)
    print(errorCount)
    print(rt)
    print(count)
    print(rightCount/count)
   
    
    
    
    for name ,catagory in testdict6.items():
        if catagory==2:
            print(name)
            
    #print(pdd)
    #print(pdd3)
    #print(len(pdd3))
    #print(pdd1)
    #print(pdd2)
    #print(pdd4)
    #print(pdd5)
    
    user_di=0
        ###################################################################################################
       
        
        
        
'''        
        ################################################################################################
        print('*'*30)
        print('是否展示这封邮件？1 展示   0 不看了')
        user_show=input()
        
    
        
        if int(user_show)==1:
            fp = open(mail_path, "r")
            msg = email.message_from_file(fp)
            print('发件人',mail.get_from(msg))
            print('收件人',mail.get_to(msg))
            print('内容:')
            print(mail.get_txt(msg))
        
        
        #黑白名单板块
        if flag==False:
            print('是否将发件人加入黑名单------加入后将不在收到来自他/她的来信--------1 加入 0 算了')
            user_black=input()
            if int(user_black)==1:
                new_black=mail.get_from(msg)
                blackandwhite.add_black(mail_path)
                print('打印当前黑名单用户：')
                print(blackandwhite.black_list)
            else:
                print('利用现有训练集继续判断')
                print('同意-1 不同意-0')
                user_in=input()
                if int(user_in)==0:
                    num=spam_dict.spamdict_count(spdict)
                    print('当前的sum words：',num)
                    spdict=spam_dict.add_spamdict(spdict,mail_path)
                    print('已添加新的字典到学习字典中')
                    num=spam_dict.spamdict_count(spdict)
                    print('当前的sum words：',num)
        else:
            print('是否将发件人加入白名单------以后收到他/她的来信将不再判断--------1 加入 0 算了')
            user_white=input()
            if int(user_white)==1:
                new_white=mail.get_from(msg)
                blackandwhite.add_white(mail_path)
                print('打印当前白名单用户：')
                print(blackandwhite.white_list)
                
            else:
                print('不将这封邮件添加到训练集')
                print('同意-1 不同意-0')
                user_in=input()
                if int(user_in)==0:
                    num=ham_dict.hamdict_count(hadict)
                    print('当前的sum words：',num)
                    hadict=ham_dict.add_hamdict(hadict,mail_path)
                    print('已添加新的字典到学习字典中')
                    num=ham_dict.hamdict_count(hadict)
                    print('当前的sum words：',num)
        print('继续使用输入1 退出输入0')
        user_di=input()
        
        
        
    print('继续使用输入1 退出输入0')
    user_di=input()

print('正在清空黑白名单...')
blackandwhite.black_list=[]
blackandwhite.white_list=[]
print('谢谢使用！')
'''  