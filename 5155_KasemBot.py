# -*- coding: utf-8 -*-

import LINELEONY
from LINELEONY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINELEONY.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""

􀔃􀅕===[ COMMAND PUBLIC ]===
[Set sider] Check Silent Reader
[Cek sider] Show Silent Reader
[Cancel] Cancel User
[Troops qr on] Open url Group
[Troops qr off] Close url Group
[View Service] View Bot Service
[Gcreator:Inv] Inv Group Creator
[Creator:inv] Invite Creator Bot
[Creator] Creator Bot 
[Gcreator] Group Creator

􀔃􀅕===[ Command Admin]===
[SetGroup] Setting Group Privacy
[Troops join] Beautiful girl join to the group
[Troops bye]  Leave Bot
[Mention All] Tag all user
[Protect On/Off] Protection Mode
[Kickjoin On/Off] Bitch Mode
[SMS ] Send a Private Message
======================
 Support by : 
T̶̸̘̟̼̉̈́͐͋͌̊E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑A̶̸̘̫͈̭͌͛͌̇̇̍M̶̸̘͈̺̪͓̺ͩ͂̾ͪ̀̋ B̶̸͎̣̫͈̥̗͒͌̃͑̔̾ͅO̶̸̜̓̇ͫ̉͊ͨS̶̸̪̭̱̼̼̉̈́ͪ͋̽̚E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑N̶̸͉̠̙͉̗̺̋̔ͧ̊ K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅI̶̸̞̟̫̺ͭ̒ͭͣC̶̸͔ͣͦ́́͂ͅK̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑R̶̸̼̯̤̗̲̞̥̈ͭ̃ͨ̆A̶̸̘̫͈̭͌͛͌̇̇̍N̶̸͉̠̙͉̗̺̋̔ͧ̊.
======================
"""
SetGroup =""" Privacy Menu 􀔃􀄆☣☣☣

