# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate
from gtts import gTTS


cl = LINETCR.LINE() 
#cl.login(qr=True)
cl.login(token="")#1
cl.loginResult()

ki = LINETCR.LINE() 
#ki.login(qr=True)
ki.login(token="")#2
ki.loginResult()

kk = LINETCR.LINE() 
#kk.login(qr=True)
kk.login(token="")#3
kk.loginResult()

kc = LINETCR.LINE()
#kc.login(qr=True)
kc.login(token="")#4
kc.loginResult()

ks = LINETCR.LINE() 
#ks.login(qr=True)
ks.login(token="")#5
ks.loginResult()

k1 = LINETCR.LINE() 
#k1.login(qr=True)
k1.login(token="")#6
k1.loginResult()

k2 = LINETCR.LINE() 
#k2.login(qr=True)
k2.login(token="")#7
k2.loginResult()

k3 = LINETCR.LINE() #
#k3.login(qr=True)
k3.login(token="")#8
k3.loginResult()

k4 = LINETCR.LINE() #
#k4.login(qr=True)
k4.login(token="")#9
k4.loginResult()

k5 = LINETCR.LINE() #
#k5.login(qr=True)
k5.login(token="")#10
k5.loginResult()

k6 = LINETCR.LINE()
#k6.login(qr=True)
k6.login(token="")#1
k6.loginResult()

k7 = LINETCR.LINE()
#k7.login(qr=True)
k7.login(token="")#2
k7.loginResult()

k8 = LINETCR.LINE()
#k8.login(qr=True)
k8.login(token="")#3
k8.loginResult()

k9 = LINETCR.LINE()
#k9.login(qr=True)
k9.login(token="")#4
k9.loginResult()

k10 = LINETCR.LINE()
#k10.login(qr=True)
k10.login(token="")#5
k10.loginResult()

k11 = LINETCR.LINE()
#k11.login(qr=True)
k11.login(token="")#6
k11.loginResult()

k12 = LINETCR.LINE() 
#k12.login(qr=True)
k12.login(token="")#7
k12.loginResult()

k13 = LINETCR.LINE() 
#k13.login(qr=True)
k13.login(token="")#8
k13.loginResult()

k14 = LINETCR.LINE()
#k14.login(qr=True)
k14.login(token="")#1.5b
k14.loginResult()

k15 = LINETCR.LINE()
#k15.login(qr=True)
k15.login(token="")
k15.loginResult()

k16 = LINETCR.LINE()
#k16.login(qr=True)
k16.login(token="")
k16.loginResult()

k17 = LINETCR.LINE()
#k17.login(qr=True)
k17.login(token="")
k17.loginResult()

k18 = LINETCR.LINE()
#k18.login(qr=True)
k18.login(token="")
k18.loginResult()

k19 = LINETCR.LINE() 
#k19.login(qr=True)
k19.login(token="")#1.2
k19.loginResult()

k20 = LINETCR.LINE() 
#k20.login(qr=True)
k20.login(token="")#1.2
k20.loginResult()

satpam1 = LINETCR.LINE() # 
satpam1.login(token="")#satpam 
#satpam1.login(qr=True)
satpam1.loginResult()

k19 = k20 = k18

