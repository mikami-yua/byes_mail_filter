import email
#邮件预处理模块
#完成对发件人的解析 对收件人的解析 对邮件内容的解析

def get_subject(fp):
    #fp = open(strg_path, "r")
    msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码
    #subject = msg.get('subject') # 取信件头里的subject,　也就是主题
    return msg

def get_from(msg):
    send_from=email.utils.parseaddr(msg.get("from"))[1]
    return send_from

def get_to(msg):
    send_to=email.utils.parseaddr(msg.get("to"))[1]
    return send_to

def get_txt(msg):
    for par in msg.walk():
      if not par.is_multipart():# 这里要判断是否是multipart，是的话，里面的数据是无用的
        strg=par.get_payload(decode=False)
    return strg

def mail_api(fp):
    messg=get_subject(fp)
    sb_from=get_from(messg)
    sb_to=get_to(messg)
    context=get_txt(messg)
    return context

def mail_display(path):
    fp = open(path, "r")
    msg = email.message_from_file(fp)


