# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:14:14 2019

@author: Mr.Jia
"""
'''主函数界面'''
import time
import func
import spam_dict
import ham_dict
import bayesfilter
import count
import mail
import email
import blackandwhite
import tkinter as tk
from tkinter import messagebox

spdict={}
hadict={}
ban_words=[]
ban_type1=['公司','有限公司','发票', '增值税','咨询','财务','合作','代开',]
ban_type2=['不要脸','弱智','弟弟']

window = tk.Tk()
window.title('贝叶斯邮件分类系统')
window.geometry('450x300')

tk.Label(window, text='欢迎使用邮件分类系统',font = ('黑体',25)).place(x=60, y= 30)

# user information


    
##########################################################################################################
def start_test():
    
        def start_1():
            
            tk.messagebox.showinfo(title='正在训练请稍后...',message='这可能会需要半分钟，请耐心等候~点击确定开始')
            global spdict
            time_start=time.time()
            spdict=spam_dict.spam_dict1_1()
            spstring1='垃圾邮件字典已建立'
            spstring2='垃圾邮件总字数为：'+ str(spam_dict.spamdict_count(spdict))
            #tk.messagebox.showinfo(title='垃圾邮件训练完成',message=spstring1+' '+spstring2)
            global hadict
            hadict=ham_dict.ham_dict1_1()
            time_end=time.time()
            hastring1='正常邮件字典已建立'
            hastring2='正常邮件总字数为：'+ str(ham_dict.hamdict_count(hadict))
            print('totally cost',time_end-time_start)
            tk.messagebox.showinfo(title='训练完成！',message=hastring1+' '+hastring2 + chr(13)
                                    +spstring1+' '+spstring2)
            
            window_in_test.destroy()
    
    
    
        def start_2():
            tk.messagebox.showinfo(title='正在训练请稍后...',message='这可能会需要半分钟，请耐心等候~点击确定开始')
            global spdict
            time_start=time.time()
            spdict=spam_dict.spam_dict1()
            spstring1='垃圾邮件字典已建立'
            spstring2='垃圾邮件总字数为：'+ str(spam_dict.spamdict_count(spdict))
            
            global hadict
            hadict=ham_dict.ham_dict1()
            time_end=time.time()
            hastring1='正常邮件字典已建立'
            hastring2='正常邮件总字数为：'+ str(ham_dict.hamdict_count(hadict))
            print('totally cost',time_end-time_start)
            tk.messagebox.showinfo(title='训练完成！',message=hastring1+' '+hastring2 + chr(13)
                                    +spstring1+' '+spstring2)
            
            window_in_test.destroy()
        def start_3():
            tk.messagebox.showinfo(title='正在训练请稍后...',message='这可能会需要半分钟，请耐心等候~点击确定开始')
            global spdict
            time_start=time.time()
            spdict=spam_dict.spam_dict1_3()
            spstring1='垃圾邮件字典已建立'
            spstring2='垃圾邮件总字数为：'+ str(spam_dict.spamdict_count(spdict))
            
            global hadict
            hadict=ham_dict.ham_dict1_3()
            time_end=time.time()
            hastring1='正常邮件字典已建立'
            hastring2='正常邮件总字数为：'+ str(ham_dict.hamdict_count(hadict))
            print('totally cost',time_end-time_start)
            tk.messagebox.showinfo(title='训练完成！',message=hastring1+' '+hastring2 + chr(13)
                                    +spstring1+' '+spstring2)
            
            window_in_test.destroy()
         
        window_in_test = tk.Toplevel(window)
        window_in_test.geometry('350x200')
        window_in_test.title('训练器')
        tk.Button(window_in_test, text='初级训练',command=start_1).place(x=155, y=30)#x=100, y=50
        tk.Button(window_in_test, text='中级训练',command=start_2).place(x=155, y=75)#x=100, y=100
        tk.Button(window_in_test, text='高级训练',command=start_3).place(x=155, y=120)#x=100, y=150
        #btn_in_test.place(x=220, y=150)
        
    
    

btn_in_test= tk.Button(window, text='选择训练集进行训练！', command=start_test).place(x=175,y=100)









###############################################################################################################
##屏蔽词系统
##################
def start_ban():
    window_ban = tk.Toplevel(window)
    window_ban.geometry('400x300')
    window_ban.title('屏蔽词选择')
    tk.Label(window_ban, text='每次输入一个词，您将不会再收到包含这个词的任何邮件').place(x=30, y= 30)
    var_words = tk.StringVar()
    var_words.set('在这里输入您想忽视的词')
    entry_words = tk.Entry(window_ban, textvariable=var_words)
    entry_words.place(x=135, y=50)
    
    def ban_words():
        word=var_words.get()
        global ban_words
        ban_words.append(word)
        print(ban_words)
        #bw=bayesfilter.get_banlist(ban_words)
        
        
        
    btn_var_words= tk.Button(window_ban, text='加入', command=ban_words)
    btn_var_words.place(x=180, y=75)
    ###################
    def ba():
        global ban_words
        global ban_type1
        global ban_type2
        if chVarDis1.get()==1 and chVarDis2.get()==1:
            ban_words=ban_type1 + ban_type2
            tk.messagebox.showinfo(title='使用内置敏感词',message='已选择：营销类词语和攻击类词语！')
        if chVarDis1.get()==0 and chVarDis2.get()==1:
            ban_words=ban_type2
            tk.messagebox.showinfo(title='使用内置敏感词',message='已选择：攻击类词语！')
        if  chVarDis1.get()==1 and chVarDis2.get()==0: 
            ban_words=ban_type1
            tk.messagebox.showinfo(title='使用内置敏感词',message='已选择：营销类词语!')
        if chVarDis1.get()==0 and chVarDis2.get()==0:
            tk.messagebox.showinfo(title='使用内置敏感词',message='您未进行任何选择!')
            
    ###################
    
    chVarDis1 = tk.IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
    chVarDis2 = tk.IntVar()
    check1 = tk.Checkbutton(window_ban, text="营销类词语", variable=chVarDis1)
    check1.place(x=160,y=150)
    check2 = tk.Checkbutton(window_ban, text="攻击类词语", variable=chVarDis2)
    check2.place(x=160,y=170)
    btn_check= tk.Button(window_ban, text='使用已有的敏感词表', command=ba)
    btn_check.place(x=160,y=200)

    
    
    
#################$





btn_in_ban= tk.Button(window, text='屏蔽词系统！', command=start_ban)
btn_in_ban.place(x=180, y=180)


    

#################################################################################################################

tk.Label(window, text='输入待测试邮件号: ').place(x=50, y= 220)

var_mail_num = tk.StringVar()
var_mail_num.set('1-200或7801-8000')
entry_mail_num = tk.Entry(window, textvariable=var_mail_num)
entry_mail_num.place(x=170, y=220)

def mail_test():
    global spdict
    global hadict
       
    window_mail = tk.Toplevel(window)
    window_mail.geometry('600x500')
    window_mail.title('贝叶斯判断')
    num1=var_mail_num.get()# .get可以传参
    if len(hadict)==0:
        tk.messagebox.showinfo(title='错误',message='没有进行训练不能判断 '+num1+' 号是否为垃圾邮件'+chr(13)+'请先进行训练~')
        window_mail.destroy()
    tk.Label(window_mail,text='待测试邮件号:'+num1).place(x=30, y=100)
    mail_dict=bayesfilter.count_words(num1)
    if mail_dict==False:
        tk.messagebox.showinfo(title='文件不存在',message='这个邮件不存在，试试别的邮件')
        window_mail.destroy()
        
        
        
        
    tk.Label(window_mail, text='当前邮件的参数',font = ('黑体',25)).place(x=180,y=5)
    #test1=str(mail_dict)这两句显示前15
    #tk.Label(window_mail,text='mail dict'+test1).place(x=30, y=120)
    mail_path=bayesfilter.this_mail()
    fp = open(mail_path, "r")
    msg = email.message_from_file(fp)
    
    
    
    
    
    
    if mail.get_from(msg) in blackandwhite.black_list:
        
        tk.messagebox.showinfo(title='检测到黑名单用户',message='这封邮件由黑名单用户：'+mail.get_from(msg)+'发送')
        window_mail.destroy()
    
    
    
    ############################
    
    def yes_show1():
        
        fp = open(mail_path, "r")
        msg = email.message_from_file(fp)
        tk.Label(window_showmail1,text='发件人：'+ mail.get_from(msg)).place(x=30, y=10)
        tk.Label(window_showmail1,text='收件人：'+ mail.get_to(msg)).place(x=30, y=50)
        tk.Label(window_showmail1,text='内容:').place(x=30, y=70)
        
        mail_test=tk.Text(window_showmail1)
        mail_test.insert('end',mail.get_txt(msg))
        mail_test.place(x=20,y=100)
        
            
    
    ##############################
    
    
    ##############################
    def no_show1():
        window_showmail1.destroy()
    
    ###############################
    
    if mail.get_from(msg) in blackandwhite.white_list:
        window_showmail1 = tk.Toplevel(window)
        window_showmail1.geometry('1000x1000')
        window_showmail1.title('接受到白名单用户发送的邮件')
        tk.Button(window_showmail1, text='展示邮件',command=yes_show1).place(x=300, y=50)
        tk.Button(window_showmail1, text='不看了',command=no_show1).place(x=700, y=50)
        tk.Label(window_showmail1, text='这是白名单用户发送的邮件',font = ('黑体',25)).place(x=300, y= 650)
        
        window_mail.destroy()
    else:
        flag=bayesfilter.bayes(mail_dict,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
        ##################################bayes2
        mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
        possible=bayesfilter.bayes2(mail_dict2,spdict,hadict)#possible---是垃圾邮件的概率 阈值0.9
        
        if len(hadict)<10000:
            if possible>0.9:
                show_flag=False
            else:
                show_flag=True
        if len(hadict)>10000:
            if flag!=True:
                show_flag=False
            else:
                show_flag=True
        
        ###################################
        '''
        if flag!=True:
            flag=False#显示信息交给show flag只保存判断的结果，存疑结果为false
            
            
        if flag!=True:
            bayes1='垃圾邮件！'
        else:
            bayes1='非垃圾邮件！'
        '''   
            
            
        ###############################5.9改
        if flag==False:
            bayes1='垃圾邮件！'
        if flag==True:
            bayes1='非垃圾邮件！'
        if flag=='这封邮件过短，是可疑邮件':
            bayes1='这封邮件过短，是可疑邮件'
            
        ###############################   
        ########################################两种bayes方法的综合利用
        if flag==True and possible>0.9:
            #show_flag='两种算法不同是可疑邮件！'
            tk.messagebox.showinfo(title='可疑邮件',message='两种贝叶斯算法结果不同，是一封可疑邮件')
            flag=False
        
        ###############################################################################
        if show_flag==True:
            tk.Label(window_mail,text='非垃圾邮件！',font=("黑体", 16),bg="green").place(x=230, y=50)
        if show_flag==False:
            tk.Label(window_mail,text='垃圾邮件！',font=("黑体", 16),bg="red").place(x=230, y=50)
        if show_flag=='系统默认可疑邮件为垃圾邮件！':
            tk.Label(window_mail,text=show_flag).place(x=230, y=50)
            
        ##############################################################################
        
        
        
        tk.Label(window_mail,text='贝叶斯算法1的结论： '+bayes1).place(x=30, y=180)
        tk.Label(window_mail,text='贝叶斯算法2的概率： '+str(possible)).place(x=30, y=150)
        tk.Label(window_mail,text='*'*90).place(x=30, y=200)  
        tk.Label(window_mail,text='收件人：'+ mail.get_to(msg)).place(x=30, y=230)
        tk.Label(window_mail,text='是否展示这封邮件？').place(x=30, y=250)
        #判断是否正确
        tk.Label(window_mail,text='如果判断不正确，点击错误学习将这封邮件加入学习字典').place(x=30, y=360)
        ####################################################################################################
        def study():
            if flag==True:#错误学习，flag为true判断错了，应是垃圾邮件
                global spdict
                num1=spam_dict.spamdict_count(spdict)
                spdict=spam_dict.add_spamdict(spdict,mail_path)
                num2=spam_dict.spamdict_count(spdict)
                tk.messagebox.showinfo(title='已将新的字典添加到垃圾学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
            else:
                global hadict
                num1=ham_dict.hamdict_count(hadict)
                hadict=ham_dict.add_hamdict(hadict,mail_path)
                num2=ham_dict.hamdict_count(hadict)
                tk.messagebox.showinfo(title='已将新的字典添加到正常学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
        ########################################################################################################### 
        
        
        
        tk.Button(window_mail, text='错误学习',command=study).place(x=370, y=360)
        
    
    
    
    
    ############################
    
    def yes_show():
        #####################在是否展示处设置敏感词
        flag_ban=bayesfilter.ban(ban_words)
        if flag_ban==True:
            window_banmail = tk.Toplevel(window_mail)
            window_banmail.geometry('300x200')
            window_banmail.title('含有敏感词的邮件')
            tk.Label(window_banmail,text='这是一封含有敏感词的邮件是否继续展示？').place(x=20,y=20)
            #####################################
            def yes_show3():
                window_showmail = tk.Toplevel(window_mail)
                window_showmail.geometry('1000x1000')
                window_showmail.title('展示邮件')
                fp = open(mail_path, "r")
                msg = email.message_from_file(fp)
                tk.Label(window_showmail,text='发件人：'+ mail.get_from(msg)).place(x=30, y=10)
                tk.Label(window_showmail,text='收件人：'+ mail.get_to(msg)).place(x=30, y=50)
                tk.Label(window_showmail,text='内容:').place(x=30, y=70)
        
                mail_test=tk.Text(window_showmail)
                mail_test.insert('end',mail.get_txt(msg))
                mail_test.place(x=20,y=100)
            ######################################
            tk.Button(window_banmail, text='好的',command=yes_show3).place(x=30, y=55)
            #####################################
            def no_show3():
                window_banmail.destroy()
                window_mail.destroy()
            #####################################
            tk.Button(window_banmail, text='不看',command=no_show3).place(x=30, y=85)
            
        else:
        
            window_showmail = tk.Toplevel(window_mail)
            window_showmail.geometry('1000x1000')
            window_showmail.title('展示邮件')
            fp = open(mail_path, "r")
            msg = email.message_from_file(fp)
            tk.Label(window_showmail,text='发件人：'+ mail.get_from(msg)).place(x=30, y=10)
            tk.Label(window_showmail,text='收件人：'+ mail.get_to(msg)).place(x=30, y=50)
            tk.Label(window_showmail,text='内容:').place(x=30, y=70)
            
            mail_test=tk.Text(window_showmail)
            mail_test.insert('end',mail.get_txt(msg))
            mail_test.place(x=20,y=100)
        
            
    
    ##############################
    tk.Button(window_mail, text='好的',command=yes_show).place(x=30, y=280)
    tk.Label(window_mail, text='展示').place(x=70, y=280)
    
    
    if flag==False:
        ######################################
        def add_black1():
            window_showblack = tk.Toplevel(window_mail)
            window_showblack.geometry('300x200')
            window_showblack.title('黑名单')
            blackandwhite.add_black(mail_path)
            new_black_list=blackandwhite.black_list
            tk.Label(window_showblack,text='黑名单：'+ str(new_black_list)).place(x=30, y=30)
        
        ######################################
        tk.Button(window_mail, text='好的',command=add_black1).place(x=30, y=305)
        tk.Label(window_mail, text='将发件人加入黑名单------加入后将不在收到来自他/她的来信').place(x=70, y=305)
        #######################################
        def add_test():
            global spdict
            num1=spam_dict.spamdict_count(spdict)
            spdict=spam_dict.add_spamdict(spdict,mail_path)
            num2=spam_dict.spamdict_count(spdict)
            tk.messagebox.showinfo(title='已添加新的字典到学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
        
        
        
        #########################################
        tk.Label(window_mail, text='更新利用现有训练集继续判断').place(x=70, y=330)
        tk.Button(window_mail, text='好的',command=add_test).place(x=30, y=330)
        
        
        
        
        
    else:
        ######################################
        def add_white1():
            window_showwhite = tk.Toplevel(window_mail)
            window_showwhite.geometry('300x200')
            window_showwhite.title('白名单')
            blackandwhite.add_white(mail_path)
            new_white_list=blackandwhite.white_list
            tk.Label(window_showwhite,text='白名单：'+ str(new_white_list)).place(x=30, y=30)
        
        ######################################
        tk.Label(window_mail, text='将发件人加入白名单------以后收到他/她的来信将不再判断').place(x=70, y=305)
        tk.Button(window_mail, text='好的',command=add_white1).place(x=30, y=305)
        #######################################
        def add_test():
            global hadict
            num1=ham_dict.hamdict_count(hadict)
            hadict=ham_dict.add_hamdict(hadict,mail_path)
            num2=ham_dict.hamdict_count(hadict)
            tk.messagebox.showinfo(title='已添加新的字典到学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
        
        
        
        #########################################
        tk.Label(window_mail, text='更新利用现有训练集继续判断').place(x=70, y=330)
        tk.Button(window_mail, text='好的',command=add_test).place(x=30, y=330)
        
        
tk.Label(window, text='当前训练集下的准确率：').place(x=120, y=150)
####################################################################################
def get_account():
    
    tk.Label(window, text=func.account_right(spdict,hadict)).place(x=270, y=150)
######################################################################################
tk.Button(window, text='更新',command=get_account).place(x=80, y=145) 



  
    
    
    

btn_in_mail= tk.Button(window, text='开始判断', command=mail_test)
btn_in_mail.place(x=330, y=215)






#######################NEW
import get_mail
#####################################
def mail_test1():
    global spdict
    global hadict
       
    window_mail = tk.Toplevel(window)
    window_mail.geometry('600x500')
    window_mail.title('贝叶斯判断')
    
    tk.Label(window_mail,text='待测试邮件为邮箱中的邮件').place(x=30, y=100)
    mail_dict=bayesfilter.count_words1()   
    tk.Label(window_mail, text='当前邮件的参数',font = ('黑体',25)).place(x=180,y=5)
    if get_mail.get_from() in blackandwhite.black_list:
        tk.messagebox.showinfo(title='检测到黑名单用户',message='这封邮件由黑名单用户：'+get_mail.get_from()+'发送')
        window_mail.destroy()
    
    def yes_show1():
        tk.Label(window_showmail1,text='发件人：'+ get_mail.get_from()).place(x=30, y=10)
        tk.Label(window_showmail1,text='收件人：'+ 'lovejiaxi_5@163.com').place(x=30, y=50)
        tk.Label(window_showmail1,text='内容:').place(x=30, y=70)
        mail_test=tk.Text(window_showmail1)
        mail_test.insert('end',get_mail.get_content())
        mail_test.place(x=20,y=100)
    def no_show1():
        window_showmail1.destroy()
 
    if get_mail.get_from() in blackandwhite.white_list:
        window_showmail1 = tk.Toplevel(window)
        window_showmail1.geometry('1000x1000')
        window_showmail1.title('接受到白名单用户发送的邮件')
        tk.Button(window_showmail1, text='展示邮件',command=yes_show1).place(x=300, y=50)
        tk.Button(window_showmail1, text='不看了',command=no_show1).place(x=700, y=50)
        tk.Label(window_showmail1, text='这是白名单用户发送的邮件',font = ('黑体',25)).place(x=300, y= 650)
        window_mail.destroy()
    else:
        flag=bayesfilter.bayes(mail_dict,spdict,hadict)#flag=false时是垃圾邮件 true时是正常邮件
        ##################################bayes2
        mail_dict2=bayesfilter.get_probdict(mail_dict,spdict,hadict)
        possible=bayesfilter.bayes2(mail_dict2,spdict,hadict)#possible---是垃圾邮件的概率 阈值0.9
        
        if len(hadict)<10000:
            if possible>0.9:
                show_flag=False
            else:
                show_flag=True
        if len(hadict)>10000:
            if flag!=True:
                show_flag=False
            else:
                show_flag=True
        if flag==False:
            bayes1='垃圾邮件！'
        if flag==True:
            bayes1='非垃圾邮件！'
        if flag=='这封邮件过短，是可疑邮件':
            bayes1='这封邮件过短，是可疑邮件'

        if flag==True and possible>0.9:
            #show_flag='两种算法不同是可疑邮件！'
            tk.messagebox.showinfo(title='可疑邮件',message='两种贝叶斯算法结果不同，是一封可疑邮件')
            flag=False
        if show_flag==True:
            tk.Label(window_mail,text='非垃圾邮件！',font=("黑体", 16),bg="green").place(x=230, y=50)
        if show_flag==False:
            tk.Label(window_mail,text='垃圾邮件！',font=("黑体", 16),bg="red").place(x=230, y=50)
        if show_flag=='系统默认可疑邮件为垃圾邮件！':
            tk.Label(window_mail,text=show_flag).place(x=230, y=50)
        tk.Label(window_mail,text='贝叶斯算法1的结论： '+bayes1).place(x=30, y=180)
        tk.Label(window_mail,text='贝叶斯算法2的概率： '+str(possible)).place(x=30, y=150)
        tk.Label(window_mail,text='*'*90).place(x=30, y=200)  
        tk.Label(window_mail,text='收件人：'+ 'lovejiaxi_5@163.com').place(x=30, y=230)
        tk.Label(window_mail,text='是否展示这封邮件？').place(x=30, y=250)
        #判断是否正确
        tk.Label(window_mail,text='如果判断不正确，点击错误学习将这封邮件加入学习字典').place(x=30, y=360)
        ####################################################################################################
        def study():
            if flag==True:#错误学习，flag为true判断错了，应是垃圾邮件
                global spdict
                num1=spam_dict.spamdict_count(spdict)
                spdict=spam_dict.add_spamdict1(spdict)
                num2=spam_dict.spamdict_count(spdict)
                tk.messagebox.showinfo(title='已将新的字典添加到垃圾学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
            else:
                global hadict
                num1=ham_dict.hamdict_count(hadict)
                hadict=ham_dict.add_hamdict1(hadict)
                num2=ham_dict.hamdict_count(hadict)
                tk.messagebox.showinfo(title='已将新的字典添加到正常学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )

        tk.Button(window_mail, text='错误学习',command=study).place(x=370, y=360)
 
    def yes_show():
        #####################在是否展示处设置敏感词
        flag_ban=bayesfilter.ban(ban_words)
        if flag_ban==True:
            window_banmail = tk.Toplevel(window_mail)
            window_banmail.geometry('300x200')
            window_banmail.title('含有敏感词的邮件')
            tk.Label(window_banmail,text='这是一封含有敏感词的邮件是否继续展示？').place(x=20,y=20)
            #####################################
            def yes_show3():
                window_showmail = tk.Toplevel(window_mail)
                window_showmail.geometry('1000x1000')
                window_showmail.title('展示邮件')
                tk.Label(window_showmail,text='发件人：'+ get_mail.get_from()).place(x=30, y=10)
                tk.Label(window_showmail,text='收件人：'+ 'lovejiaxi_5@163.com').place(x=30, y=50)
                tk.Label(window_showmail,text='内容:').place(x=30, y=70)
        
                mail_test=tk.Text(window_showmail)
                mail_test.insert('end',get_mail.get_content())
                mail_test.place(x=20,y=100)
            ######################################
            tk.Button(window_banmail, text='好的',command=yes_show3).place(x=30, y=55)
            #####################################
            def no_show3():
                window_banmail.destroy()
                window_mail.destroy()
            #####################################
            tk.Button(window_banmail, text='不看',command=no_show3).place(x=30, y=85)
            
        else:
        
            window_showmail = tk.Toplevel(window_mail)
            window_showmail.geometry('1000x1000')
            window_showmail.title('展示邮件')
            tk.Label(window_showmail,text='发件人：'+ get_mail.get_from()).place(x=30, y=10)
            tk.Label(window_showmail,text='收件人：'+ 'lovejiaxi_5@163.com').place(x=30, y=50)
            tk.Label(window_showmail,text='内容:').place(x=30, y=70)
            
            mail_test=tk.Text(window_showmail)
            mail_test.insert('end',get_mail.get_content())
            mail_test.place(x=20,y=100)

    tk.Button(window_mail, text='好的',command=yes_show).place(x=30, y=280)
    tk.Label(window_mail, text='展示').place(x=70, y=280)
    
    if flag==False:
        ######################################
        def add_black1():
            window_showblack = tk.Toplevel(window_mail)
            window_showblack.geometry('300x200')
            window_showblack.title('黑名单')
            blackandwhite.add_black1()
            new_black_list=blackandwhite.black_list
            tk.Label(window_showblack,text='黑名单：'+ str(new_black_list)).place(x=30, y=30)

        tk.Button(window_mail, text='好的',command=add_black1).place(x=30, y=305)
        tk.Label(window_mail, text='将发件人加入黑名单------加入后将不在收到来自他/她的来信').place(x=70, y=305)
        #######################################
        def add_test():
            global spdict
            num1=spam_dict.spamdict_count(spdict)
            spdict=spam_dict.add_spamdict1(spdict)
            num2=spam_dict.spamdict_count(spdict)
            tk.messagebox.showinfo(title='已添加新的字典到学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
        
        tk.Label(window_mail, text='更新利用现有训练集继续判断').place(x=70, y=330)
        tk.Button(window_mail, text='好的',command=add_test).place(x=30, y=330)
        
        
        
        
        
    else:
        ######################################
        def add_white1():
            window_showwhite = tk.Toplevel(window_mail)
            window_showwhite.geometry('300x200')
            window_showwhite.title('白名单')
            blackandwhite.add_white1()
            new_white_list=blackandwhite.white_list
            tk.Label(window_showwhite,text='白名单：'+ str(new_white_list)).place(x=30, y=30)
        
        ######################################
        tk.Label(window_mail, text='将发件人加入白名单------以后收到他/她的来信将不再判断').place(x=70, y=305)
        tk.Button(window_mail, text='好的',command=add_white1).place(x=30, y=305)
        #######################################
        def add_test():
            global hadict
            num1=ham_dict.hamdict_count(hadict)
            hadict=ham_dict.add_hamdict1(hadict)
            num2=ham_dict.hamdict_count(hadict)
            tk.messagebox.showinfo(title='已添加新的字典到学习字典中！',message='更新前的sum words：'+str(num1)+'    '+'当前的sum words：'+str(num2) )
        
        
        
        #########################################
        tk.Label(window_mail, text='更新利用现有训练集继续判断').place(x=70, y=330)
        tk.Button(window_mail, text='好的',command=add_test).place(x=30, y=330)
  


###################################














btn_in_mail= tk.Button(window, text='判断邮箱中的邮件', command=mail_test1)
btn_in_mail.place(x=170, y=250)


window.mainloop()



def get_banlist(blist):
    return blist












































    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


