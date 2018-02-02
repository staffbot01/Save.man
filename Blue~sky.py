# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess,pickle

cl = LINETCR.LINE()
cl.login(token="ใส่โทเค็น")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ใส่โทเค็น k1")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="ใส่โทเค็น k2")
kk.loginResult()

ks = LINETCR.LINE()
ks.login(token="ใส่โทเค็น k3")
ks.loginResult()

kc = LINETCR.LINE()
kc.login(token="ใส่โทเค็น k4")
kc.loginResult()

ka = LINETCR.LINE()
ka.login(token="ใส่โทเค็น k5")
ka.loginResult()

with open('profileSave.pkl') as f:
    save1 = pickle.load(f)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""Mr. Bots…⛿
╔══╦═╦═╗
║║║║║║║║    ✯✯❇ᵀᴴᴬᴵᴸᴬᴺᴰ❇✯✯
║║║║╦║║║ ❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͡o͜͡Ŧ❇
╚╩╩╩╩╩╩╝️ နับთิஏთั้ଏบਹທ SirichanV⒑
📧https://line.me/R/ti/p/%40uvh1233u
╔══════════════════════
║❂➣[Id]
║❂➣[Mid]
║❂➣[All mid]
║❂➣[Me]
║❂➣[You @]
║❂➣[Mybot]
║❂➣[Name Bot (Text)]
║❂➣[Sendcontact]
║❂➣[K1/K2/K3 join]
║❂➣[K1/K2/K3/]
║❂➣[K1/K2/K3 fuck:]
║❂➣[K1/K2/K3 gift
║❂➣[Allgift]
║❂➣[Group Id]
║❂➣[TL:"Text"]
║❂➣[Clock:]
║❂➣[Up clock]
║❂➣[Name:'text']
║❂➣[Mic]:"mid"]
║❂➣[Mc @]
║❂➣[Rejectall]
║❂➣[Massage add:"text"]
║❂➣[Add confirmasi]
║❂➣[Comment set:"Text"]
║❂➣[Comment check]
║❂➣[Clock: on]
║❂➣[Clock: off]
║❂➣[Ban]:
║❂➣[Unban]:
║❂➣[Conban]
║❂➣[Banlist]:
║❂➣[Allgiftt]
║❂➣[Test]
║❂➣[Copy @]
║❂➣[Save]
║❂➣[Load]
║❂➣[Spam on (Number) (Text)
║❂➣[Spam off (Number) (Text)
║❂➣[Gcreator]
║❂➣[Covergroup]
║❂➣[Tagall]
║❂➣[Kicker]
║❂➣[Setpoint]
║❂➣[Setcheck]
║❂➣[Kick"@tag]]
╠══════════════════════
║    ✥(sᴇᴛ)ᴄᴏᴍᴍᴀɴᴅ✥
╠══════════════════════
║❂➣[Contact: on/off] 
║❂➣[Auto join: on/off] 
║❂➣[Cancel Invite: 1 on/off]
║❂➣[Auto share: on/off]
║❂➣[Auto leave: on/off] 
║❂➣[Comment: on/off]
║❂➣[Auto add: on/off]
║❂➣[Auto like: on/off]
╠══════════════════════
║✥ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ✥
╠══════════════════════
║❂➣[Ban"@Tag] 
║❂➣[Unban"@Tag] 
║❂➣[Urlon]:
║❂➣[Urloff]:
║❂➣[Url]:
║❂➣[Ginfo]:
║❂➣[Invite:"mid"] 
║❂➣[Say:"Text"]:
║❂➣[Cancel]:
║❂➣[Gn:"name"]:
║❂➣[NK @tag]:
║❂➣[Dead]
╠══════════════════════
║•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•
╚══════════════════════
    Message Protect  [Help2]
"""
helpMessage2 ="""•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•
╔═══════════════════════
║❂➣[PROTECT: ON/OFF]ชุดล็อกกลุ่ม
║❂➣[BLOCK URL: ON/OFF] ล็อกลิงก์
║❂➣[NAMELOCK: ON/OFF] ล็อกชื่อกลุ่ม
║❂➣[BLOCKINVITE: ON/OFF]ล็อกเชิญ
╚═══════════════════════
"""
KAC = [cl,ki,kk,ks,kc,ka]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
kimid = kk.getProfile().mid
ki2mid = ks.getProfile().mid
Cmid = kc.getProfile().mid
Emid = ka.getProfile().mid
admin = ["ud24af63fd62d14c3bf8f719df80c3745"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

admins = ["ud24af63fd62d14c3bf8f719df80c3745"]
Rx5 = ["u406133ad4d3fbe50a2f4d51ea081d050"]
Rx4 = ["u406133ad4d3fbe50a2f4d51ea081d050"]
Rx3 = ["u406133ad4d3fbe50a2f4d51ea081d050"]
Rx2 = ["ua51ba06b0dd18c0bfe2cc6caa3458202"]
Rx1 = ["uc7f32bb28dc009916d40af87c9910ddc"]
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5
adminsA = admins + Rx3 + Rx5

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凄1�7"]

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""──────┅═ই۝ई═┅──────
နับთิஏთั้ଏบਹທ  Sirichan V⒑ ชุดบอทป้องกัน
สนใจติดต่อที่  ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ
http://line.me/ti/p/~1ove..neverdie
──────┅═ই۝ई═┅──────
Thank For Add Me  Creator Selfbot
""",
    "lang":"JP",
    "comment":"Auto like By.[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅] \n\nနับთิஏთั้ଏบਹທ  Sirichan V⒑ ชุดบอทป้องกัน\n📧https://line.me/R/ti/p/%40uvh1233u \n",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},    
    "dblacklist":False
}

wait2 = {
	'readMember':{},	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

save1 = {
    "Saved":False,
    "displayName":"",
    "statusMessage":"",
    "pictureStatus":""
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
         
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

        if op.type == 15:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,"👋Ɓy℮ Bye ☛" + cl.getContact(op.param2).displayName + "☚ \n\n「REPORT MEMBER LEAVE OUT GROUP」 🕘 " + datetime.today().strftime('%H:%M:%S') )
            print ("MEMBER HAS LEFT THE GROUP")

        if op.type == 19:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ☚ 👣ซัดเต็มข้อเลยครับ👀..ท่านผู้ชม😯 \n\n「MEMBER KICK OUT FORM GROUP」 🕘 " +datetime.today().strftime('%H:%M:%S') )
            print "MEMBER KICK OUT FORM GROUP"

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ka.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            koutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass                
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ud24af63fd62d14c3bf8f719df80c3745":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvita		
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])							
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)							
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"It's included in a blacklist already〄1�7")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to make a comment〄1�7")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"It's included in a blacklist already.〄1�7")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"It was added to the blacklist.〄1�7")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Key","KEY"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:"in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif "kick:" in msg.text:
                midd = msg.text.replace("kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "K1 invite:" in msg.text:
                midd = msg.text.replace("K1 invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "K1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "K2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
            elif "K3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)    
            elif "K4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "K5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
            elif "Sendcontact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
            elif msg.text in ["Gift","Man gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ka.sendMessage(msg)
            elif msg.text in ["Allgift","All Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)

            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            cl.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif msg.text in ["K1 cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            ki.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
                        
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment check"]:
                cl.sendText(msg.to,"An automatic comment is established as follows at present。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")
            elif msg.text in ["コメント:オフ","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")          
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Block url:on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"ƊƠƝЄ")
            elif msg.text in ["Block url:off"]:
                if msg.from_ in Administrator:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"ƛԼԼƠƜЄƊ")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ")
            elif msg.text in ["Urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƠƝ ƛԼƦЄƛƊƳ〄1�7")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƇԼƠƧЄƊ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["ginfo","Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิดอยู่"
                        else:
                            u = "เปิดอยู่"
                        cl.sendText(msg.to,"[กลุ่ม]\n" + str(ginfo.name) + "\n\n[ไอดีกลุ่ม]\n" + msg.to + "\n\n[ผู้สร้างกลุ่ม]\n" + gCreator + "\n\n[รูปโปรไฟล์กลุ่ม]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nสมาชิก:" + str(len(ginfo.members)) + " ท่าน\nเชิญ:" + sinvitee + " ท่าน\nURL:" + u + "")
                    else:
                        cl.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,kimid)
                ks.sendText(msg.to,ki2mid)      
            elif "ฮ่าๆ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "โกรธ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "ยินดีต้อนรับ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Name:" in msg.text:
                string = msg.text.replace("Name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
            elif "Name Bot" in msg.text:
                string = msg.text.replace("Name Bot","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    kk.updateProfile(profile)
                    ks.updateProfile(profile)
                    kc.updateProfile(profile)
                    ka.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
#---------------------------------------------------------
            elif "K1 upname:" in msg.text:
                string = msg.text.replace("K1 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K2 upname:" in msg.text:
                string = msg.text.replace("K2 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K3 upname:" in msg.text:
                string = msg.text.replace("K3 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K1 upstatus: " in msg.text:
                string = msg.text.replace("K1 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            elif "K2 upstatus: " in msg.text:
                string = msg.text.replace("K2 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"display message " + string + " done")
            elif "K3 upstatus: " in msg.text:
                string = msg.text.replace("K3 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"display message " + string + " done")
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif "Cancel invite:" in msg.text:
                try:
                    strnum = msg.text.replace("Cancel invite:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off。\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "A group below the person made sure that I'll refuse invitation automatically。")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong。")
                    else:
                        cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["共有:オン","共有：オン","Auto share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["共有:オフ","共有：オフ","Auto share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")                        
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="✔ Contact → on \n"
                else:md+="❎ Contact → off \n"
                if wait["autoJoin"] == True: md+="✔  Auto join → on \n"
                else:md+="❎ Auto join → off \n"
                if wait["autoCancel"]["on"] == True:md+="✔ Cancel Invite → " + str(wait["autoCancel"]["members"]) + " \n" 
                else:md+="❎ Cancel Invite → off \n"  
                if wait["leaveRoom"] == True: md+="✔ Auto leave → on \n"   
                else:md+="❎ Auto leave → off \n"
                if wait["timeline"] == True: md+="✔ Auto Share → on \n"
                else:md+="❎ Auto Share → off \n"
                if wait["commentOn"] == True: md+="✔ Comment → on \n"
                else:md+="❎ Comment → off \n"
                if wait["autoAdd"] == True: md+="✔ Auto add → on \n"
                else:md+="❎ Auto add → off \n"
                if wait["likeOn"] == True: md+="✔ Auto like → on \n"
                else:md+="❎ Auto like → off \n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion。")
                else:
                    cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

            elif msg.text in ["Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's on already。")
                    else:
                        cl.sendText(msg.to,"on already。")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned on。")
                    else:
                        cl.sendText(msg.to,"Turned on。")
            elif msg.text in ["Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's off already。")
                    else:
                        cl.sendText(msg.to,"off already。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned off。")
                    else:
                        cl.sendText(msg.to,"Turned off。")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:","")
                cl.sendText(msg.to,"The message was changed。")
            elif "Auto addition→" in msg.text:
                wait["message"] = msg.text.replace("Auto addition→","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"The message was changed。")
                else:
                    cl.sendText(msg.to,"was change already。")
            elif msg.text in ["Add confirmasi","自動追加問候語確認"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".automatic message is established as follows。\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image。\n\n" + wait["message"])
            elif msg.text in ["CHANGE","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"ƇƠƲƝƬƦƳ ԼƛƝƓƲƛƓЄ ƊƲƦƖƝƓ ƛ ƇHƛƝƓЄ。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". The language was made English。")
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ.。")
                    else:
                        cl.sendText(msg.to,"ƖMƤƠƧƧƖƁԼЄ ƲƧЄ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ. ")
            elif "gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ。")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƛƝ ƝƠƬ ƁЄ ƲƧЄƊ ƠƲƬƧƖƊЄ ƬHЄ ƓƦƠƲƤ")
                    else:
                        cl.sendText(msg.to,"ƝƠƬ ƑƠƦ ƲƧЄ ԼЄƧƧ ƬHƛƝ ƓƦƠƲƤ")
            elif msg.text in ["cb"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbd"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist。")
                else:
                    cl.sendText(msg.to,"Below is a blacklist。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already。")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["Clock:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.。")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off。")
            elif "Clock:" in msg.text:
                n = msg.text.replace("Clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock。")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["Up clock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed。")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.。")
            elif "Tagall" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
            elif "Kicker" in msg.text:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            elif msg.text in ["K1 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["K2 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["K3 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)                           

            elif msg.text in ["Bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					ka.leaveGroup(msg.to)
                except:
                     pass            
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kc.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kc.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------------------                          
            elif "Kick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           cl.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "K1 fuck" in msg.text:
				OWN = "u9fee8ed8e746cc6134346e37f672cbb3"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K1 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])							   
							except:
									ki.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "K2 fuck" in msg.text:
				OWN = "u49e3ce7e546c60d2f5a38afe264fd1e9"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K2 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])							   
							except:
									kk.kickoutFromGroup(msg.to, [target])							   
									pass

            elif "K3 fuck" in msg.text:
				OWN = "uc903012b76390e088c772b21062a3b20"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K3 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])							   
							except:
									ks.kickoutFromGroup(msg.to, [target])							   
									pass									
            elif "Ban " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("Ban ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
#-----------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-----------------------------------------------------------
            elif "Unban " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
#-----------------------------------------------------------
            elif "Protect:on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ")
            elif "Protect:off" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ")
					else:
						cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
				except:
					pass
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass                                 
#-----------------------------------------------------------
            elif msg.text in ["Delete chat"]:
                cl.removeAllMessages(op.param2)
                ki.removeAllMessages(op.param2)
                kk.removeAllMessages(op.param2)
                ks.removeAllMessages(op.param2)
                kc.removeAllMessages(op.param2)
                ka.removeAllMessages(op.param2)
                cl.sendText(msg.to,"Delete Chat")
                cl.sendText(msg.to,"Success...")
#-----------------------------------------------------------
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Spam Start")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ki.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kk.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       kc.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ka.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       ks.sendText(g.mid," (ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ)")
                       cl.sendText(msg.to, "Ok success")
                       print "Done spam" 
#----------------------------------------------------------