print "login success bos"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔═════════════
║     ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
╠═════════════
║           Owner : Kris       
╠═════════════
║   ◄]·♦·Menu For Public·♦·[►
║╔════════════
║╠[•]Help
║╠[•]Key
║╠[•]Mimin
║╠[•]Creator
║╠[•]Time
║╠════════════
║╠[•]Say....
║╠[•]Wkwkwk/Wkwk/Wk
║╠[•]Hehehe/Hehe/He
║╠[•]Galau
║╠[•]You
║╠[•]Hadeuh
║╠[•]Please
║╠[•]Haaa
║╠[•]Lol
║╠[•]Hmmm/Hmm/Hm
║╠[•]Welcome
║╠[•]Woy
║╠════════════
║╠[•]Wiki 
║╠[•]Lyric
║╠[•]Instagram
║╠[•]Music
║╠[•]Youtube
║╠[•]Vidio
║╠════════════
║╠[•]Bc
║╠[•]Up
║╠[•]Berapa besar cinta
║╠[•]Apakah
║╠[•]Siapakah cewek 
║╠[•]Siapakah cowok
║╠[•]Adakah
║╠[•]Cakepkah
║╠════════════
║╠[•]T-eng
║╠[•]T-japan 
║╠[•]T-thai
║╠[•]T-id
║╚════════════
║     ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╚═════════════
"""
Keyowner ="""
╔═════════════
║       ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
╠═════════════
║                    Owner : Kris       
╠═════════════
║   ◄]·♦·Menu For Admin·♦·[►
║╔════════════
║╠[•]Kick ...
║╠[•]Invite (by mid)
║╠[•]Undang (Invite by kontak)
║╠[•]Tarik/Jepit (Invite by kontak)
║╠[•]Adminlist
║╠[•]Bot Add @
║╠[•]Spam... (spam on 10 tes)
║╠[•]Bot? (cek kontak bot)
║╠[•]Cancel (cncl undngn trtunda)
║╠[•]clean invites
║╠[•]clear invites
║╠════════════
║╠[•]Message change:...
║╠[•]Message add:...
║╠[•]Message
║╠[•]Comment:...
║╠[•]Add comment:...
║╠════════════
║╠[•]Jam on/off
║╠[•]Change clock
║╠[•]Jam Update
║╠════════════
║╠[•]Status (cek status room)
║╠[•]Cctv
║╠[•]Intip
║╠[•]Toong
║╠[•]Nk
║╠[•]Tajong
║╠[•]Vkick
║╠[•]Emak/Abah
║╠[•]Kill
║╠[•]Absen/Respon
║╠════════════
║╠[•]Ifconfig
║╠[•]System
║╠[•]Cpu
║╠[•]Kernel
║╠[•]Debug speed
║╠[•]Bot speed
║╠[•]Speed respon
║╠[•]Sp turunin
║╠[•]Sp naikin
║╠[•]Turun lagi
║╠[•]Spbot
║╠[•]Sp asli
║╠[•]Speedbot
║╠[•]Speed
║╚════════════
║     ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╚═════════════
"""
Setgroup ="""
╔═════════════
║       ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
╠═════════════
║                    Owner : Kris       
╠═════════════
║   ◄]·♦·Menu For Admin·♦·[►
║╔════════════
║╠[•]Cancel
║╠[•]Buka qr/Open qr
║╠[•]link open
║╠[•]Tutup qr/Close qr
║╠[•]link close
║╠[•]Rejectall (reject semua invite)
║╠[•]Protect:hight/low
║╠[•]Auto blockqr:off/on
║╠[•]Namelock:on/off
║╠[•]Blockinvite:on/off
║╠[•]Joinn on/off (kick protect join)
║╠[•]Cancel on/off(cncl all undngan)
║╠[•]Qr on/off (protect qr)
║╠[•]Contact On/off
║╠[•]Join on/off (auto join bot)
║╠[•]Gcancel:on/off (invite grup)
║╠[•]Leave on/off
║╠[•]Share on/off
║╠[•]Add on/off
║╠[•]Cancelall (canccel all invite)
║╠[•]Comment off/on
║╠[•]Backup:on/off
║╠[•]Mode on
║╠════════════
║╠[•]Info Group
║╠[•]ginfo
║╠[•]Group id
║╠[•]TL:....
║╠[•]Gn
║╠[•]LG
║╠[•]LG2
║╠[•]group list
║╠════════════
║╠[•]My mid
║╠[•]Mid Bot
║╠[•]Bot restart
║╠[•]Turn off bots
║╠[•]Allbio: (ganti bio stat bot)
║╠[•]Myname: (ganti nama bot)
║╠════════════
║╠[•]Banlist
║╠[•]Cek ban
║╠[•]Kill ban
║╠[•]Blacklist @ 
║╠[•]Banned @
║╠[•]Mid @"
║╠[•]Unban @
║╠[•]Ban
║╠[•]Unban
║╠════════════
║╠[•]Steal group pict
║╠[•]Steal cover @
║╠[•]Midpict:..
║╠[•]Steal pict 
║╠[•]Steal bio
║╠[•]Steal mid
║╠[•]Steal contact
║╠[•]Mimic on/off
║╠[•]Targetlist
║╠[•]Mimic target
║╠[•]Target @
║╠[•]Del target @
║╠[•]copy @
║╠[•]Backup
║╠════════════
║╠[•]Spamcontact @
║╠[•]GBc
║╠[•]Pm cast
║╠[•]Bot like
║╠════════════
║╠[•]One piece
║╠[•]Kabur all
║╠[•]Kabur
║╠[•]Bot kadieu
║╠[•]Asupka:
║╠[•]Invite me
║╠════════════
║╠[•]Remove all chat
║╠[•]Admin add @ (by tag)
║╠[•]Admin remove @
║╠[•]Cleanse
║╠[•]Ready op
║╠[•]Greet
║╚════════════
║👑Hanya Utk Owner/Admin👑
╠═════════════
║     ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╚═════════════
"""
KAC=[cl,ki,kk,kc,ks,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
DEF=[ki,kk,kc,ks,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
kicker=[satpam1]
mid = cl.getProfile().mid 
Amid = ki.getProfile().mid 
Bmid = kk.getProfile().mid 
Cmid = kc.getProfile().mid 
Dmid = ks.getProfile().mid 
Emid = k1.getProfile().mid
Fmid = k2.getProfile().mid
Gmid = k3.getProfile().mid
Hmid = k4.getProfile().mid
Imid = k5.getProfile().mid
Jmid = k6.getProfile().mid
Kmid = k7.getProfile().mid
Lmid = k8.getProfile().mid
Mmid = k9.getProfile().mid
Nmid = k10.getProfile().mid
Omid = k11.getProfile().mid
Pmid = k12.getProfile().mid
Qmid = k13.getProfile().mid
Rmid = k14.getProfile().mid
Smid = k15.getProfile().mid
Tmid = k16.getProfile().mid
Umid = k17.getProfile().mid
Vmid = k18.getProfile().mid
Wmid = k19.getProfile().mid
Xmid = k20.getProfile().mid
Smid1 = satpam1.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,Umid,Vmid,Wmid,Xmid]
induk=[mid]
Creator=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,Umid,Vmid,Wmid,Xmid] #Krisna,kris,
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
>>✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰<<
≫ bot protect ≪
≫ SelfBot ≪
ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ FS3I FAMILY ☆
✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
☆ ONE PIECE BOT PROTECT ☆
Idline: http://line.me/ti/p/GkwfNjoPDH""",
    "lang":"JP",
    "comment":"👉ąµţ๏ℓɨЌ€ By😊\n☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "namelock":True,
    "Backup":False,
    "AutoKick":True,
    "Mimic":False,
    "pname":True,
    "qr":True,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "Protectcancel":True,
    "winvite":False,
    "winvite2":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

wait3 = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
profile = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
profile = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
profile = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
profile = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
profile = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k1.getProfile()
backup = k1.getProfile()
profile = k1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k2.getProfile()
backup = k2.getProfile()
profile = k2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k3.getProfile()
backup = k3.getProfile()
profile = k3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k4.getProfile()
backup = k4.getProfile()
profile = k4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k5.getProfile()
backup = k5.getProfile()
profile = k5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k6.getProfile()
backup = k6.getProfile()
profile = k6.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k7.getProfile()
backup = k7.getProfile()
profile = k7.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k8.getProfile()
backup = k8.getProfile()
profile = k8.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k9.getProfile()
backup = k9.getProfile()
profile = k9.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k10.getProfile()
backup = k10.getProfile()
profile = k10.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k11.getProfile()
backup = k11.getProfile()
profile = k11.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k12.getProfile()
backup = k12.getProfile()
profile = k12.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k13.getProfile()
backup = k13.getProfile()
profile = k13.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k14.getProfile()
backup = k14.getProfile()
profile = k14.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k15.getProfile()
backup = k15.getProfile()
profile = k15.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k16.getProfile()
backup = k16.getProfile()
profile = k16.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k17.getProfile()
backup = k17.getProfile()
profile = k17.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k18.getProfile()
backup = k18.getProfile()
profile = k18.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k19.getProfile()
backup = k19.getProfile()
profile = k19.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k20.getProfile()
backup = k20.getProfile()
profile = k20.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def mention2(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def MENTION(to,nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nama:
     akh = akh + 2
     aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
     strt = strt + 6
     akh = akh + 4
     bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[COMMAND] Tag All"
    try:
      cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
          with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
      else:
          raise Exception('Download Audio failure.')
      try:
          self.sendAudio(to_, path)
      except Exception as e:
        print e

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)       
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True

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
                    
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += '\n ☞ ' + Name
                    wait2['ROM'][op.param1][op.param2] = '☞ ' + Name
            else:
                pass
              
#-------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass
#------------------------------------------
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
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ks.getGroup(op.param1)
				    except:
					try:
                                            G = k1.getGroup(op.param1)
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
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ks.updateGroup(G)
                                    except:
                                        try:
                                            k1.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        kk.sendText(op.param1,"please do not change group name-_-")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  X = cl.getGroup(op.param1)
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)
        #------Protect Group Kick finish-----#
        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              try:
                random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              except:
                random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Creator:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Creator:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Creator:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Creator:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Creator:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Creator:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Creator:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Creator:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Creator:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Creator:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Creator:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Creator:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Creator:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Creator:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Creator:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Creator:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Creator:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Creator:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Creator:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Creator:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Creator:
		    k20.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Dmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Emid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Fmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Gmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Hmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Imid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Jmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Kmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Lmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Mmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Nmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Omid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Pmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Qmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Rmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Smid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Tmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Umid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Vmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Wmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Xmid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Dmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Emid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Fmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Gmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Hmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Imid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Jmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Kmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Lmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Mmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Nmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Omid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Pmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Qmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Rmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Smid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Tmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Umid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Vmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Wmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Xmid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Dmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Emid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Fmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Gmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Hmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Imid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Jmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Kmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Lmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Mmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Nmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Omid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Pmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Qmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Rmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Smid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Tmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Umid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Vmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Wmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Xmid:
		    kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Dmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Emid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Fmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Gmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Hmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Imid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Jmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Kmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Lmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Mmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Nmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Omid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Pmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Qmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Rmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Smid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Tmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Umid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Vmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Wmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Xmid:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Dmid:
		if op.param2 in mid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Amid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Bmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Cmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Emid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Fmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Gmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Hmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Imid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Jmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Kmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Lmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Mmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Nmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Omid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Pmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Qmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Rmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Smid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Tmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Umid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Vmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Wmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Xmid:
		    ks.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Emid:
		if op.param2 in mid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Amid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Bmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Cmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Dmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Fmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Gmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Hmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Imid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Jmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Kmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Lmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Mmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Nmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Omid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Pmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Qmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Rmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Smid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Tmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Umid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Vmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Wmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Xmid:
		    k1.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Fmid:
		if op.param2 in mid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Amid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Bmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Cmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Dmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Emid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Gmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Hmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Imid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Jmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Kmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Lmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Mmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Nmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Omid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Pmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Qmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Rmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Smid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Tmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Umid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Vmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Wmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Xmid:
		    k2.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Gmid:
		if op.param2 in mid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Amid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Bmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Cmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Dmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Emid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Fmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Hmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Imid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Jmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Kmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Lmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Mmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Nmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Omid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Pmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Qmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Rmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Smid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Tmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Umid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Vmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Wmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Xmid:
		    k3.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Hmid:
		if op.param2 in mid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Amid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Bmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Cmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Dmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Emid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Fmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Gmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Imid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Jmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Kmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Lmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Mmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Nmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Omid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Pmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Qmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Rmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Smid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Tmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Umid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Vmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Wmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Xmid:
		    k4.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Imid:
		if op.param2 in mid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Amid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Bmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Cmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Dmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Emid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Fmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Gmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Hmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Jmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Kmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Lmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Mmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Nmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Omid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Pmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Qmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Rmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Smid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Tmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Umid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Vmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Wmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Xmid:
		    k5.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Jmid:
		if op.param2 in mid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Amid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Bmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Cmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Dmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Emid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Fmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Gmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Hmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Imid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Kmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Lmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Mmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Nmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Omid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Pmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Qmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Rmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Smid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Tmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Umid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Vmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Wmid:
		    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		if op.param2 in Xmid:
		    k6.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Kmid:
		if op.param2 in mid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Amid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Bmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Cmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Dmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Emid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Fmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Gmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Hmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Imid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Jmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Lmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Mmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Nmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Omid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Pmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Qmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Rmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Smid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Tmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Umid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Vmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Wmid:
		    k7.acceptGroupInvitation(op.param1)
            if op.param3 in Kmid:
		if op.param2 in Xmid:
		    k7.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Lmid:
		if op.param2 in mid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Amid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Bmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Cmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Dmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Emid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Fmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Gmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Hmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Imid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Jmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Kmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Mmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Nmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Omid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Pmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Qmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Rmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Smid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Tmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Umid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Vmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Wmid:
		    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Lmid:
		if op.param2 in Xmid:
		    k8.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Mmid:
		if op.param2 in mid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Amid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Bmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Cmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Dmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Emid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Fmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Gmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Hmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Imid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Jmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Kmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Lmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Nmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Omid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Pmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Qmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Rmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Smid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Tmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Umid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Vmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Wmid:
		    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Mmid:
		if op.param2 in Xmid:
		    k9.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Nmid:
		if op.param2 in mid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Amid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Bmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Cmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Dmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Emid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Fmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Gmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Hmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Imid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Jmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Kmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Lmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Mmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Omid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Pmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Qmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Rmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Smid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Tmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Umid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Vmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Wmid:
		    k10.acceptGroupInvitation(op.param1)
            if op.param3 in Nmid:
		if op.param2 in Xmid:
		    k10.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Omid:
		if op.param2 in mid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Amid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Bmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Cmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Dmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Emid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Fmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Gmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Hmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Imid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Jmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Kmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Lmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Mmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Nmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Pmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Qmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Rmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Smid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Tmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Umid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Vmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Wmid:
		    k11.acceptGroupInvitation(op.param1)
            if op.param3 in Omid:
		if op.param2 in Xmid:
		    k11.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Pmid:
		if op.param2 in mid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Amid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Bmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Cmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Dmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Emid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Fmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Gmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Hmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Imid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Jmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Kmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Lmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Mmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Nmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Omid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Qmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Rmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Smid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Tmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Umid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Vmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Wmid:
		    k12.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
		if op.param2 in Xmid:
		    k12.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Qmid:
		if op.param2 in mid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Amid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Bmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Cmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Dmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Emid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Fmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Gmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Hmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Imid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Jmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Kmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Lmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Mmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Nmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Omid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Pmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Rmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Smid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Tmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Umid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Vmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Wmid:
		    k13.acceptGroupInvitation(op.param1)
            if op.param3 in Qmid:
		if op.param2 in Xmid:
		    k13.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Rmid:
		if op.param2 in mid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Amid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Bmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Cmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Dmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Emid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Fmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Gmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Hmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Imid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Jmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Kmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Lmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Mmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Nmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Omid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Pmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Qmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Smid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Tmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Umid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Vmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Wmid:
		    k14.acceptGroupInvitation(op.param1)
            if op.param3 in Rmid:
		if op.param2 in Xmid:
		    k14.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Smid:
		if op.param2 in mid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Amid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Bmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Cmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Dmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Emid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Fmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Gmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Hmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Imid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Jmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Kmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Lmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Mmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Nmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Omid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Pmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Qmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Rmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Tmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Umid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Vmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Wmid:
		    k15.acceptGroupInvitation(op.param1)
            if op.param3 in Smid:
		if op.param2 in Xmid:
		    k15.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Tmid:
		if op.param2 in mid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Amid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Bmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Cmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Dmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Emid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Fmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Gmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Hmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Imid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Jmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Kmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Lmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Mmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Nmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Omid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Pmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Qmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Rmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Smid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Umid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Vmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Wmid:
		    k16.acceptGroupInvitation(op.param1)
            if op.param3 in Tmid:
		if op.param2 in Xmid:
		    k16.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Umid:
		if op.param2 in mid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Amid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Bmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Cmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Dmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Emid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Fmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Gmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Hmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Imid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Jmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Kmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Lmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Mmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Nmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Omid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Pmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Qmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Rmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Smid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Tmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Vmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Wmid:
		    k17.acceptGroupInvitation(op.param1)
            if op.param3 in Umid:
		if op.param2 in Xmid:
		    k17.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Vmid:
		if op.param2 in mid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Amid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Bmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Cmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Dmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Emid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Fmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Gmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Hmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Imid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Jmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Kmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Lmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Mmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Nmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Omid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Pmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Qmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Rmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Smid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Tmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Umid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Wmid:
		    k18.acceptGroupInvitation(op.param1)
            if op.param3 in Vmid:
		if op.param2 in Xmid:
		    k18.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Wmid:
		if op.param2 in mid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Amid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Bmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Cmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Dmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Emid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Fmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Gmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Hmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Imid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Jmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Kmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Lmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Mmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Nmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Omid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Pmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Qmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Rmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Smid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Tmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Umid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Vmid:
		    k19.acceptGroupInvitation(op.param1)
            if op.param3 in Wmid:
		if op.param2 in Xmid:
		    k19.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Xmid:
		if op.param2 in mid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Amid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Bmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Cmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Dmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Emid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Fmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Gmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Hmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Imid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Jmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Kmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Lmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Mmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Nmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Omid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Pmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Qmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Rmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Smid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Tmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Umid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Vmid:
		    k20.acceptGroupInvitation(op.param1)
            if op.param3 in Xmid:
		if op.param2 in Wmid:
		    k20.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
#-------------------------------------------------------- 
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k1.acceptGroupInvitation(op.param1)
                else:
                  k1.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Fmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k2.acceptGroupInvitation(op.param1)
                else:
                  k2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Gmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k3.acceptGroupInvitation(op.param1)
                else:
                  k3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Hmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k4.acceptGroupInvitation(op.param1)
                else:
                  k4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Imid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k5.acceptGroupInvitation(op.param1)
                else:
                  k5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Jmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k6.acceptGroupInvitation(op.param1)
                else:
                  k6.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Kmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k7.acceptGroupInvitation(op.param1)
                else:
                  k7.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Lmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k8.acceptGroupInvitation(op.param1)
                else:
                  k8.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Mmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k9.acceptGroupInvitation(op.param1)
                else:
                  k9.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Nmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k9.acceptGroupInvitation(op.param1)
                else:
                  k9.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
#-------------------------------------------------------- 
        if op.type == 17:
          if wait["Protectjoin"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
        #------Joined User Kick start------#
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                random.choice(KAC).sendText(op.param1, "Jangan di cancel woy...!!!\nAdmin Bukan,Owner Juga Bukan\Kick Ah 😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2]) 
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
		            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    kk.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		
#-----------------------------------------------------------------
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
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
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
			k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ks.updateGroup(G)
                    Ti = ks.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
			k2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k1.updateGroup(G)
                    Ti = k1.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
			k3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k2.updateGroup(G)
                    Ti = k2.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k1.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
			k4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k3.updateGroup(G)
                    Ti = k3.reissueGroupTicket(op.param1)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k2.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
			k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k4.updateGroup(G)
                    Ti = k4.reissueGroupTicket(op.param1)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k3.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
			k6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k5.updateGroup(G)
                    Ti = k5.reissueGroupTicket(op.param1)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k4.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
			k7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k6.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k6.updateGroup(G)
                    Ti = k6.reissueGroupTicket(op.param1)
                    k5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k5.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
			k8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k7.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k7.updateGroup(G)
                    Ti = k7.reissueGroupTicket(op.param1)
                    k6.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k6.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Kmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
			k9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k8.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k8.updateGroup(G)
                    Ti = k8.reissueGroupTicket(op.param1)
                    k7.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k7.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Lmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
			k10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k9.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k9.updateGroup(G)
                    Ti = k9.reissueGroupTicket(op.param1)
                    k8.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k8.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Mmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
			k11.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k10.updateGroup(G)
                    Ti = k10.reissueGroupTicket(op.param1)
                    k9.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k9.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k11.kickoutFromGroup(op.param1,[op.param2])
			k12.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k11.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k11.updateGroup(G)
                    Ti = k11.reissueGroupTicket(op.param1)
                    k10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k10.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Omid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
			k13.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k12.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k12.updateGroup(G)
                    Ti = k12.reissueGroupTicket(op.param1)
                    k11.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k11.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k11.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k13.kickoutFromGroup(op.param1,[op.param2])
			k14.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k13.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k13.updateGroup(G)
                    Ti = k13.reissueGroupTicket(op.param1)
                    k12.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k12.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k12.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Qmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k14.kickoutFromGroup(op.param1,[op.param2])
			k15.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k14.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k14.updateGroup(G)
                    Ti = k14.reissueGroupTicket(op.param1)
                    k13.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k13.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k13.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Rmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k15.kickoutFromGroup(op.param1,[op.param2])
			k16.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k15.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k15.updateGroup(G)
                    Ti = k15.reissueGroupTicket(op.param1)
                    k14.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k14.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k14.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Smid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k16.kickoutFromGroup(op.param1,[op.param2])
			k17.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k16.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k16.updateGroup(G)
                    Ti = k16.reissueGroupTicket(op.param1)
                    k15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k15.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k15.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Tmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k17.kickoutFromGroup(op.param1,[op.param2])
			k18.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k17.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k17.updateGroup(G)
                    Ti = k17.reissueGroupTicket(op.param1)
                    k16.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k16.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k16.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Umid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k18.kickoutFromGroup(op.param1,[op.param2])
			k19.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k18.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k18.updateGroup(G)
                    Ti = k18.reissueGroupTicket(op.param1)
                    k17.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k17.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k17.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Vmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k19.kickoutFromGroup(op.param1,[op.param2])
			k20.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k19.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k19.updateGroup(G)
                    Ti = k19.reissueGroupTicket(op.param1)
                    k18.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k18.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k18.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Wmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k20.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k20.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k20.updateGroup(G)
                    Ti = k20.reissueGroupTicket(op.param1)
                    k19.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k19.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k19.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Xmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    k20.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = k20.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    k20.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------------------------------------
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True

        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  k1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True

        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in mid:
              if op.param2 not in Bots:
                try:
                  random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(DEF).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(DEF).updateGroup(G)
                  Ticket = random.choice(DEF).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(DEF).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(DEF).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True

#-----------------------------------------------
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in Bots:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
#--------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


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
                        ks.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        ks.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        ks.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")
                        ks.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        ks.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        ks.sendText(msg.to,"It is not in the black list")
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
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Key","key"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Keyowner)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Mimin","mimin"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
#===========================================
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          random.choice(KAC).sendText(op.param1, "|============================|\n Selamat Datang Di  " + str(ginfo.name) + "\n|============================|\n" + " Founder =>>> " + str(ginfo.name) + " :\n" + ginfo.creator.displayName + "\n|============================|\n" + " 😊Semoga Betah Kak 😘 \n|============================|\n No Baper,No nakal,No Ngeyel ya..!! \n|============================|")
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "|============================|\n Baper Tuh Orang :v \n|============================|\n Belum di Anu Kayanya 😊 \n|============================|")
          print "MEMBER HAS LEFT THE GROUP"
#--------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite2"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = random.choice(KAC).getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 random.choice(KAC).sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 random.choice(KAC).sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 random.choice(KAC).sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     random.choice(KAC).findAndAddContactsByMid(target)
                                     random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                     wait["winvite2"] = False
                                     break
                                 except:
                                     try:
                                         random.choice(KAC).findAndAddContactsByMid(invite)
                                         random.choice(KAC).inviteIntoGroup(op.param1,[invite])
                                         wait["winvite2"] = False
                                     except:
                                         random.choice(KAC).sendText(msg.to,"Error Boss, di tunggu beberapa saat lagi boss")
                                         wait["winvite2"] = False
                                         break

            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = k1.getGroup(msg.to)
                gs = k2.getGroup(msg.to)
                gs = k3.getGroup(msg.to)
                gs = k4.getGroup(msg.to)
                gs = k5.getGroup(msg.to)
                gs = k6.getGroup(msg.to)
                gs = k7.getGroup(msg.to)
                gs = k8.getGroup(msg.to)
                gs = k9.getGroup(msg.to)
                gs = k10.getGroup(msg.to)
                gs = k11.getGroup(msg.to)
                gs = k12.getGroup(msg.to)
                gs = k13.getGroup(msg.to)
                gs = k14.getGroup(msg.to)
                gs = k15.getGroup(msg.to)
                gs = k16.getGroup(msg.to)
                gs = k17.getGroup(msg.to)
                gs = k18.getGroup(msg.to)
                gs = k19.getGroup(msg.to)
                gs = k20.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = k1.getGroup(msg.to)
                gs = k2.getGroup(msg.to)
                gs = k3.getGroup(msg.to)
                gs = k4.getGroup(msg.to)
                gs = k5.getGroup(msg.to)
                gs = k6.getGroup(msg.to)
                gs = k7.getGroup(msg.to)
                gs = k8.getGroup(msg.to)
                gs = k9.getGroup(msg.to)
                gs = k10.getGroup(msg.to)
                gs = k11.getGroup(msg.to)
                gs = k12.getGroup(msg.to)
                gs = k13.getGroup(msg.to)
                gs = k14.getGroup(msg.to)
                gs = k15.getGroup(msg.to)
                gs = k16.getGroup(msg.to)
                gs = k17.getGroup(msg.to)
                gs = k18.getGroup(msg.to)
                gs = k19.getGroup(msg.to)
                gs = k20.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = k1.getGroup(msg.to)
                  gs = k2.getGroup(msg.to)
                  gs = k3.getGroup(msg.to)
                  gs = k4.getGroup(msg.to)
                  gs = k5.getGroup(msg.to)
                  gs = k6.getGroup(msg.to)
                  gs = k7.getGroup(msg.to)
                  gs = k8.getGroup(msg.to)
                  gs = k9.getGroup(msg.to)
                  gs = k10.getGroup(msg.to)
                  gs = k11.getGroup(msg.to)
                  gs = k12.getGroup(msg.to)
                  gs = k13.getGroup(msg.to)
                  gs = k14.getGroup(msg.to)
                  gs = k15.getGroup(msg.to)
                  gs = k16.getGroup(msg.to)
                  gs = k17.getGroup(msg.to)
                  gs = k18.getGroup(msg.to)
                  gs = k19.getGroup(msg.to)
                  gs = k20.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        k1.findAndAddContactsByMid(target)
                        k2.findAndAddContactsByMid(target)
                        k3.findAndAddContactsByMid(target)
                        k4.findAndAddContactsByMid(target)
                        k5.findAndAddContactsByMid(target)
                        k6.findAndAddContactsByMid(target)
                        k7.findAndAddContactsByMid(target)
                        k8.findAndAddContactsByMid(target)
                        k9.findAndAddContactsByMid(target)
                        k10.findAndAddContactsByMid(target)
                        k11.findAndAddContactsByMid(target)
                        k12.findAndAddContactsByMid(target)
                        k13.findAndAddContactsByMid(target)
                        k14.findAndAddContactsByMid(target)
                        k15.findAndAddContactsByMid(target)
                        k16.findAndAddContactsByMid(target)
                        k17.findAndAddContactsByMid(target)
                        k18.findAndAddContactsByMid(target)
                        k19.findAndAddContactsByMid(target)
                        k20.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")                
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k6.getProfile()
                    profile.statusMessage = string
                    k6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k7.getProfile()
                    profile.statusMessage = string
                    k7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k8.getProfile()
                    profile.statusMessage = string
                    k8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k9.getProfile()
                    profile.statusMessage = string
                    k9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k10.getProfile()
                    profile.statusMessage = string
                    k10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k11.getProfile()
                    profile.statusMessage = string
                    k11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k12.getProfile()
                    profile.statusMessage = string
                    k12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k13.getProfile()
                    profile.statusMessage = string
                    k13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k14.getProfile()
                    profile.statusMessage = string
                    k14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k15.getProfile()
                    profile.statusMessage = string
                    k15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k16.getProfile()
                    profile.statusMessage = string
                    k16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k17.getProfile()
                    profile.statusMessage = string
                    k17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k18.getProfile()
                    profile.statusMessage = string
                    k18.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k19.getProfile()
                    profile.statusMessage = string
                    k19.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k20.getProfile()
                    profile.statusMessage = string
                    k20.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k6.getProfile()
                    profile.displayName = string
                    k6.updateProfile(profile)
                    k6.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k7.getProfile()
                    profile.displayName = string
                    k7.updateProfile(profile)
                    k7.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k8.getProfile()
                    profile.displayName = string
                    k8.updateProfile(profile)
                    k8.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k9.getProfile()
                    profile.displayName = string
                    k9.updateProfile(profile)
                    k9.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k10.getProfile()
                    profile.displayName = string
                    k10.updateProfile(profile)
                    k10.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k11.getProfile()
                    profile.displayName = string
                    k11.updateProfile(profile)
                    k11.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k12.getProfile()
                    profile.displayName = string
                    k12.updateProfile(profile)
                    k12.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k13.getProfile()
                    profile.displayName = string
                    k13.updateProfile(profile)
                    k13.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k14.getProfile()
                    profile.displayName = string
                    k14.updateProfile(profile)
                    k14.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k15.getProfile()
                    profile.displayName = string
                    k15.updateProfile(profile)
                    k15.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k16.getProfile()
                    profile.displayName = string
                    k16.updateProfile(profile)
                    k16.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k17.getProfile()
                    profile.displayName = string
                    k17.updateProfile(profile)
                    k17.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k18.getProfile()
                    profile.displayName = string
                    k18.updateProfile(profile)
                    k18.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k19.getProfile()
                    profile.displayName = string
                    k19.updateProfile(profile)
                    k19.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k20.getProfile()
                    profile.displayName = string
                    k20.updateProfile(profile)
                    k20.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam " in msg.text:
              if msg.from_ in admin and owner:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                k1.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                k2.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                k3.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                k4.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                k5.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                k6.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Kmid}
                k7.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                k8.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                k9.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                k10.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                k11.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                k12.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                k13.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                k14.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                k15.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                k16.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Umid}
                k17.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Vmid}
                k18.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Wmid}
                k19.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Xmid}
                k20.sendMessage(msg)
                