[Reject Invite -- Cancel On / Off]
[Protect Cancel -- On / Off]
[Protect Qr -- On / Off]
[Protect Group -- Protect On/Off]
[Kicked if Join -- Kickjoin On/Off]
[Broadcast] Broadcast all group
[Copy @ ] Duplicate Profile
[/Leave (gid)] Left by ID
[/InviteMeTo (gid)] Invite Creator by ID
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["YOUR_MID_HERE"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"Chivas ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


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
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
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

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False







#-------------- = Spammed User Start = -----------#
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki11.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki12.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki13.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki14.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki15.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki16.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki17.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki18.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

#---------------------- = NUKE = ------------------

#-----------------------------------------------
            elif msg.text.lower() == 'sini':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------







.                elif op.param3 in ki19mid:
                    if op.param2 in ki20mid:
                        G = ki20.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki20.updateGroup(G)
                    else:
                        G = ki20.getGroup(op.param1)


                        ki20.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki20.updateGroup(G)

                elif op.param3 in ki20mid:
                    if op.param2 in ki19mid:
                        G = ki19.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki19.updateGroup(G)
                        Ticket = ki19.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki19.updateGroup(G)
                    else:
                        G = ki19.getGroup(op.param1)


                        ki20.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki19.updateGroup(G)
                        Ticket = ki19.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki19.updateGroup(G)
            except:
                pass
                   Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
<Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
# -*- coding: utf-8 -*-

import LINELEONY
from LINELEONY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINELEONY.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ☣☣ LEON BOTS ☣☣

􀔃􀅕===[ COMMAND PUBLIC ]===
[Set sider] Check Silent Reader
[Cek sider] Show Silent Reader
[Cancel] Cancel User
[Troops qr on] Open url Group
[Troops qr off] Close url Group
[View Service] View Bot Service
[Gcreator:Inv] Inv Group Creator
[Creator:inv] Invite Creator Bot
[Creator] Creator Bot 
[Gcreator] Group Creator

􀔃􀅕===[ Command Admin]===
[SetGroup] Setting Group Privacy
[Troops join] Beautiful girl join to the group
[Troops bye]  Leave Bot
[Mention All] Tag all user
[Protect On/Off] Protection Mode
[Kickjoin On/Off] Bitch Mode
[SMS ] Send a Private Message
======================
 Support by : 
T̶̸̘̟̼̉̈́͐͋͌̊E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑A̶̸̘̫͈̭͌͛͌̇̇̍M̶̸̘͈̺̪͓̺ͩ͂̾ͪ̀̋ B̶̸͎̣̫͈̥̗͒͌̃͑̔̾ͅO̶̸̜̓̇ͫ̉͊ͨS̶̸̪̭̱̼̼̉̈́ͪ͋̽̚E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑N̶̸͉̠̙͉̗̺̋̔ͧ̊ K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅI̶̸̞̟̫̺ͭ̒ͭͣC̶̸͔ͣͦ́́͂ͅK̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑R̶̸̼̯̤̗̲̞̥̈ͭ̃ͨ̆A̶̸̘̫͈̭͌͛͌̇̇̍N̶̸͉̠̙͉̗̺̋̔ͧ̊.
======================
"""
SetGroup =""" Privacy Menu 􀔃􀄆☣☣☣

[Reject Invite -- Cancel On / Off]
[Protect Cancel -- On / Off]
[Protect Qr -- On / Off]
[Protect Group -- Protect On/Off]
[Kicked if Join -- Kickjoin On/Off]
[Broadcast] Broadcast all group
[Copy @ ] Duplicate Profile
[/Leave (gid)] Left by ID
[/InviteMeTo (gid)] Invite Creator by ID
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["YOUR_MID_HERE"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"Chivas ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


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
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
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

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
<Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
# -*- coding: utf-8 -*-

import LINELEONY
from LINELEONY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINELEONY.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ☣☣ LEON BOTS ☣☣

􀔃􀅕===[ COMMAND PUBLIC ]===
[Set sider] Check Silent Reader
[Cek sider] Show Silent Reader
[Cancel] Cancel User
[Troops qr on] Open url Group
[Troops qr off] Close url Group
[View Service] View Bot Service
[Gcreator:Inv] Inv Group Creator
[Creator:inv] Invite Creator Bot
[Creator] Creator Bot 
[Gcreator] Group Creator

􀔃􀅕===[ Command Admin]===
[SetGroup] Setting Group Privacy
[Troops join] Beautiful girl join to the group
[Troops bye]  Leave Bot
[Mention All] Tag all user
[Protect On/Off] Protection Mode
[Kickjoin On/Off] Bitch Mode
[SMS ] Send a Private Message
======================
 Support by : 
T̶̸̘̟̼̉̈́͐͋͌̊E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑A̶̸̘̫͈̭͌͛͌̇̇̍M̶̸̘͈̺̪͓̺ͩ͂̾ͪ̀̋ B̶̸͎̣̫͈̥̗͒͌̃͑̔̾ͅO̶̸̜̓̇ͫ̉͊ͨS̶̸̪̭̱̼̼̉̈́ͪ͋̽̚E̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑N̶̸͉̠̙͉̗̺̋̔ͧ̊ K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑K̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅI̶̸̞̟̫̺ͭ̒ͭͣC̶̸͔ͣͦ́́͂ͅK̶̸̲̱̠̞̖ͧ̔͊̿̑ͯͅE̶̸̮̟͈̣̖̰̩̹͈̾ͨ̑͑R̶̸̼̯̤̗̲̞̥̈ͭ̃ͨ̆A̶̸̘̫͈̭͌͛͌̇̇̍N̶̸͉̠̙͉̗̺̋̔ͧ̊.
======================
"""
SetGroup =""" Privacy Menu 􀔃􀄆☣☣☣

[Reject Invite -- Cancel On / Off]
[Protect Cancel -- On / Off]
[Protect Qr -- On / Off]
[Protect Group -- Protect On/Off]
[Kicked if Join -- Kickjoin On/Off]
[Broadcast] Broadcast all group
[Copy @ ] Duplicate Profile
[/Leave (gid)] Left by ID
[/InviteMeTo (gid)] Invite Creator by ID
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["YOUR_MID_HERE"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"Chivas ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


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
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
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

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
<Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu
Skip to content
Pelajaran Sekolah Online

 
 MENU

 

Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap
By Si ManisPosted on March 12, 2017

 
Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi, Teori Kekekalan Energi  Beserta Contoh Soal Hukum Kekekalan Energi Terlengkap – Hukum Kekekalan Energi adalah hukum yang menyatakan bahwa jumlah energi dari sebuah sistem tertutup akan tetap sama tidak akan berubah. Energi tersebut tidak dapat diciptakan atau dimusnahkan, namun energi tersebut dapat berubah menjadi bentuk energi yang lain. Sebagai contohnya, energi kimia diubah menjadi energi kinetik dalam sebuah ledakan dinamit.
Contoh hukum kekekalan energi dalam kehidupan sehari-hari antara lain: buah jatuh dari pohon, lempar tangkap bola dan lain sebagianya.

Contents [hide]
1 Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
2 Teori Hukum Kekekalan Energi
3 Rumus Hukum Kekekalan Energi
4 Contoh Soal Hukum Kekekalan Energi
Bunyi Hukum Kekekalan Energi (Hukum I Termodinamika)
“Energi dapat diubah dari suatu bentuk ke bentuk lainnya tetapi tidak dapat diciptakan atau dimusnahkan (konversi energi).”

Teori Hukum Kekekalan Energi
Energi yang ada di alam semesta bersifat tetap, semua energi yang ada tidak dapat dimusnahkan dan hanya dapat diubah ke bentuk energi yang lain. Berbicara tentang energi, energi dibagi menjadi 2 yaitu energi mekanik dan energi kinetik.


 
Energi Kinetik adalah energi yang dimiliki suatu benda tertentu saat bergerak yang dinyatakan dengan satuan joule. Secara matematis, rumus energi kinetik yaitu:

Ek = ½ x mv2


 
Keterangan:
m : massa benda (kg)
v : kecepatan (m/s)

Ada 2 jenis energi kinetik yaitu Energi Kinetik Rotasi dan Energi Kinetik Relativistik.

Energi kinetik rotasi, apabila suatu objek tidak bergerak linear tapi berotasi. Rumus energi kinetik yang digunakan untuk objek yang berotasi yaitu:


 
Er = ½ x I x ω2

Keterangan:
I = momen inersia
ω = Kecepatan sudut

Energi kinetik relativistik, jika suatu objek bergerak relativistik maka rumus yang digunakan yaitu:

Ek = m γ c2 – mc2 


Keterangan:
c: kecepatan cahaya
m: massa objek

Contoh energi kinetik yaitu Kendaraan yang bergerak, planet yang mengelilingi matahari, orang mengetik komputer, bayi merangkak, orang berlari, orang berjalan dan lain sebagainya.

Energi Potensial adalah energi yang dimiliki suatu benda karena memiliki ketinggian tertentu. Satuan energi potensial yaitu joule. Energi potensial dirumuskan dengan:
Ep = m x g x h

Keterangan:
m : massa benda (kg)
g : percepatan grafitasi (m/s2)
h : tinggi benda dari permukaan tanah (m)

Jumlah dari energi potensial dan energi kinetik disebut dengan energi mekanik. Atau dituliskan:
Em = Ep + Ek

Rumus Hukum Kekekalan Energi
Em1 = Em2
Ek1 + Ep1 = Ek2 + Ep2

Keterangan:
Em1, Em2 = energi mekanik awal, energi mekanik akhir
Ek1, Ek2 = energi kinetik awal, energi kinetik akhir
Ep1, Ep2 = energi potensial awal, energi potensial akhir

Contoh Soal Hukum Kekekalan Energi
1. Buah kelapa bermassa 1,4 kg jatuh dari pohon dengan ketinggian 10 meter diatas tanah. (g= 10 m/s2). Tentukan:
a. Energi potensial dan energi kinetik mula-mula
b. Energi potensial dan energi kinetik pada saat ketinggian 5 meter Serta Kecepatan kelapa saat itu
c. Kecepatan saat menyentuh tanah.

Cara Penyelesaian:
































Demikian penjelasan yang bisa kami sampaikan tentang Pengertian Hukum Kekekalan Energi, Bunyi Hukum Kekekalan Energi Beserta Contoh Soal Terlengkap . Semoga postingan ini bermanfaat bagi pembaca

Lihat Artikel Lainnya
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
Pengertian Pengukuran dan Macam Macam Alat Ukur dalam Ilmu Fisika
Fisika Inti Dan Radioativitas – 11 Inti Induk dan Inti Baru radioaktivitas Beserta Rumus
Elastisitas Fisika – Pengertian, Rumus, Hukum Hooke, Dan Contoh Soal
Contoh Soal Dan Pembahasan Tentang Persamaan Gerak Lurus Dan Gerak Melingkar

 
Posted in FisikaTagged bunyi hukum kekekalan energi, bunyi hukum kekekalan energi mekanik, contoh hukum kekekalan energi dalam kehidupan sehari-hari, contoh soal hukum kekekalan energi, dasar teori hukum kekekalan energi, hukum energi, hukum kekekalan energi, hukum kekekalan energi dikemukakan oleh, hukum kekekalan energi mekanik, hukum kekekalan energi pdf, hukum kekelan energi, kekekalan energi, kekekalan energi mekanik, laporan hukum kekekalan energi, penemu hukum kekekalan energi, rumus hukum kekekalan energi, rumus kekekalan energi
Post navigation
Previous post
Asma – 12 Resep Tradisional Mengobati Asma Secara Alami, Ciri-Ciri dan Gejala Asma
Next post
Cara Mengobati Encok Secara Alami atau Sakit Pinggang Lengkap dengan Penyebab dan Pencegahannya
 

 
Recent Posts

 Pengertian Hak Cipta, Ciri-Ciri, Fungsi, Sifat dan Dasar Hukum Hak Cipta Terlengkap
 Pengertian Desain, Fungsi, Tujuan, Manfaat, Prinsip, Metode dan Jenis Cabang Seni Desain Terlengkap
 Pengertian Ebook (Buku Digital), Fungsi, Manfaat, Tujuan, Format, Kelebihan dan Kekurangan Ebook Terlengkap
 Pengertian Kinerja, Indikator dan Faktor Yang Mempengaruhi Kinerja Menurut Para Ahli
 Pengertian Himpunan, Cara Penyelesaian, Macam dan Contoh Soal Himpunan Beserta Pembahasan Lengkap
 Teks Tanggapan Kritis: Pengertian, Ciri, Kaidah Kebahasaan, Struktur, Contoh Teks Tanggapan Kritis Beserta Strukturnya
 Sejarah Lengkap Kerajaan Majapahit, Raja, Kehidupan Politik, Peninggalan, Masa Kejayaan dan Keruntuhan Kerajaan Majapahit
 Teks Eksplanasi: Pengertian, Tujuan, Ciri, Struktur, Kaidah Kebahasaan, Contoh Teks Ekplanasi Beserta Strukturnya
 Sejarah Lengkap BPUPKI, Pengertian, Tujuan, Anggota, Tugas dan Sidang BPUPKI
 Sejarah Lengkap Kerajaan Kediri, Raja, Peninggalan, Kehidupan, Masa Kejayaan dan Keruntuhan Kerajaan Kediri

 
PelajaranSekolahOnline.Com 

Science Blogs

 Academics 

 Feedage Grade A rated
Hot Artikel

Pengertian Peta dan Cara Mudah Menghitung Skala Pada Peta
Pengertian, Rumus Momen Inersia, Contoh Soal dan Pembahasan Momen Inersia Terlengkap
Contoh Teks Pengumuman Resmi dan Pengumuman Tak resmi Lengkap
3 Cara Membuat Magnet Sederhana Dengan Cara Menggosok, Induksi dan Arus Listrik
34 Nama Rumah Adat ,Pakaian,Tarian Adat dan Senjata Tradisional di Provinsi Indonesia Lengkap
Materi Lengkap Trigonometri Dengan Fungsi , Rumus Dan Pembahasan Contoh Soal
1914 Kumpulan Kata Kata Bijak Motivasi TerUPDATE
25 Pengertian HAM Hak Asasi Manusia Menurut Pendapat Para Ahli Terlengkap

 
Copyright © 2017 | Powered By Team Pelajaran.Co.Id
Home
IPS
Sejarah
Geografi
IPA
Kimia
Biologi
Fisika
Matematika
Agama
Bahasa
Bahasa Indonesia
Bahasa Inggris
Tips dan Trik
Komputer
Kesehatan
Olahraga

Search
Close Menu