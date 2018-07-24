import itchat
import time
import re
from itchat.content import *
#coding=utf8
 
 
# 如果对方发的是文字，则我们给对方回复以下的东西
@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('年',msg['Text'])
    if match:
        itchat.send(('那我就祝你狗年大吉大利，新的一年事事顺心'),msg['FromUserName'])
 
# 如果对方发送的是图片，音频，视频和分享的东西我们都做出以下回复。
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
    itchat.send(('那我就祝你狗年大吉大利，新的一年事事顺心'),msg['FromUserName'])
 
itchat.auto_login(hotReload=True)
itchat.run()