#====================================================
            elif msg.text.lower() == "crash":
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "c33b66e4b7709e54a6fe6eced6e57c157',"}
                cl.sendMessage(msg)
#====================================================
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = ks.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ks.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ks.sendText(msg.to,"No one is inviting")
                        else:
                            ks.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ks.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
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
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                k1.sendText(msg.to,Emid)
                k2.sendText(msg.to,Fmid)
                k3.sendText(msg.to,Gmid)
                k4.sendText(msg.to,Hmid)
                k5.sendText(msg.to,Imid)
                k6.sendText(msg.to,Jmid)
                k7.sendText(msg.to,Kmid)
                k8.sendText(msg.to,Lmid)
                k9.sendText(msg.to,Mmid)
                k10.sendText(msg.to,Nmid)
                k11.sendText(msg.to,Omid)
                k12.sendText(msg.to,Pmid)
                k13.sendText(msg.to,Qmid)
                k14.sendText(msg.to,Rmid)
                k15.sendText(msg.to,Smid)
                k16.sendText(msg.to,Tmid)
                k17.sendText(msg.to,Umid)
                k18.sendText(msg.to,Vmid)
                k19.sendText(msg.to,Wmid)
                k20.sendText(msg.to,Xmid)
                
#--------------------------------- GIFT -------------------------------------
            elif msg.text.lower() in ["gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#----------------------------------------------------------------------------                
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Invite:on"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
#==================================

#==================================================
            elif 'Lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'Wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("Wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'Kr restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'Ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'System':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'Kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'Cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif 'Instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("Instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'Music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Music ','')
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif 'Clean invites' in msg.text.lower():
               if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#================================================================================
            elif 'Clear invites' in msg.text.lower():
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif 'Link open' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================================================
         
            elif 'Link close' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#============================================================
          
            elif msg.text.lower() == 'Ginfo':
              if msg.from_ in admin:
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
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[display name]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nmembers:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
#===============================================================
            elif 'Group list' in msg.text.lower():
              if msg.from_ in admin:
                gs = cl.getGroupIdsJoined()
                L = "『 Groups List 』\n"
                for i in gs:
                    L += "[≫] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
 
            elif "Invite me" in msg.text:
              if msg.from_ in owner:
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			        cl.findAndAddContactsByMid(msg.from_)
                                cl.inviteIntoGroup(i,[msg.from_])
			        cl.sendText(msg.to, "successfully invited you to all groups")

            elif "Steal group pict" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
            elif "Turn off bots" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)

