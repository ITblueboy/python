import itchat
import time
import re
from itchat.content import *
#coding=utf8
 
 
# ����Է����������֣������Ǹ��Է��ظ����µĶ���
@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('��',msg['Text'])
    if match:
        itchat.send(('���Ҿ�ף�㹷��󼪴������µ�һ������˳��'),msg['FromUserName'])
 
# ����Է����͵���ͼƬ����Ƶ����Ƶ�ͷ���Ķ������Ƕ��������»ظ���
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
    itchat.send(('���Ҿ�ף�㹷��󼪴������µ�һ������˳��'),msg['FromUserName'])
 
itchat.auto_login(hotReload=True)
itchat.run()