#===========================================================
 #=======================================================
            elif "T-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-japan " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-japan ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ja')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate japan'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-thai " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-thai ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate thai'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-id " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error: 
                    cl.sendText(msg.to,(error))          

            elif "Say " in msg.text:
              if msg.from_ in  admin:
				bctxt = msg.text.replace("Say ","")
				cl.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))

#==========================================================================	
            elif msg.text in ["Mode on","mode on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Boss")
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pname'][msg.to] = cl.getGroup(msg.to).name
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
				if msg.to in protection:
					cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ Protect ᴏɴ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏɴ")
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
#==========================================================================	
            elif msg.text in ["Mode off","mode off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")

            if "Mode off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
	
            if "Mode off" == msg.text:
				try:
					if msg.from_ in admin:
						protection.remove(msg.to)
						cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏғғ")
					else:
						cl.sendText(msg.to,"No have access Protect")
				except:
					pass

#==========================================================================	
            elif msg.text in ["Invite on","invite on"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
#======================================
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:off","auto blockqr:off"]:
              if msg.from_ in admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:on","auto blockqr:on"]:
              if msg.from_ in admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
					
            elif "Blockinvite:on" == msg.text:
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
					
            elif "Protect on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"Protect ᴀʟʀᴇᴀᴅʏ ᴏɴ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏɴ")
            elif "Protect off" == msg.text:
				try:
					if msg.from_ in admin:
						protection.remove(msg.to)
						cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏғғ")
					else:
						cl.sendText(msg.to,"Protect ᴀʟʀᴇᴀᴅʏ ᴏғғ")
				except:
					pass
 #================================================================           
            elif msg.text in ["Undang"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 random.choice(KAC).sendText(msg.to,"Kirim contact Boss")
            elif msg.text in ["Jepit"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 random.choice(KAC).sendText(msg.to,"Kirim contact Boss")
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)#=================
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite on","invite on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite off","Invite off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join on","Auto join on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","Auto join off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç���¨è‡ªåŠ¨é‚€è¯·æ���’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Leave on","Auto leave:on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Leave off","Auto leave:off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","status"]:
              if msg.from_ in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+="[•]Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["Backup"] == True: md+="[•]Backup : on\n"
                else:md+="[•]Backup : off\n"
                if wait["qr"] == True: md+="[•]AutoBlock QR : on\n"
                else:md+="[•]AutoBlock QR : off\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n"
                if wait["Protectcancel"] == True: md+="[•]Protect Cancel [On]\n"
                else: md+="[•]Protect Cancel [Off]\n"
                if wait["protectionOn"] == True: md+="[•]Protection : hight\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="[•]Protection : low\n"+ datetime.today().strftime('%H:%M:%S')
                "\n*============*\n⭐✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif "Album merit " in msg.text:
                gid = msg.text.replace("Album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç���¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "Album remove " in msg.text:
                gid = msg.text.replace("Album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "Album removeat’" in msg.text:
                gid = msg.text.replace("Album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Add on","Auto add:on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#-----------------------------------------------
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Rejectall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
#---------------------Sc invite owner ke group------
            elif "Asupka: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("Asupka: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#
#========================================
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
#===============================================
            elif msg.text in ["debug speed","Debug speed"]:
              if msg.from_ in admin:
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["zzz","Bot speed"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Measuring...")
                    start = time.time()
                    time.sleep(0.00009)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                    print "[Command]Speed palsu executed"
            elif "Speed respon" in msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Measuring...")
                    start = time.time()
                    time.sleep(0.0001)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed palsu executed"				
            elif "Sp turunin" in msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Sek lurr")
                    start = time.time()
                    time.sleep(0.02)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed palsu executed"
            elif "Sp naikin" in msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Sek lurr")
                    start = time.time()
                    time.sleep(0.1)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))   
                    print "[Command]Speed palsu executed"
            elif "Turun lagi" in msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Sek lurr")
                    start = time.time()
                    time.sleep(0.5)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))  
                    print "[Command]Speed palsu executed"
            elif "Spbot" in msg.text:
                if msg.from_ in admin:
                    time.sleep(0.5)
                    cl.sendText(msg.to, "Sek lurr")
                    start = time.time()
                    time.sleep(2.32)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))     	
                    print "[Command]Speed palsu executed"
            elif msg.text in ["Sp asli"]:
                if msg.from_ in admin:
                    start = time.time()                   
                    cl.sendText(msg.to, "Sek")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed asli executed"
    
            elif msg.text in ["Speedbot","speedbot"]:
	      if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "loading...................")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki.sendText(msg.to, "%sseconds" % (elapsed_time))
		kk.sendText(msg.to, "%sseconds" % (elapsed_time))
		cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#========================================
            elif msg.text in ["Bot1 backup run"]:
                if msg.from_ in admin:
                    wek = cl.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    cl.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot2 backup run"]:
                if msg.from_ in admin:
                    wek = ki.getContact(Amid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myesm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfs.txt',"w")
                    u.write(a)
                    u.close()
                    ki.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot3 backup run"]:
                if msg.from_ in admin:
                    wek = kk.getContact(Bmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('msgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysfdgm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('gymyps.txt',"w")
                    u.write(a)
                    u.close()
                    kk.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot4 backup run"]:
                if msg.from_ in admin:
                    wek = kc.getContact(Cmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('jhmydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myhfsm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfhs.txt',"w")
                    u.write(a)
                    u.close()
                    kc.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot5 backup run"]:
                if msg.from_ in admin:
                    wek = ks.getContact(Dmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('madydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysgjm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myrdps.txt',"w")
                    u.write(a)
                    u.close()
                    ks.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot6 backup run"]:
                if msg.from_ in admin:
                    wek = k1.getContact(Emid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydnsgv.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('jhmysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myiyps.txt',"w")
                    u.write(a)
                    u.close()
                    k1.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
#----------------------------------------------
            elif "Bot1 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        cl.updateProfilePicture(P)
                    except Exception as e:
                        cl.sendText(msg.to, "Failed!")
                        print e
            elif "Bot2 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ki.getContact(target)
                        X = contact.displayName
                        profile = ki.getProfile()
                        profile.displayName = X
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ki.getProfile()
                        lol.statusMessage = Y
                        ki.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ki.updateProfilePicture(P)
                    except Exception as e:
                        ki.sendText(msg.to, "Failed!")
                        print e
            elif "Bot3 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kk.getContact(target)
                        X = contact.displayName
                        profile = kk.getProfile()
                        profile.displayName = X
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kk.getProfile()
                        lol.statusMessage = Y
                        kk.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kk.updateProfilePicture(P)
                    except Exception as e:
                        kk.sendText(msg.to, "Failed!")
                        print e
            elif "Bot4 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kc.getContact(target)
                        X = contact.displayName
                        profile = kc.getProfile()
                        profile.displayName = X
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kc.getProfile()
                        lol.statusMessage = Y
                        kc.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kc.updateProfilePicture(P)
                    except Exception as e:
                        kc.sendText(msg.to, "Failed!")
                        print e
            elif "Bot5 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ks.getContact(target)
                        X = contact.displayName
                        profile = ks.getProfile()
                        profile.displayName = X
                        ks.updateProfile(profile)
                        ks.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ks.getProfile()
                        lol.statusMessage = Y
                        ks.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ks.updateProfilePicture(P)
                    except Exception as e:
                        ks.sendText(msg.to, "Failed!")
                        print e
            elif "Bot6 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = k1.getContact(target)
                        X = contact.displayName
                        profile = k1.getProfile()
                        profile.displayName = X
                        k1.updateProfile(profile)
                        k1.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = k1.getProfile()
                        lol.statusMessage = Y
                        k1.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        k1.updateProfilePicture(P)
                    except Exception as e:
                        k1.sendText(msg.to, "Failed!")
                        print e

#=================================================
            elif "Bot1 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = cl.getProfile()
                            profile.displayName = x
                            cl.updateProfile(profile)
                            i = open('mysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = cl.getProfile()
                            cak.statusMessage = y
                            cl.updateProfile(cak)
                            j = open('myps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            cl.updateProfilePicture(p)
                            cl.sendText(msg.to, "Succes")
                        except Exception as e:
                            cl.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot2 backup" in msg.text:
                 if msg.from_ in admin:
                        try:
                            h = open('mgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ki.getProfile()
                            profile.displayName = x
                            ki.updateProfile(profile)
                            i = open('myesm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ki.getProfile()
                            cak.statusMessage = y
                            ki.updateProfile(cak)
                            j = open('mypfs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ki.updateProfilePicture(p)
                            ki.sendText(msg.to, "Succes")
                        except Exception as e:
                            ki.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot3 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('msgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kk.getProfile()
                            profile.displayName = x
                            kk.updateProfile(profile)
                            i = open('mysfdgm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kk.getProfile()
                            cak.statusMessage = y
                            kk.updateProfile(cak)
                            j = open('gymyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kk.updateProfilePicture(p)
                            kk.sendText(msg.to, "Succes")
                        except Exception as e:
                            kk.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot4 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('jhmydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kc.getProfile()
                            profile.displayName = x
                            kc.updateProfile(profile)
                            i = open('myhfsm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kc.getProfile()
                            cak.statusMessage = y
                            kc.updateProfile(cak)
                            j = open('mypfhs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kc.updateProfilePicture(p)
                            kc.sendText(msg.to, "Succes")
                        except Exception as e:
                            kc.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot5 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('madydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ks.getProfile()
                            profile.displayName = x
                            ks.updateProfile(profile)
                            i = open('mysgjm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ks.getProfile()
                            cak.statusMessage = y
                            ks.updateProfile(cak)
                            j = open('myrdps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ks.updateProfilePicture(p)
                            ks.sendText(msg.to, "Succes")
                        except Exception as e:
                            ks.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot6 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydnsgv.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = k1.getProfile()
                            profile.displayName = x
                            k1.updateProfile(profile)
                            i = open('jhmysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kt.getProfile()
                            cak.statusMessage = y
                            k1.updateProfile(cak)
                            j = open('myiyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            k1.updateProfilePicture(p)
                            k1.sendText(msg.to, "Succes")
                        except Exception as e:
                            k1.sendText(msg.to,"Gagagl!")
                            print e
#=================================================

            elif msg.text == "Cctv":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek CCTV di proses......")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Toong":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : ✰Ќriֆ✰ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰||\n\n>Pelaku CCTV<\n%s-=CCTV=-\n•Bintitan\n•Panuan\n•Kurapan\n•Kudisan\n\nAmiin Ya Allah\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketik Toong\nDASAR PIKUN ♪")
                        
            elif msg.text == "Cctv":
              if msg.from_ in admin:
                    cl.sendText(msg.to, "Siap di intip....")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,'%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Reset"

            elif msg.text == "Intip":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰\nRead : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.strftime(now2,'%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] reset"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik Cctv untuk membuat Read point.")                        
#-----------------------------------------------
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
            elif "Cleanse" in msg.text:
	      if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok cleanse"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    gs = k11.getGroup(msg.to)
                    gs = k12.getGroup(msg.to)
                    gs = k13.getGroup(msg.to)
                    gs = k14.getGroup(msg.to)
                    gs = k15.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"you are not admin")
                    else:
                        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                               try:
                                klist=[ki,kk,kc,ks,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                               except:
                                cl.sendText(msg.to,"Group cleanse")
#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["One piece","Kr asup"]: #Panggil Semua Bot
              if msg.from_ in owner:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k11.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k12.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k13.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k14.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k15.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k16.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k17.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k18.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k19.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k20.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
                        
            elif msg.text in ["Kampret join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Luffy join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Zorro join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Sanji Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Kabur all","Ampih"]: #Bot Ninggalin Group termasuk Bot Induk
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        k6.leaveGroup(msg.to)
                        k7.leaveGroup(msg.to)
                        k8.leaveGroup(msg.to)
                        k9.leaveGroup(msg.to)
                        k10.leaveGroup(msg.to)
                        k11.leaveGroup(msg.to)
                        k12.leaveGroup(msg.to)
                        k13.leaveGroup(msg.to)
                        k14.leaveGroup(msg.to)
                        k15.leaveGroup(msg.to)
                        k16.leaveGroup(msg.to)
                        k17.leaveGroup(msg.to)
                        k18.leaveGroup(msg.to)
                        k19.leaveGroup(msg.to)
                        k20.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Kabur"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        k6.leaveGroup(msg.to)
                        k7.leaveGroup(msg.to)
                        k8.leaveGroup(msg.to)
                        k9.leaveGroup(msg.to)
                        k10.leaveGroup(msg.to)
                        k11.leaveGroup(msg.to)
                        k12.leaveGroup(msg.to)
                        k13.leaveGroup(msg.to)
                        k14.leaveGroup(msg.to)
                        k15.leaveGroup(msg.to)
                        k16.leaveGroup(msg.to)
                        k17.leaveGroup(msg.to)
                        k18.leaveGroup(msg.to)
                        k19.leaveGroup(msg.to)
                        k20.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["Bye zorro"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye sanji"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ussop"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe3"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Emak"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["Abah"]:
            	 if msg.from_ in admin:              
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    mention2(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                 if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                 if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                 if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention2(msg.to, nm5)
                 if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                 cnt = Message()
                 cnt.text = "Done : " + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)                      
                      
            elif msg.text in ["Crot"]:
            	 if msg.from_ in admin:              
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    mention2(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                 if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                 if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                 if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention2(msg.to, nm5)
                 if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                 cnt = Message()
                 cnt.text = "Done : " + str(jml) +  " Members\nCrot aw.. Muncrat...!!!"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)                  
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Ready op" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ready op","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    gs = k11.getGroup(msg.to)
                    gs = k12.getGroup(msg.to)
                    gs = k13.getGroup(msg.to)
                    gs = k14.getGroup(msg.to)
                    gs = k15.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Eh Ini Room apaan?")
                    random.choice(KAC).sendText(msg.to,"Ratain aja lah\nRoom Ga Berguna..")
                    random.choice(KAC).sendText(msg.to,"Jangan Baper yah Tollll;")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in Bots:
                            pass
                          if target in admin:
                            pass
                          else:
                            try:
                              klist=[cl,ki,kk,kc,ks,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                              print (msg.to,[g.mid])
                            except:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              random.choice(KAC).sendText(msg.to,"Koq Ga Ditangkis Wooyyy?\Lemah Banget Nih Room")
                              
            elif "Greet" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Greet","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    gs = k11.getGroup(msg.to)
                    gs = k12.getGroup(msg.to)
                    gs = k13.getGroup(msg.to)
                    gs = k14.getGroup(msg.to)
                    gs = k15.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    kk.sendText(msg.to,"makasih semuanya..")
                    kc.sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
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
                      cl.kickoutFromGroup(msg.to,[target])
                      print (msg.to,[g.mid])
                    except:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                      
            elif "Tajong " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Tajong ","")
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
                satpam1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
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
                        satpam1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        satpam1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
                        
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k10.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k13.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k15.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#
#----------------------------[Spam To Contact]----------------------------#WORK 
            elif "Spamcontact @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam") 
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       k9.sendText(g.mid,"Ini Adalah Spam")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k7.sendText(g.mid,"Jangan Ngintip")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k15.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       k20.sendText(g.mid,"Masuk Room Woy...!!!")
                       cl.sendText(msg.to, "Target Spam, Done...!!!")
                       kk.sendText(msg.to, "Target Spam, Done...!!!")
                       k1.sendText(msg.to, "Target Spam, Done...!!!")
                       k20.sendText(msg.to, "Target Spam, Done...!!!")
                       k9.sendText(msg.to, "Target Spam, Done...!!!")
                       k7.sendText(msg.to, "Target Spam, Done...!!!")
                       k15.sendText(msg.to, "Target Spam, Done...!!!")
                       print " Spammed !"
#----------------------------[Spam To Contact]----------------------------#WORK 
       #--------------------Start-----------------------#       
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)		
                k15.sendText(msg.to,jawaban)		                
                k15.sendText(msg.to,jawaban)		                
            elif "Berapa besar cinta " in msg.text:
                tanya = msg.text.replace("Berapa besar cinta ","")
                jawab = ("0%","25%","50%","75%","100%")
                jawaban = random.choice(jawab)
                kk.sendText(msg.to,jawaban)                
                kk.sendText(msg.to,jawaban)		                
                kk.sendText(msg.to,jawaban)		                
            elif "Siapakah cewek " in msg.text:
                tanya = msg.text.replace("Siapakah cewek ","")
                jawab = ("Maryati􀜁�","Ida􀜁�","Uke􀜁�","Alyn􀜁�","Ikka􀜁�","Yunikey􀜁�","Qwenie􀜁�","Gendis􀜁�","Aryani􀜁�","Nindy􀜁�","Wina􀜁�","Dewi􀜁�","Ifah􀜁�")
                jawaban = random.choice(jawab)
                k7.sendText(msg.to,jawaban)
                k7.sendText(msg.to,jawaban)
                k7.sendText(msg.to,jawaban)
            elif "Siapakah cowok " in msg.text:
                tanya = msg.text.replace("Siapakah cowok ","")
                jawab = ("Arjun􀜁�","Ahmad khan􀜁�","Hajir􀜁�","Dd􀜁�","Indra􀜁�","Jeong􀜁�","Yogi􀜁�","Ary􀜁�","Ucil􀜁�")
                jawaban = random.choice(jawab)
                k5.sendText(msg.to,jawaban)
                k5.sendText(msg.to,jawaban)
                k5.sendText(msg.to,jawaban)
            elif "Adakah " in msg.text:
                tanya = msg.text.replace("Adakah ","")
                jawab = ("Tidak tahu.","Ada.","Tidak ada.","Mungkin ada")
                jawaban = random.choice(jawab)
                k3.sendText(msg.to,jawaban)
                k3.sendText(msg.to,jawaban)	                
                k3.sendText(msg.to,jawaban)	                             
            elif "Cakepkah " in msg.text:
                tanya = msg.text.replace("Cakepkah ","")
                jawab = ("Jelek.","Cakep.","Lumayan.","Kaya jembut.")
                jawaban = random.choice(jawab)
                k11.sendText(msg.to,jawaban)
                k11.sendText(msg.to,jawaban)	         
                k11.sendText(msg.to,jawaban)	                       
       #-------------------Finish-----------------------#
        #-------------Fungsi Broadcast Start------------#
            elif "GBc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                bctxt = msg.text.replace("GBc ","")
                a = cl.getGroupIdsJoined()
                a = ki.getGroupIdsJoined()
                a = kk.getGroupIdsJoined()
                a = kc.getGroupIdsJoined()
                a = ks.getGroupIdsJoined()
                a = k1.getGroupIdsJoined()
                a = k2.getGroupIdsJoined()
                a = k3.getGroupIdsJoined()
                a = k4.getGroupIdsJoined()
                a = k5.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  ki.sendText(taf, (bctxt))
                  kk.sendText(taf, (bctxt))
                  kc.sendText(taf, (bctxt))
                  ks.sendText(taf, (bctxt))
                  k1.sendText(taf, (bctxt))
                  k2.sendText(taf, (bctxt))
                  k3.sendText(taf, (bctxt))
                  k4.sendText(taf, (bctxt))
                  k5.sendText(taf, (bctxt))
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				kc.sendText(msg.to,(bctxt))
				k1.sendText(msg.to,(bctxt))
				k2.sendText(msg.to,(bctxt))
				k12.sendText(msg.to,(bctxt))
				k13.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#                  

            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in admin:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                  cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                  h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                  cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot kadieu"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = k1.getGroupIdsJoined()
                gid = k2.getGroupIdsJoined()
                gid = k3.getGroupIdsJoined()
                gid = k4.getGroupIdsJoined()
                gid = k5.getGroupIdsJoined()
                gid = k6.getGroupIdsJoined()
                gid = k7.getGroupIdsJoined()
                gid = k8.getGroupIdsJoined()
                gid = k9.getGroupIdsJoined()
                gid = k10.getGroupIdsJoined()
                gid = k11.getGroupIdsJoined()
                gid = k12.getGroupIdsJoined()
                gid = k13.getGroupIdsJoined()
                gid = k14.getGroupIdsJoined()
                gid = k15.getGroupIdsJoined()
                gid = k16.getGroupIdsJoined()
                gid = k17.getGroupIdsJoined()
                gid = k18.getGroupIdsJoined()
                gid = k19.getGroupIdsJoined()
                gid = k20.getGroupIdsJoined()
                for i in gid:
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  k1.leaveGroup(i)
                  k2.leaveGroup(i)
                  k3.leaveGroup(i)
                  k4.leaveGroup(i)
                  k5.leaveGroup(i)
                  k6.leaveGroup(i)
                  k7.leaveGroup(i)
                  k8.leaveGroup(i)
                  k9.leaveGroup(i)
                  k10.leaveGroup(i)
                  k11.leaveGroup(i)
                  k12.leaveGroup(i)
                  k13.leaveGroup(i)
                  k14.leaveGroup(i)
                  k15.leaveGroup(i)
                  k16.leaveGroup(i)
                  k17.leaveGroup(i)
                  k18.leaveGroup(i)
                  k19.leaveGroup(i)
                  k20.leaveGroup(i)
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sayonara, Bye bye all...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
  #------------------------End---------------------
#-------------------------------------------------
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Broadcast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Broadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt +"\n\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
  #-----------------End-----------
            elif msg.text in ["hai","Hai"]:
                ki.sendText(msg.to,"Hai Every Body 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hai Every Body 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hai Every Body 􀜁􀅔Har Har􏿿")

            elif msg.text in ["nah","Nah"]:
                ki.sendText(msg.to,"Kan")
                kk.sendText(msg.to,"Kan")
                kc.sendText(msg.to,"Kan")
#-----------------------------------------------)
            elif msg.text in ["Wc","wc","kam"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Respon"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"★")
                ki.sendText(msg.to,"★★")
                cl.sendText(msg.to,"★★★")
                kc.sendText(msg.to,"★★★★")
                ks.sendText(msg.to,"★★★★★")
                k1.sendText(msg.to,"★★★★★★")
                k2.sendText(msg.to,"★★★★★★★")
                k3.sendText(msg.to,"★★★★★★★★")
                k4.sendText(msg.to,"★★★★★★★★★")
                k5.sendText(msg.to,"★★★★★★★★★★")
                k6.sendText(msg.to,"★★★★★★★★★★★")
                k7.sendText(msg.to,"★★★★★★★★★★★★")
                k8.sendText(msg.to,"★★★★★★★★★★★★★")
                k9.sendText(msg.to,"★★★★★★★★★★★★★★")
                k10.sendText(msg.to,"★★★★★★★★★★★★★★★")
                k11.sendText(msg.to,"★★★★★★★★★★★★★★★★")
                k12.sendText(msg.to,"★★★★★★★★★★★★★★★★★")
                k13.sendText(msg.to,"★★★★★★★★★★★★★★★★★★")
                k14.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★")
                k15.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★")
                k16.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★★")
                k17.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★★★")
                k18.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★★★★")
                k19.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★★★★★")
                k20.sendText(msg.to,"★★★★★★★★★★★★★★★★★★★★★★★★★")
                random.choice(KAC).sendText(msg.to,"Semua Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
      #-------------Fungsi Respon Finish---------------------#
                            
#==========================================
            elif "Youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif "youtube " in msg.text.lower():
                query = msg.text.split(" ")
                try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
              if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
#==========================================
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
           
            	    ki.sendText(msg.to,text)
                    kc.sendText(msg.to,text)
                    kk.sendText(msg.to,text)
                    ks.sendText(msg.to,text)
                    k1.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
			        kc.sendMessage(msg)
            			ks.sendMessage(msg)
			        k1.sendMessage(msg)
            			
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
                                k1.sendMessage(msg)
                                kc.sendMessage(msg)
                                ks.sendMessage(msg)         

            
#            elif msg.text in ["Target list"]:
#              if msg.from_ in admin:
#                        if mimic["target"] == {}:
#                            cl.sendText(msg.to,"nothing")
#                        else:
#                            mc = "Target mimic user\n"
#                            for mi_d in mimic["target"]:
#                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
#                            cl.sendText(msg.to,mc)

         
#            elif "Mimic:" in msg.text:
#	          if msg.from_ in admin:
#            		  cmd = msg.text.replace("Mimic:","")
#            		  if cmd == "on":
#            			  if mimic["status"] == False:
#            				  mimic["status"] = True
#            				  cl.sendText(msg.to,"turning on mimic")
#            				
#            			  else:
#            				  cl.sendText(msg.to,"mimic have been enable")
            				
#            		  elif cmd == "off":
#            			  if mimic["status"] == True:
#            				  mimic["status"] = False
#            				  cl.sendText(msg.to,"turning off mimic")
#            				
#            			  else:
#            				  cl.sendText(msg.to,"Mimic have been desable")
            				
#            		  elif "Mimic target " in cmd:
#                            if msg.from_ in admin:
#                                      target0 = msg.text.replace("Mimic target ","")
#            			      target1 = target0.lstrip()
#            			      target2 = target1.replace("@","")
#            			      target3 = target2.rstrip()
#            			      _name = target3
#            			      gInfo = cl.getGroup(msg.to)
#            			      targets = []
#            			      for a in gInfo.members:
#                               	              if _name == a.displayName:
#            				              targets.append(a.mid)
#            			      if targets == []:
#            				     cl.sendText(msg.to,"No targets")
#            				
#            			      else:
#                			      for target in targets:
#            					      try:
#            						      mimic["target"][target] = True
#            						      cl.sendText(msg.to,"Success added target")
#            						
#            						      #cl.sendMessageWithMention(msg.to,target)
#            						      break
#            					      except:
#            						      cl.sendText(msg.to,"Failed")
#            						
#            						      break
#            		  elif "Untarget " in cmd:
#                            if msg.from_ in admin:
#            			      target0 = msg.text.replace("Untarget ","")
#            			      target1 = target0.lstrip()
#            			      target2 = target1.replace("@","")
#            			      target3 = target2.rstrip()
#            			      _name = target3
#            			      gInfo = cl.getGroup(msg.to)
#            			      gInfo = ki.getGroup(msg.to)
#            			      targets = []
#            			      for a in gInfo.members:
#            				      if _name == a.displayName:
#            					      targets.append(a.mid)
#            			      if targets == []:
#            				      cl.sendText(msg.to,"No targets")
            				
#            			      else:
#            				      for target in targets:
#            					      try:
#            						      del mimic["target"][target]
#            						      cl.sendText(msg.to,"Success deleted target")
            					
            						      #cl.sendMessageWithMention(msg.to,target)
#            						      break
#            					      except:
#            						      cl.sendText(msg.to,"Failed!")            

#==========================================

            elif msg.text in ["Mimic on","mimic on","Mimic:on"]:
                if msg.from_ in admin:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic off","Mimic:off"]:
                if msg.from_ in admin:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list","Targetlist"]:
                if msg.from_ in admin:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                if msg.from_ in admin:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                if msg.from_ in admin:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                if msg.from_ in admin:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#==========================================
#=======================================
            elif msg.text in ["Backup","backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateProfile(backup)
                    kk.updateProfile(backup)
                    kc.updateProfile(backup)
                    ks.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                    ki.sendText(msg.to, "Refreshed.")
                    kk.sendText(msg.to, "Refreshed.")
                    kc.sendText(msg.to, "Refreshed.")
                    ks.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    ki.sendText(msg.to, str(e))
                    kk.sendText(msg.to, str(e))
                    kc.sendText(msg.to, str(e))
                    ks.sendText(msg.to, str(e))
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    ki.CloneContactProfile(target)
                                    kk.CloneContactProfile(target)
                                    kc.CloneContactProfile(target)
                                    ks.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif msg.text in ["Kembali awal"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#--------------------------------------------------------
            elif "rejectall" in msg.text:
                    X = cl.getGroupIdsInvited()
                    for i in X:           	    
			cl.rejectGroupInvitation(i)
#--------------------------------------------------------
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#
            elif ("Vkick" in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")
							
       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Sabar Boss...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sDetik" % (elapsed_time))
                kk.sendText(msg.to, "%sDetik" % (elapsed_time))
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
                kc.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u31ef22df7f538df1d74dc7f756ef1a32'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"Itu Creator Kami Yang Manis Kalem 😜\nSmule : @FS3i_Kris_S1H\nNama : Kris\nZodiak : Cancer")  
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Koplak Lu','Muka Lu Kaya Jembut','Ada Orang kah disini?','Ada Janda Yang Bisa Di Ajak Mojok Gak, Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    random.choice(KAC).sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
	      if msg.from_ in owner:
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		kc.removeAllMessages(op.param2)
		ks.removeAllMessages(op.param2)
		k1.removeAllMessages(op.param2)
		k2.removeAllMessages(op.param2)
		k3.removeAllMessages(op.param2)
		k4.removeAllMessages(op.param2)
		k5.removeAllMessages(op.param2)
		k6.removeAllMessages(op.param2)
		k7.removeAllMessages(op.param2)
		k8.removeAllMessages(op.param2)
		k9.removeAllMessages(op.param2)
		k10.removeAllMessages(op.param2)
		k11.removeAllMessages(op.param2)
		k12.removeAllMessages(op.param2)
		k13.removeAllMessages(op.param2)
		k14.removeAllMessages(op.param2)
		k15.removeAllMessages(op.param2)
		k16.removeAllMessages(op.param2)
		k17.removeAllMessages(op.param2)
		k18.removeAllMessages(op.param2)
		k19.removeAllMessages(op.param2)
		k20.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#---------------------------
#KICK_BY_TAG
        elif "Boom " in msg.text:
          if msg.from_ in Creator:
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', msg.text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                print mentionees
                for mention in mentionees:
                    ki.kickoutFromGroup(msg.to,[mention['M']])


#===========================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#        if op.param1 in autocancel:
#			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
#			if op.param2 in OWN:
#				pass
#			else:
#				Inviter = op.param3.replace("",',')
#				InviterX = Inviter.split(",")
#				contact = cl.getContact(op.param2)
#				cl.cancelGroupInvitation(op.param1,InviterX)
#				ki.cancelGroupInvitation(op.param1,InviterX)
#				kk.cancelGroupInvitation(op.param1,InviterX)
#				ks.cancelGroupInvitation(op.param1,InviterX)
#				kc.cancelGroupInvitation(op.param1,InviterX)
#				ka.cancelGroupInvitation(op.param1,InviterX)
#				cl.kickoutFromGroup(op.param1,[op.param2])
#				ki.kickoutFromGroup(op.param1,[op.param2])
#				kk.kickoutFromGroup(op.param1,[op.param2])
#				ks.kickoutFromGroup(op.param1,[op.param2])
#				kc.kickoutFromGroup(op.param1,[op.param2])
#				ka.kickoutFromGroup(op.param1,[op.param2])
#				wait["blacklist"][op.param2] = True
#				f=codecs.open('st2__b.json','w','utf-8')
#				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = ""
			if op.param2 in Bots and admin:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				k1.kickoutFromGroup(op.param1,[op.param2])
				k2.kickoutFromGroup(op.param1,[op.param2])
				k3.kickoutFromGroup(op.param1,[op.param2])
				k4.kickoutFromGroup(op.param1,[op.param2])
				k5.kickoutFromGroup(op.param1,[op.param2])
				k6.kickoutFromGroup(op.param1,[op.param2])
				k7.kickoutFromGroup(op.param1,[op.param2])
				k8.kickoutFromGroup(op.param1,[op.param2])
				k9.kickoutFromGroup(op.param1,[op.param2])
				k10.kickoutFromGroup(op.param1,[op.param2])
				k11.kickoutFromGroup(op.param1,[op.param2])
				k12.kickoutFromGroup(op.param1,[op.param2])
				k13.kickoutFromGroup(op.param1,[op.param2])
				k14.kickoutFromGroup(op.param1,[op.param2])
				k15.kickoutFromGroup(op.param1,[op.param2])
				k16.kickoutFromGroup(op.param1,[op.param2])
				k17.kickoutFromGroup(op.param1,[op.param2])
				k18.kickoutFromGroup(op.param1,[op.param2])
				k19.kickoutFromGroup(op.param1,[op.param2])
				k20.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
#        if op.type == 26:
#            if "@"+cl.getProfile().displayName in msg.text:
#                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
#                jawab = ("Jgn Tag Gw woyy!!\nlagi ngocok dulu...!!!","Berisik jgn tag Gw Koplak","Gw Sibuk, Gausah di Tag!!!","Ngapain tag neh,, kangen yah...!!!")
#                jawaban = random.choice(jawab)
#                cl.sendText(msg.to,jawaban)
                
        elif "@"+cl.getProfile().displayName in msg.text:
            try:
                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                jawab = ("Jgn Tag Si "+cl.getProfile().displayName+"Ta cipok luh..!!","Berisik jgn tag si "+cl.getProfile().displayName+" dia lagi asyik ngocok...!!!")
                jawaban = random.choice(jawab)
                random.choice(KAC).sendText(msg.to,jawaban)
                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
            except:
                pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
#        if op.type == 17:
#          if op.param2 in Bots:
#            return
#          ginfo = cl.getGroup(op.param1)
#          random.choice(KAC).sendText(op.param1, "Welcome\nSelamat Datang Di  " + str(ginfo.name))
#          random.choice(KAC).sendText(op.param1, "Founder =>>> " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
#          random.choice(KAC).sendText(op.param1, "😊 Semoga Betah Kk 😘\nNo Baper,No nakal,No Ngeyel ya,No Bulshit")
#          print "MEMBER HAS JOIN THE GROUP"
#        if op.type == 15:
#          if op.param2 in Bots:
#             return
#          random.choice(KAC).sendText(op.param1, "Baper Tuh Orang :v\nBelum di Anu Kayanya 😊")
#          print "MEMBER HAS LEFT THE GROUP"
#--------------------------------------------------------
#        if 'MENTION' in mid or Amid or Bmid or Cmid or Dmid or Emid or Fmid or Gmid or Hmid or Imid:
#          cl.sendtext(msg.to,'[Auto Respon]\nngapain tag, pc langsung aja...!!!')
#          pass
#--------------------------------------------------------
#Restart_Program
        elif msg.text in ["Bot restart"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Bot has been restarted")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
#--------------------------------------------------------




        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k11.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k12.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k13.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k14.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k15.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k16.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k17.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k18.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k19.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k20.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Boss"
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5)
            time.sleep(600)
        except:
            pass
         
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
