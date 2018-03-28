# -*- coding: utf-8 -*-    
      
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='ErHvZ0wnlbyv9ucqpAj8.sGpL7MhXv/v78cRSmT7doa.Ha8SF3Fdlw8OLigrYH4zLliNF6gburHHH30EbIxziG8=') # BOT PUBLIK
cl.loginResult()

print "❂➣ [BOT PUBLIK BERHASIL LOGIN}"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'

helpMessage ="""
============================
       🤖 BOT  KEY 🤖
============================
01. Apakah [text] = Kr_ajaib
02. Kapan [text] = Tanya bot
03. Dosa @ [by tag]
04. Pahala @ [by tag]
05. Gcreator
06. Bot spam on [jml] [text]
07. Search image: [text]
08. Instagram: [username]
09. Wikipedia: [search words]
10. Playstore: [search words]
11. Anime: [search words]
12. Lirik: [artis] [judul]
13. Music: [artis] [judul]
14. youtube: [text]
15. youtube search: [text]
16. Mister/Mr (cek bot)
17. Dubbing [text]
18. Name: [tag member]
19. Bio: [tag member]
20. Info: [tag member]
21. Getinfo: [tag member]
22. Getprofile [tag member]
23. Getcontact: [tag member]
24. Getpp [tag member]
25. Gethome [tag member]
26. Getgroup (cover group)
27. Set sider
28. Cek sider
29. setview
30. viewseen
31. Tagall/Mentionall
32. Gift
33. Gift1
34. Gift2
35. Gift3
36. Line clone
37. Key translate
38. Up chat / Up
39. love [Siti love adi]
40. sider on/off (auto)
==============================
Mʏ ᴄʀᴇᴀᴛᴏʀ:
line.me//ti/p/~tak.dapat.tidur
==============================
"""

protectMessage ="""Empty"""
#╔═════════════
#║    ADMIN ONLY
#╠═════════════
#║╔════════════
#║╠❂͜͡⚡➣qr on/oғғ
#║╠❂͜͡⚡➣gυeѕт on/oғғ
#║╠❂͜͡⚡➣мeмвer on/oғғ
#║╠❂͜͡⚡➣groυp on/oғғ
#║╠❂͜͡⚡➣ĸιcĸ on/oғғ
#║╠❂͜͡⚡➣cancel on/oғғ
#║╚════════════
#╚═════════════


socmedMessage ="""
╔═════════════
║    SOSMED KEY
║╔════════════
║╠❂͜͡🌟➣Wikipedia: [тeхт]
║╠❂͜͡🌟➣Instagram: [username]
║╠❂͜͡🌟➣Image: [тeхт]
║╠❂͜͡🌟➣Lirik: [тeхт]
║╠❂͜͡🌟➣Lineid: [тeхт]
║╠❂͜͡🌟➣Music: [artis] [judul]
║╠❂͜͡🌟➣тιмe [тιмe]
║╠❂͜͡🌟➣ѕay [тeхт]
║╚════════════
╚═════════════
"""

translateMessage ="""
╔═════════════
║    TRANSLATE KEY
║╔════════════
║╠☔тr-ιd = ιndoneѕιa
║╠☔тr-мy = мyanмar
║╠☔тr-en = englιѕн
║╠☔тr-тн = тнaιland
║╠☔тr-ja = japaneѕe
║╠☔тr-мѕ = мalayѕιa
║╠☔тr-ιт = ιтalιan
║╠☔тr-тr = тυrĸιѕн
║╠☔тr-aғ = aғrιĸaanѕ
║╠☔тr-ѕq = alвanιan
║╠☔тr-aм = aмнarιc
║╠☔тr-ar = araвιc
║╠☔тr-нy = arмenιan
║╚════════════
╚═════════════
"""

botMessage ="""
╔═════════════
║    BOT KEY
║╔════════════
║╠❂͜͡⚡➣Set sider > Cek sider
║╠❂͜͡⚡➣Tes / Sepi
║╠❂͜͡⚡➣Reѕpon
║╠❂͜͡⚡➣Speed / Sp
║╠❂͜͡⚡➣Grup list
║╠❂͜͡⚡➣Tagall / Mentionall
║╠❂͜͡⚡➣Me
║╚════════════
╚═════════════
"""

settingMessage ="""Empty"""
#╔═════════════
#║    SETTING KEY
#║╔════════════
#║╠❂͜͡🌟➣ѕeт
#║╠❂͜͡🌟➣тag on/oғғ
#║╠❂͜͡🌟➣aυтolιĸe on/oғғ
#║╠❂͜͡🌟➣add on/oғғ
#║╠❂͜͡🌟➣joιn on/oғғ
#║╠❂͜͡🌟➣ѕнare on/oғғ
#║╠❂͜͡🌟➣coммenт on/oғғ
#║╚════════════
#╚═════════════
#"""

giftMessage ="""
╔═════════════
║    GIFT KEY
║╔════════════
║╠❂͜͡🌟➣gιғт
║╠❂͜͡🌟➣gιғт 1
║╠❂͜͡🌟➣gιғт 2
║╠❂͜͡🌟➣gιғт 3
║╚════════════
╚═════════════
"""

stealMessage ="""
╔═════════════
║    STEAL KEY
║╔════════════
║╠❂͜͡🌟➣geтnaмe @
║╠❂͜͡🌟➣geтвιo @
║╠❂͜͡🌟➣geтιnғo @
║╠❂͜͡🌟➣geтpp @
║╠❂͜͡🌟➣geтмιd @
║╠❂͜͡🌟➣geтgroυp
║╠❂͜͡🌟➣papιмage
║╠❂͜͡🌟➣papvιdeo
║╚════════════
╚═════════════
"""
KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid]
owner=["u3cfa63811888b3a880bc4f348a95b23b",mid]
admin=["u3cfa63811888b3a880bc4f348a95b23b",mid]
baby=[""]#chery/barby/ranita
creator=["u3cfa63811888b3a880bc4f348a95b23b"]
owner=["u3cfa63811888b3a880bc4f348a95b23b"]
wait = {
    'contact':False,
    'autoJoin':True,
    'leaveRoom':False,
    'autoAdd':False,
    'timeline':True,
    "Timeline":True,
    "message":"""Tʜᴀɴᴋꜱ ғᴏʀ ᴀᴅᴅ ᴍᴇ (^_^)\nIɴᴠɪᴛᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ヘ(^_^)ヘ\n\nCᴏɴᴛᴀᴄᴛ Mʏ Cʀᴇᴀᴛᴏʀ:\nline.me/ti/p/~tak.dapat.tidur""",
    "lang":"JP",
    "comment":"Cᴏɴᴛᴀᴄᴛ Mʏ Cʀᴇᴀᴛᴏʀ:\nline.me/ti/p/~tak.dapat.tidur",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "auto":True,
    "tag":True,
    "pap":True,
    "steal":{},
    "gift":{},
    "likeOn":True,
    "alwayRead":True,
    "Mimic":False,
    "mimic":False,
    "winvite":True,
    "winvite2":False,
    "Wc":True,
    "Lv":True,
    "atjointicket":True,
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
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

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'http://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def sendFileWithURL(self, url, name = ''):
        """Send a File with given File url
        :param url: File url to send
        """
        from urlparse import urlparse
        from os.path import basename
        import urllib2

        if name == '':
          name = basename(urlparse(url).path)
        file = urllib2.urlopen(url)
        output = open('pythonLine.data','wb')
        output.write(file.read())
        output.close()
        try:
            self.sendFile('pythonLine.data', name)
        except Exception as e:
            raise e

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'https://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

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

     return image

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
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
      r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
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

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
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

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "✔ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
		
def removeAllMessages(self, lastMessageId):
      return self._client.removeAllMessages(0, lastMessageId)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if wait["auto"] == True:
                cl.acceptGroupInvitation(op.param1)
                cl.sendText(op.param1, "Jᴀɴɢᴀɴ ɪɴᴠɪᴛᴇ ꜱᴇᴍʙᴀʀᴀɴɢ ᴏʀᴀɴɢ! Sᴇʟᴀɪɴ ᴅᴀᴘᴀᴛ ɪᴊɪɴ ᴅᴀʀɪ ᴏᴡɴᴇʀ ᴀᴛᴀᴜ ᴀᴅᴍɪɴ.\n\nSɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ [Mɪꜱᴛᴇʀ Hᴇʟᴘ] ᴜɴᴛᴜᴋ ʙᴀɴᴛᴜᴀɴ, ᴅᴀɴ ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ. Tᴇʀɪᴍᴀ Kᴀꜱɪʜ")
 #               cl.sendText(op.param1, "Tᴇʀɪᴍᴀ ᴋᴀꜱɪʜ ᴛᴇʟᴀʜ ᴜɴᴅᴀɴɢ ꜱᴀʏᴀ.\nPᴇʀᴋᴇɴᴀʟᴋᴀɴ ɴᴀᴍᴀ ꜱᴀʏᴀ ᴍɪꜱᴛᴇʀ Rɪᴜꜱ 👱\n\nSɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ [Mɪꜱᴛᴇʀ Hᴇʟᴘ] ᴜɴᴛᴜᴋ ʙᴀɴᴛᴜᴀɴ, ᴅᴀɴ ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ. Tᴇʀɪᴍᴀ Kᴀꜱɪʜ")


        if op.type == 5:
           if wait["autoAdd"] == True:
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass

#---------------------------------------------------------------------
        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = ("Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung biar anu hihi..!!\n\n[autoRespon]\nby 🍁հմՏɑíղ✍️\n👉line.me//t/p/~tak.dapat.tidur👈","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja dari pada ngetag mulu.. wkwk...!!!\n\n[autoRespon]\nby 🍁հմՏɑíղ✍️\n👉line.me//t/p/~tak.dapat.tidur👈")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)

        #------Open QR Kick finish-----#
                if wait["alwayRead"] == True:
                    if msg.toType == 0:
                        cl.sendChatChecked(msg.from_,msg.id)
                    else:
                        cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")

        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                cl.sendMessage(c)
                cl.sendImageWithURL(op.param1,image)
                cl.sendText(op.param1,"Hɪɪ... " + cl.getContact(op.param2).displayName + " \nWᴇʟᴄᴏᴍᴇ Tᴏ " + str(ginfo.name) + "\n\n" + "Gʀᴏᴜᴘ Cʀᴇᴀᴛᴏʀ :\n👉  " + ginfo.creator.displayName + "\n\nBᴜᴅᴀʏᴀᴋᴀɴ ᴄᴇᴋ ɴᴏᴛᴇ\nDᴀɴ ꜱᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴅɪꜱɪɴɪ ^_^\nSɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ [Mɪꜱᴛᴇʀ ʜᴇʟᴘ],\nᴅᴀɴ ɢᴜɴᴀᴋᴀɴ ᴅɢɴ ʙɪᴊᴀᴋ. Tᴇʀɪᴍᴀ Kᴀꜱɪʜ")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                cl.sendMessage(c)
                cl.sendImageWithURL(op.param1,image)
                cl.sendText(op.param1,"Gᴏᴏᴅ Bʏᴇ " + cl.getContact(op.param2).displayName +  "\nSᴇᴇ Yᴏᴜ Nᴇxᴛ Tɪᴍᴇ . . . (p′︵‵。) 🤗")
                print "MEMBER HAS LEFT THE GROUP"
#-----------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin or owner:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
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
#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in creator:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner or mid:
                  cl.acceptGroupInvitation(op.param1)
                  cl.sendText(op.param1, "Tᴇʀɪᴍᴀ ᴋᴀꜱɪʜ ᴛᴇʟᴀʜ ᴜɴᴅᴀɴɢ ꜱᴀʏᴀ.\nPᴇʀᴋᴇɴᴀʟᴋᴀɴ ɴᴀᴍᴀ ꜱᴀʏᴀ ᴍɪꜱᴛᴇʀ Rɪᴜꜱ 👱\n\nSɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ [Mɪꜱᴛᴇʀ Hᴇʟᴘ] ᴜɴᴛᴜᴋ ʙᴀɴᴛᴜᴀɴ, ᴅᴀɴ ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ. Tᴇʀɪᴍᴀ Kᴀꜱɪʜ")
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
#-----------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
            if op.param3 in admin:
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,admin)
                 cl.inviteIntoGroup(op.param1,[op.param3])
            else:
                pass
#================================================================
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
#-----------------------------------------
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
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")

               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        cl.sendText(msg.to,"already")
                        cl.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        cl.sendText(msg.to,"aded")
                        cl.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")

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
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Mister help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key translate"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,translateMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key7"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,botMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key2"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,socmedMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key4"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,protectMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key5"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,settingMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key6"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,stealMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key3"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,giftMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif ("Gn: " in msg.text):
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn: ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
            elif "Botinvite " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Botinvite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
            elif msg.text in ["Me"]:
                 msg.contentType = 13
                 msg.contentMetadata = {'mid': mid}
                 cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Cancel","cancel"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						G = cl.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
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
#--------------------------------------------------
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
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
#--------------------------------------------------
            elif msg.text == "Ginfo":
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
                            u = "Close"
                        else:
                            u = "Open"
                        cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Profile Status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nMembers: " + str(len(ginfo.members)) + " members\nPending: " + sinvitee + " people\nURL: " + u + " it is inside")
                    else:
                        cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Profile Status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
														
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        print "Spamtag Berhasil."
#--------------------------------------------------
            elif msg.text.lower() in ["wkwk","wkwkwk","ckck","ckckck"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100' }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100' }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["galon","galo","galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100' }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["you","kamu","km","u","qm"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "7",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["hadeuh","hadeh","hadech"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "6",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["please"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "4",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["haaa","hah","kaget","terkejut"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "3",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["lol","haha","hahaha","ngakak","lucu"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "110",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["hmmm","hmm"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "101",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text.lower() in ["come","ayo","kuy"]:
                msg.contentType = 7
                msg.contentMetadata={"STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["tidur","turu","bobo","bubu","sleep","nite"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)
#---------------------------------------------------
            elif "Id" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,msg.to)
#--------------------------------------------------
            elif msg.text in ["TL "]:
				if msg.from_ in admin or owner:
					tl_text = msg.text.replace("TL ","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#--------------------------------------------------
            elif msg.text in ["Undang"]:
              if msg.from_ in admin or owner:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#--------------------------------------------------
            elif msg.text in ["Mc "]:
				if msg.from_ in admin or owner:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥Ââ 1�71¤7šÃ¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Join on","Auto join:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥ÂÆ’Ã¥Å�1�7�1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
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
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥Ââ 1�71¤7šÃ¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Join off","Auto join:off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥ÂÆ’Ã¥Å�1�7�1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
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
#--------------------------------------------------
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin or owner:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ�1�7�1�71¤7 Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»ÂÃ£â�1�7�¬â€šÃ¨Â¦ÂÃ¦â 1�71¤7”Â¶Ã¥Â¼â�1�7�¬Ã¨Â¯Â·Ã¦Å�1�7�â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â 1�71¤7¢Â°Ã¥Ââ 1�71¤7˜Ã©â‚¬Â1�7")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â�1�7�1�71¤7žÃ¥Â°ÂÃ§Â»â 1�71¤7žÃ§â 1�71¤7Â¨Ã¨â 1�71¤7¡ÂªÃ¥Å Â¨Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»Â�1�7�1�71¤7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
#--------------------------------------------------
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡Â 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡ÂºÃ¯Â¼Å¡Ã©â 1�71¤7“â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡Â 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡ÂºÃ¯Â¼Å¡Ã©â 1�71¤7”Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
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
#--------------------------------------------------
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å�1�7�â�1�7�1�71¤7 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Share on","Share on"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å�1�7�â�1�7�1�71¤7 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Share off","Share off"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")

            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")      
#--------------------------------------------------
            elif msg.text in ["Status bot"]:
				if msg.from_ in admin or owner:
					md = ""
					if wait["contact"] == True: md+="[􀜁􀇔Mask􏿿] CONTACT : [✅]\n"
					else: md+="[􀜁􀇔Mask􏿿] CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="[􀜁􀇔Mask􏿿] AUTOJOIN : [✅]\n"
					else: md +="[􀜁􀇔Mask􏿿] AUTOJOIN : [❌]\n"
					if wait["leaveRoom"] == True: md+="[􀜁􀇔Mask􏿿] AUTOLEAVE : [✅]\n"
					else: md+="[􀜁􀇔􀜁􀇔Mask􏿿􏿿] AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="[􀜁􀇔Mask􏿿] SHARE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="[􀜁􀇔Mask􏿿] AUTOADD : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="[􀜁􀇔Mask􏿿] COMMENT : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] COMMENT : [❌]\n"
					if wait["likeOn"] == True: md+="[􀜁􀇔Mask􏿿] AUTOLIKE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AUTOLIKE : [❌]\n"
					if wait["Wc"] == True: md+="[􀜁􀇔Mask􏿿] WELCOME : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] WELCOME : [❌]\n"
					if wait["Lv"] == True: md+="[􀜁􀇔Mask􏿿] LEAVE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] LEAVE : [❌]\n"
					if wait["tag"] == True: md+="[􀜁􀇔Mask􏿿] TAG 1 : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] TAG 1 : [❌]\n"
					if wait["auto"] == True: md+="[􀜁􀇔Mask􏿿] AutoBot Join : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AutoBot Join : [❌]\n"
					if wait["auto"] == True: md+="[􀜁􀇔Mask􏿿] Autoread On : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] Autoread Off : [❌]\n"
					if wait["auto"] == True: md+="[􀜁􀇔Mask􏿿] Auto Sider : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] Auto Sider : [❌]\n"
					if wait["auto"] == True: md+="[􀜁􀇔Mask􏿿] Simisimi On : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] Simisimi Off : [❌]\n"
					cl.sendText(msg.to,md)
#--------------------------------------------------
            elif "album merit " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â�1�7�1�71¤7 Å’Ã¦Â²Â¡Ã¥Å�1�7�Â¨Ã£â�1�7�¬â€ 1�71¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â�1�7�1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å 1�71¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
#--------------------------------------------------
            elif "album " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â�1�7�1�71¤7 Å’Ã¦Â²Â¡Ã¥Å�1�7�Â¨Ã£â�1�7�¬â€ 1�71¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â�1�7�1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å 1�71¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
#--------------------------------------------------
            elif "album remove " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë 1�7 Ã©â„¢Â¤Ã¤Âºâ�1�7�1�71¤7 Ã¤Âºâ 1�71¤7¹Ã§Å¡â 1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å’Ã£â�1�7�¬â€ 1�71¤7")
            elif msg.text in ["Group id","Ã§Â¾Â¤Ã§Âµâ€žÃ¥â�1�7�1�71¤7¦Â¨id"]:
				if msg.from_ in admin or owner:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
#--------------------------------------------------
            elif msg.text in ["Clear"]:
				if msg.from_ in admin or owner:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"Ã¦â€¹â�1�7�1�71¤7™Ã§Â»ÂÃ¤Âºâ�1�7�1�71¤7 Ã¥â 1�71¤7¦Â¨Ã©Æ’Â¨Ã§Å¡â�1�7�1�71¤7žÃ©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif "album removeÃ¢â€ â�1�7�1�71¤7 1�71¤7" in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album removeÃ¢â€ â�1�7�1�71¤7 1�71¤7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë 1�7 Ã©â„¢Â¤Ã¤Âºâ�1�7�1�71¤7 Ã¤Âºâ 1�71¤7¹Ã§Å¡â 1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å’Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Add on","Auto add:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Add off","Auto add:off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif "Message change: " in msg.text:
				if msg.from_ in admin or owner:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin or owner:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneÃ£â‚¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Message","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¥â€¢ÂÃ¥â�1�7�¬â�1�7�¢Ã¨ÂªÅ¾Ã§Â¢ÂºÃ¨ÂªÂ�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â�1�7�1�71¤7š\n\n" + wait["message"])
#--------------------------------------------------
            elif "Comment:" in msg.text:
				if msg.from_ in admin or owner:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
#--------------------------------------------------
            elif "Add comment:" in msg.text:
				if msg.from_ in admin or owner:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Ã£â€šÂ³Ã£Æ�1�7�Â¡Ã£Æ�1�7�Â³Ã£Æ�1�7�Ë�1�7�1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Comment on","Comment:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã©Â¦â 1�71¤7“Ã�1�7�1�71¤7 ÂÃ§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã¯Â¼Å¡Ã©â�1�7�1�71¤7“â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
            elif msg.text in ["Ã£â€šÂ³Ã£Æ�1�7�Â¡Ã£Æ�1�7�Â³Ã£Æ�1�7�Ë�1�7�1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Comment on","Comment off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã©Â¦â 1�71¤7“Ã�1�7�1�71¤7 ÂÃ§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã¯Â¼Å¡Ã©â�1�7�1�71¤7”Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
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
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
            elif msg.text in ["Comment","Ã§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã§Â¢ÂºÃ¨ÂªÂ�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
#---------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin or owner:
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
#--------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin or owner:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin or owner:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin or owner:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin or owner:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin or owner:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin or owner:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
#-----------------------------------------------
            elif msg.text in ["Tagall","Mentionall"]:
                              group = cl.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                              if jml <= 100:
                                 mention(msg.to, nama)
                              if jml > 100 and jml < 200:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                              if jml > 200 and jml < 300:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                              if jml > 300 and jml < 400:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, 299):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                                 for l in range (300, len(nama)-1):
                                     nm4 += [nama[l]]
                                 mention(msg.to, nm4)
                              cnt = Message()
                              cnt.text = "Hasil Tag : "+str(jml)
                              cnt.to = msg.to
                              cl.sendText(msg.to,"TAGALL SUCCESS")
                              cl.sendMessage(cnt)
#-----------------------------------------------
            elif msg.text in ["Bot pergi"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.sendText(msg.to,"Sɪᴀᴘ ʙᴏᴢᴢ!! Lasanakan!!\n\nBʏᴇ,, Bʏᴇᴇ... " + str(ginfo.name) + "\nJᴀɴɢᴀɴ Lᴜᴘᴀ Bᴀʜᴀɢɪᴀ...")
							cl.leaveGroup(msg.to)
							print "[Command]Bot pergi"
						except:
							pass
#-----------------------------------------------
            elif "Gruplist" in msg.text:
                if msg.from_ in owner:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "☄ %s  \n" % (cl.getGroup(i).name + " 👥 ▄ [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")
#-----------------------------SALAM or SELAMAT--------------------------------------
            elif msg.text in ["Pagi","Pagi all","Pagi semua","Pageeh","Vagi","Vageeh"]:
                cl.sendText(msg.to,"Pagi kak...")
                cl.sendText(msg.to,"Buruan mandi gih,, bau jigong tuh")
                cl.sendText(msg.to,"Wkwkwk")
                cl.sendText(msg.to,"Dan buruan sarapan 😁")
            elif msg.text in ["Assalamu alaikum","Salamu alaikum","Assalamu ‘alaikum"]:
                cl.sendText(msg.to,"وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
#-----------------------------------------------
            elif msg.text == "Set sider":
                    cl.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Cek sider"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "Yang baca ↴\n  ===========================                     %s\n===========================\n\nTukang nyimak ↴\n%s\n===========================\nIn the last seen point:\n[%s]\n===========================" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        cl.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik [Set sider] dulu")
#-------------------------------------
            elif "Bot rename " in msg.text:
              if msg.from_ in admin or owner:
                string = msg.text.replace("Bot rename ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"UpdateName => " + string + " <= Success")
#-----------------------------------------------
            elif msg.text in ['kontol','Kontol','jancuk','Jancuk','jancok','Jancok','asu','Asu','jembut','Jembut','jembot','Jembot','tempek','Tempek','itil','Itil','makmu','Makmu','mak mu','Mak mu']:
              if msg.from_ in admin or owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    cl.sendMessage(msg)
                    cl.sendMessage(msg)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Lag"]:
                cl.sendText(msg.to,"44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Sepi"]:
                cl.sendText(msg.to,"Mᴇɴᴛɪᴏɴᴀʟʟ Oʀ Tᴀɢᴀʟʟ")
            elif msg.text in ["Mister","Mr"]:
                cl.sendText(msg.to,"Sɪᴀᴘ ʙᴏᴢᴢ")
            elif msg.text in ["Test","test","Tes","tes"]:
                cl.sendText(msg.to,"Cᴇᴋ")
                cl.sendText(msg.to,"1")
                cl.sendText(msg.to,"2")
                cl.sendText(msg.to,"3")
                cl.sendText(msg.to,"Pᴏꜱɪᴛɪғ ʙᴏᴢᴢ")
                cl.sendText(msg.to,"Sᴇʟᴀᴍᴀᴛ ʏᴀ... 􀜁􀅔haha􏿿")
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                jawab = ['Aʜ Kᴜᴘʀᴇᴛ Lᴜ','Mᴜᴋᴀ Lᴜ Kᴀʏᴀ Jᴀᴍʙᴀɴ','Aᴅᴀ Oʀᴀɴɢ ᴋᴀʜ ᴅɪꜱɪɴɪ?','Sᴀɴɢᴇ Eᴜʏ','Aᴅᴀ Pᴇʀᴀᴡᴀɴ Nɢᴀɴɢɢᴜʀ ɢᴀ Cᴏʏ?']
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
                cl.sendText(msg.to,"Kita nge-spam kuy!")
                cl.sendText(msg.to,"Kuy 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Kuy 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"3")
                cl.sendText(msg.to,"2")
                cl.sendText(msg.to,"1")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Kurang ga? 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"KURAAAANG BANYAAK")
                cl.sendText(msg.to,"Kurang Mastaah")
                cl.sendText(msg.to,"Ok!")
                cl.sendText(msg.to,"Tambah ya! 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Udh cukup?")
                cl.sendText(msg.to,"Udh cukup 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Cape nih")
                cl.sendText(msg.to,"Ok sudah.")
                cl.sendText(msg.to,"MAKASIH SEMUA 􀜁􀅔XD􏿿")
                cl.sendText(msg.to,"Done")

            elif msg.text in ["Up up","up up"]:
                cl.sendText(msg.to,"Ha? ada apa nih")
                cl.sendText(msg.to,"Di up in bos")
                cl.sendText(msg.to,"Butuh balon udara nggak?")
                cl.sendText(msg.to,"Buat di up in nih")
                cl.sendText(msg.to,"Gausah lah ya")
                cl.sendText(msg.to,"Up atuh")
                cl.sendText(msg.to,"Panjat bos")
                cl.sendText(msg.to,"Jangan panjat sosyal aja")
                cl.sendText(msg.to,"Panjat panjat pohon")
                cl.sendText(msg.to,"yiha")
                cl.sendText(msg.to,"Pohon aja di panjat")
                cl.sendText(msg.to,"Apalagi kamu.gg unch")
                cl.sendText(msg.to,"Maaf, harus kita up in")
                cl.sendText(msg.to,"Demi kebaikan bersama sayang")
                cl.sendText(msg.to,"Iya sayang")
                cl.sendText(msg.to,"Opo koe krungu?")
                cl.sendText(msg.to,"Jerite atiku")
                cl.sendText(msg.to,"Oaoee..")
                cl.sendText(msg.to,"Males lanjutin ah")
                cl.sendText(msg.to,"Sepi bat")
                cl.sendText(msg.to,"Iya sepi udah udah")
                cl.sendText(msg.to,"Gaada yang denger juga")
                cl.sendText(msg.to,"Yaiyalah, ini kan ketik ogeb")
                cl.sendText(msg.to,"Mending gua nyari BBG dulu")
                cl.sendText(msg.to,"Sono huss")
                cl.sendText(msg.to,"Up unch")
                cl.sendText(msg.to,"Up in dulu bos")
                cl.sendText(msg.to,"Ada apa nih")
                cl.sendText(msg.to,"Up atuh")
                cl.sendText(msg.to,"Maaf di up bos")

            elif msg.text in ["Spam"]:
                cl.sendText(msg.to,"Aku belum mandi")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tapi masih cantik juga")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"apalagi kalau sudah mandi")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Pasti cantik sekali")
                cl.sendText(msg.to,"yiha")
                cl.sendText(msg.to,"Kalau orang lain melihatku")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Badak aku taba bana")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tuntuang")
                cl.sendText(msg.to,"Tapi kalau langsuang diidu")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Atagfirullah baunya")
                cl.sendText(msg.to,"Males lanjutin ah")
                cl.sendText(msg.to,"Sepi bat")
                cl.sendText(msg.to,"Iya sepi udah udah")
                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                cl.sendText(msg.to,"Nah")
                cl.sendText(msg.to,"Mending gua makan dulu")
                cl.sendText(msg.to,"Siyap")
                cl.sendText(msg.to,"Okeh")
                cl.sendText(msg.to,"Katanya owner kita Jomblo ya")
                cl.sendText(msg.to,"Iya emang")
                cl.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                cl.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")

            elif msg.text == "Myspam":
                    cl.sendText(msg.to,"3")
                    cl.sendText(msg.to,"2")
                    cl.sendText(msg.to,"1")
                    cl.sendText(msg.to,"Fuck Off")
                    cl.sendText(msg.to,"Ku mengejar bus yang mulai berjalan")
                    cl.sendText(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    cl.sendText(msg.to,"Kabut dalam hatiku telah menghilang")
                    cl.sendText(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    cl.sendText(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    cl.sendText(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    cl.sendText(msg.to,"Untukku menjadi diri sendiri")
                    cl.sendText(msg.to,"Ku harus jujur, pada perasaanku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untukku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Saat ku sadari sesuatu menghilang")
                    cl.sendText(msg.to,"Hati ini pun resah tidak tertahankan")
                    cl.sendText(msg.to,"Sekarang juga yang bisa ku lakukan")
                    cl.sendText(msg.to,"Merubah perasaan ke dalam kata kata")
                    cl.sendText(msg.to,"Mengapa sedari tadi")
                    cl.sendText(msg.to,"Aku hanya menatap langit")
                    cl.sendText(msg.to,"Mataku berkaca kaca")
                    cl.sendText(msg.to,"Berlinang tak bisa berhenti")
                    cl.sendText(msg.to,"Di tempat kita tinggal, didunia ini")
                    cl.sendText(msg.to,"Dipenuhi cinta, kepada seseorang")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Janji tak lepas dirimu lagi")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Akhirnya kita bisa bertemu")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Ku akan bahagiakan dirimu")
                    cl.sendText(msg.to,"Ku ingin kau mendengarkan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Jika jika kamu ragu")
                    cl.sendText(msg.to,"Takkan bisa memulai apapun")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga")
                    cl.sendText(msg.to,"Jika kau bersuar")
                    cl.sendText(msg.to,"Cahaya kan bersinar")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Sampaikan rasa sayangku ini")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriakkan ditengah angin")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untuk ku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Katakan dengan berani")
                    cl.sendText(msg.to,"Jika kau diam kan tetap sama")
                    cl.sendText(msg.to,"Janganlah kau merasa malu")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga..")
                    cl.sendText(msg.to,"Anugerah terindah adalah ketika kita masih diberikan waktu untuk berkumpul bersama orang-orang yang kita sayangi.")
                    cl.sendText(msg.to,"Cuma dirimu seorang yang bisa meluluhkan hati ini. Kamulah yang terindah dalam hidupku.")
                    cl.sendText(msg.to,"Aku ingin meraih kembali cintamu menjadi kenyataan. Saat diriku dalam siksaan cinta, dirimu melenggang pergi tanpa pernah memikirkan aku.")
                    cl.sendText(msg.to,"Tak ada yang salah dengan CINTA. Karena ia hanyalah sebuah kata dan kita sendirilah yang memaknainya.")
                    cl.sendText(msg.to,"Mencintaimu adalah inginku. memilikimu adalah dambaku. meski jarak jadi pemisah, hati tak akan bisa terpisah.")
                    cl.sendText(msg.to,"Dalam cinta ada bahagia, canda, tawa, sedih, kecewa, terluka, semua itu tidak akan terlupakan dalam hal cinta, itu yang artinya cinta.")
                    cl.sendText(msg.to,"Seseorang yang berarti, tak akan dengan mudah kamu miliki. Jika kamu sungguh mencintai, jangan pernah berhenti berusaha untuk hati.")
                    cl.sendText(msg.to,"Jika esok pagi menjelang, akan aku tantang matahari yang terbangun dari tidur lelap nya.")
                    cl.sendText(msg.to,"Ketulusan cinta hanya dapat dirasakan mereka yang benar-benar mempunyai hati tulus dalam cinta.")
                    cl.sendText(msg.to,"Kamu tak perlu menjadikan dirimu cantik/ganteng untuk bisa memilikiku, kamu hanya perlu menunjukkan bahwa aku membutuhkanmu.")
                    cl.sendText(msg.to,"Ada seribu hal yang bisa membuatku berpikir ununtuk meninggalkanmu, namun ada satu kata yang membuatku tetap disini. Aku Cinta Kamu.")
                    cl.sendText(msg.to,"Aku pernah jatuhkan setetes air mata di selat Sunda. Di hari aku bisa menemukannya lagi, itulah waktunya aku berhenti mencintaimu.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang ku bahagia kadang ku bersedih.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Saat jarak memisahkan, satu yang harus kamu ketahui. Akan aku jaga cinta ini ununtukmu.")
                    cl.sendText(msg.to,"Bersandarlah di pundaku sampai kau merasakan kenyamanan, karena sudah keharusan bagiku ununtuk memberikanmu rasa nyaman.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun untuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun ununtuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Cinta merupakan keteguhan hati yang ditambatkan pada kemanusiaan yang menghubungkan masa lalu, masa kini dan masa depan.")
                    cl.sendText(msg.to,"Ketika mencintai seseorang, cintailah apa adanya. Jangan berharap dia yang sempurna, karena kesempurnaan adalah ketika mencinta tanpa syarat.")
                    cl.sendText(msg.to,"Cinta bukanlah tentang berapa lama kamu mengenal seseorang, tapi tentang seseorang yang membuatmu tersenyum sejak kamu mengenalnya.")
                    cl.sendText(msg.to,"Ketika mereka bertanya tentang kelemahanku, aku ingin mengatidakan bahwa kelemahanku itul adalah kamu. Aku merindukanmu di mana-mana dan aku sanagat mencintaimu.")
                    cl.sendText(msg.to,"Kehadiranmu dalam hidupku, aku tahu bahwa aku bisa menghadapi setiap tantangan yang ada di hadapanku, terima kasih telah menjadi kekuatanku.")
                    cl.sendText(msg.to,"Meneriakkan namamu di deras hujan, memandangmu dari kejauhan, dan berdo’a di hening malam. Cinta dalam diam ini lah yang mampu kupertahankan.")
                    cl.sendText(msg.to,"Perempuan selalu menjaga hati orang yang dia sayangsehingga hati dia sendiri tersiksa. inilah pengorbanan perempuan ununtuk lelaki yang tidak pernah sadar.")
                    cl.sendText(msg.to,"Ketika kau belum bisa mengambil keputusan ununtuk tetap bertahan dengan perasaan itu, sabarlah, cinta yang akan menguatkanmu.")
                    cl.sendText(msg.to,"Aku tidak akan pernah menjajikan ununtuk sebuah perasaan, tapi aku bisa menjanjikan ununtuk sebuah kesetiaan.")
                    cl.sendText(msg.to,"Cinta yang sebenarnya tidak buta, cinta yaitu adalah hal yang murni, luhur serta diharapkan. Yang buta itu jika cinta itu menguasai dirimu tanpa adanya suatu pertimbangan.")
                    cl.sendText(msg.to,"Aku tercipta dalam waktu, ununtuk mengisi waktu, selalu memperbaiki diri di setiap waktu, dan semua waktu ku adalah ununtuk mencintai kamu.")
                    cl.sendText(msg.to,"Cinta akan indah jika berpondasikan dengan kasih sang pencipta. Karena sesungguhnya Cinta berasal dari-Nya Dan cinta yang paling utama adalah cinta kepada Yang Kuasa.")
                    cl.sendText(msg.to,"Bagi aku, dalam hidup ini, hidup hanya sekali, cinta sekali dan matipun juga sekali. Maka tidak ada yang namanya mendua.")
                    cl.sendText(msg.to,"Tuhan..jagalah ia yang jauh disana, lindungi tiap detik hidup yang ia lewati,sayangi dia melebihi engkau menyayangiku.")
                    cl.sendText(msg.to,"Kapan kau akan berhenti menyakitiku, lelah ku hadapi semua ini tapi aku tidak bisa memungkiri aku sangat mencintaimu.")
                    cl.sendText(msg.to,"Ketidakutan terbesar dalam hidupku bukan kehilanganmu, tapi melihat dirimu kehilangan kebahagiaanmu.")
                    cl.sendText(msg.to,"Cinta yang sesungguhnya akan mengatidakan aku butuh kamu karna aku siap ununtuk mencintaimu dan menjalani suka duka bersamamu")
                    cl.sendText(msg.to,"Seseorang pacar yang baik adalah dia yang JUJUR dan tidak pernah membuat kamu selalu bertanya-tanya atau selalu mencurigai dia")
                    cl.sendText(msg.to,"Cinta bukanlah sebuah kata cinta, yang sebenarnya adalah cinta yang menyentuh hati dan perasaan")
                    cl.sendText(msg.to,"Kau datang di saat ke egoisan akan cinta tengah mendera. Membawa cahaya dan kedamaian, membuatku tidak mudah menyerah ununtuk merengkuh kisah cinta bersamamu")
                    cl.sendText(msg.to,"Aku sangat menyukai kebersamaan karena kebersamaan mengajarkan kita tentang suka dan duka di lalui bersama")
                    cl.sendText(msg.to,"Mungkin Tuhan sengaja memberi kita berjumpa dengan orang yang salah sebelum menemui insan yang betul supaya apabila kita akhirnya menemui insan yang betul, kita akan tahu bagaimana ununtuk bersyukur dengan pemberian dan hikmah di balik pemberian tersebut.")
                    cl.sendText(msg.to,"Getaran di hatiku yang lama haus akan belaianmu seperti saat dulu dan kau bisikan kata ‘aku cinta padamu’ aku merindukannya")
                    cl.sendText(msg.to,"Terkadang air mata adalah tanda kebahagiaan yang tidak terucapkan. Dan senyuman adalah tanda sakit yang mencoba ununtuk kuat")
                    cl.sendText(msg.to,"Dicintai dan disayangi kamu adalah anugerah terindah yang tuhan berikan padaku.")
                    cl.sendText(msg.to,"Mencintai kamu butuh waktu beberapa detik, Namun melupakanmu butuh waktu ku seumur hidup.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang aku bahagia dan juga kadang aku bersedih.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu lagi menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Jauh sebelum bertemu denganmu, aku telah mengenalmu dalam doaku.")
                    cl.sendText(msg.to,"Mungkin dia tidak sadar bahwa aku itu cemburu dan mungkin juga dia tidak merasa bahwa aku sangat terluka, tidak mendengar bahwa hatiku sedang menangis.")
                    cl.sendText(msg.to,"Kehadirmu membawa cinta, memberi bahagia, dan juga rasa rindu yang tiada pernah ada akhirnya.")
                    cl.sendText(msg.to,"Aku nngak mau jadi wakil rakyat, aku maunya jadi wali murid yang ngambil raport anak kita besok.")
                    cl.sendText(msg.to,"Seperti hujan yang turun di tanah yang tandus, seperti itulah arti hadirmu dengan cinta dan kasih sayang untukku.")
                    cl.sendText(msg.to,"Tanda-tanda cinta adalah ketika anda merasa bahwa kebahagiaan orang tersebut lebih penting daripada kebahagiaanmu sendiri.")
                    cl.sendText(msg.to,"Cinta tidak hanya apa yang anda rasakan, tetapi apa yang harus anda lakukan.")
                    cl.sendText(msg.to,"Cinta adalah sebuah kekuatan untuk melihat kesamaan dan tidak kesamaan.")
                    cl.sendText(msg.to,"Cinta adalah pengalaman penuh emosi yang dirasakan banyak orang tetapi hanya beberapa orang saja yang bisa menikmatinya.")
                    cl.sendText(msg.to,"Cinta adalah berbagi. Karena walau ada di dua raga yang berbeda, setiap pasangan hanya memiliki satu hati.")
                    cl.sendText(msg.to,"Saat kita berjauhan, sebenarnya hanya raga kitalah yang jauh. Namun hati kita selalu dekat, karena hatiku ada di hatimu.")
                    cl.sendText(msg.to,"Cinta datang dengan pengorbanan yang akan memberikan petunjuk siapa diri kita yang sebenarnya.")
                    cl.sendText(msg.to,"Cinta begitu lembut dan merdu, namun jangan kau gunankan untuk merayu. Karena rayuan hanyalah akan mengosongkan makna kecintaan yang sesungguhnya.")
                    cl.sendText(msg.to,"Cinta bukanlah penuntutan, penguasaan, pemaksaan, dan pengintimidasian. Tak lain itu hanyalah cara manusia mendefinisikannya. Karena cinta adalah perjuangan, pengorbanan, tanggungjawab, kejujuran, dan keikhlasan.")
                    cl.sendText(msg.to,"Derajat cinta hanya bisa diukur dengan seberapa besar “Pemberian” yang kita korbankan.")
            elif msg.text in ["Ngantuk","Sleep","Nite","Good night"]:
                cl.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")

            elif msg.text in ["Pekok","Pea","Dudul"]:
                cl.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"􀜁􀅔Har Har􏿿")

            elif msg.text in ["PING","Ping","ping"]:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")

            elif msg.text in ["Bot resek ae coeg","Berisik","Rame ae","Rame wae","Sepi bet","Sepi banget","Sepi Bgt"]:
                cl.sendText(msg.to,"Kasian dy jones 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")

            elif "Pap creator" in msg.text:
                tanya = msg.text.replace("Pap creator","")
                link = ["http://dl.profile.line-cdn.net/0hMJ3w03iOEmUODj51FXRtMjJLHAh5IAMtYGhbUHsOSAclNlYxMW4NAnxaSgEmOAUxZThaCikPRFVz","http://dl.profile.line-cdn.net/0hMJ3w9GpxEmUODj6JvWxtMjJLHAh5IAMtYGhbUHsOSAclNlYxMW4NAnxaSgEmOAUxZThaCikPRFVz","http://dl.profile.line-cdn.net/0hMJ3wzUdrEmUODj6JveNtMjJLHAh5IAMtYGhbUHsOSAclNlYxMW4NAnxaSgEmOAUxZThaCikPRFVz","http://dl.profile.line-cdn.net/0hMJ3w5Xh8EmUODj6JvY9tMjJLHAh5IAMtYGhbUHsOSAclNlYxMW4NAnxaSgEmOAUxZThaCikPRFVz"]
                pilih = random.choice(link)
                cl.sendImageWithURL(msg.to,pilih)
#----------------------
            elif "Pap cecan" in msg.text:
                tanya = msg.text.replace("Pap cecan","")
                jawab = ("https://i.pinimg.com/736x/fa/b0/de/fab0def5ba3108d51ba40747791bb089.jpg","https://i.pinimg.com/736x/8b/c6/0e/8bc60e8fd6fb5d142a074b6d2cf5c7ed.jpg","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQAa0KQ8XfoVfKRh82Ys63AX3VcuPml1JJFLk7iTEtMpmd7OzbN-yk_MGK6","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPMwr1Igswf8wgrTURHbGAt9jn54SvimA6Ps6W6lCtItkrh4I-kA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg5SRVDjILsjUyBeLkBnbV96kX22_1mplLyjfCKws6nv8E_VtMDyV07e56bw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXZ4yFF8R8vPVmEl21Txhvzh4YpUJkJ2uuO3KQLUzYIEVsuT9")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
#----------------------
            elif "Pap cogan" in msg.text:
                tanya = msg.text.replace("Pap cogan","")
                jawab = ("https://i.pinimg.com/736x/41/9b/a5/419ba5606edf61dbab6dfdcc8014624d.jpg","https://i.pinimg.com/736x/38/9c/b1/389cb1203841730a1a8ba322daa7ecb0.jpg","https://i.pinimg.com/736x/76/e3/dc/76e3dc311ddbd61f666083b963910cea.jpg","https://i.pinimg.com/736x/e4/96/67/e496676ca6ea785c8ca5d28f514f9b69.jpg","https://i.pinimg.com/736x/c7/c9/d6/c7c9d6ee5e7d5214d89e3d8bab964497.jpg","https://i.pinimg.com/736x/98/79/5c/98795c07ad9b84ef22e4a6c2cdb135cc.jpg","https://i.pinimg.com/736x/63/fe/b0/63feb07620c1fab54e98ed2139be8aae.jpg","https://i.pinimg.com/736x/66/fc/f2/66fcf2d7d405398f8f163c4ea61aafbf.jpg","https://i.pinimg.com/736x/d9/52/ca/d952caf7b7de45d70f058be2b44e28b3.jpg","https://i.pinimg.com/736x/34/59/c5/3459c5208c819675eff6273210eed009.jpg","https://i.pinimg.com/736x/2a/55/76/2a557666df14a2594f6f3aade212021e.jpg","https://i.pinimg.com/736x/f0/b7/d5/f0b7d5140ec2fb65e58a53bef4506b52.jpg","https://i.pinimg.com/736x/ea/7b/4d/ea7b4d364c0150060e6b9bca249527b9.jpg","https://i.pinimg.com/736x/05/45/a4/0545a45040b9e368726bc134abf78075.jpg","https://i.pinimg.com/736x/f5/92/3a/f5923a99bfd83e0d8f7c0362e649c33a.jpg","http://dl.profile.line-cdn.net/0hMJ3wh4HFEmUODj6JvBNtMjJLHAh5IAMtYGhbUHsOSAclNlYxMW4NAnxaSgEmOAUxZThaCikPRFVz")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#----------------------
            elif "Pap abs" in msg.text:
                tanya = msg.text.replace("Pap abs","")
                jawab = ("https://i.pinimg.com/736x/80/1f/e8/801fe86de5b3768ac2994230b1a579e2.jpg","https://i.pinimg.com/736x/a0/e4/89/a0e489d5aeb8cc33c902f49b3b1f8006.jpg","https://i.pinimg.com/736x/91/b0/ee/91b0ee956c46b29f74b0e6d015be3255.jpg","https://i.pinimg.com/736x/f4/92/4d/f4924d75fe3170a73929fa3408592c86.jpg","https://i.pinimg.com/736x/d5/31/ba/d531ba0b7e72056eaedffa54620707e9.jpg","https://i.pinimg.com/736x/51/9b/99/519b9954e1b2ca5f4ab18a4e7c325619.jpg","https://i.pinimg.com/736x/3c/31/8c/3c318cae8e2a5e41ea1ed326737bf12f.jpg","https://i.pinimg.com/736x/87/d3/cb/87d3cb48f2e8eef33a49cd28d971d14b.jpg","https://i.pinimg.com/736x/0d/a3/57/0da357eeeeb9711317f2755a525d07db.jpg","https://i.pinimg.com/736x/09/7a/22/097a2296802dc6535edf1f10d35e64e8.jpg","https://i.pinimg.com/736x/e7/75/cc/e775cc97b9d52777f561daf284ace68b.jpg","https://i.pinimg.com/736x/76/bd/bf/76bdbfa728dcc6dfdd90cb816310af75.jpg","https://i.pinimg.com/736x/49/3a/98/493a988a4872216568844b319f022ac9.jpg","https://i.pinimg.com/736x/f0/f1/cf/f0f1cf3a347dd44c7416ca7baf2da7ed.jpg")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
#----------------------
            elif "Pap toket" in msg.text:
                tanya = msg.text.replace("Pap toket","")
                jawab = ("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTilO50kExe4q_t-l8Kfn98sxyrHcbWPWCu2GP2SNgg8XWGMaZc8h5zaxAeVA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgSYYgB33GP3LAvVSYxKjDlbPokmtzSWjbWJogz8lbZMNSyvqJTE3qWpwBg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgwKO_CAdZpSlXVVfA29qglGQR00WHkeqq4JakyYDuzIW2tKhvGg","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSC3ZMq4PnCX5dj7Fc_N6HOG6R_XrmOM7r6uBtpEcBfbO4hMEXQirK_lU_ePw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgynJUxS4uYgaIiV_R6e4FY62QfhYRUEgYZg6psfJzWH_ci4dFng")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
            elif "Pap anu" in msg.text:
                tanya = msg.text.replace("Pap anu","")
                jawab = ("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQFFKdXErF56KzAa4oWnWQT34jmGKJ66lj1g0hnN4zwYh9GgW0dHWZfRnuM","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQTn4_JMD1ZAg-XIk6JZ1Crhz9gtXEIS8AcjTA3SYmazAutt7ekHw","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTIVuITo7KicaU6UwPhol1Rvkq4aQwznly8Xl2SiTlAa_1FrSHuwhwV5XoElA")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
						
            elif msg.text in ["Raisa"]:
                    try:
                        cl.sendImageWithURL(msg.to, "https://cdn.brilio.net/news/2017/05/10/125611/750xauto-selalu-tampil-cantik-memesona-ini-harga-10-sepatu-raisa-andriana-170510q.jpg")
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
#-----------------------------------------------
            elif msg.text in ["Mode:on","mode:on"]:
                if msg.from_ in admin or owner:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag On")
                        else:
                            cl.sendText(msg.to,"already on")
#=================================================
            elif msg.text in ["Mode Off","mode off"]:
                if msg.from_ in admin or owner:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already Tag off")
                        else:
                            cl.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag Off")
                        else:
                            cl.sendText(msg.to,"Already Tag off")
#===================================================
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u3cfa63811888b3a880bc4f348a95b23b"}
					cl.sendMessage(msg)
					cl.sendText(msg.to,'Mʏ Cʀᴇᴀᴛᴏʀ👉 line.me/ti/p/~tak.dapat.tidur')
#-------------Fungsi Creator Finish-----------------#
            elif "Spam: " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
#----------------------------------------------------
            elif "Botstatus " in msg.text:
              if msg.from_ in admin or owner:
                string = msg.text.replace("Botstatus ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "dubbing " in msg.text.lower():
                say = msg.text.lower().replace("dubbing ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#--------------------
            elif 'wikipedia: ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wikipedia: ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
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
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                cl.sendText(msg.to,jawaban)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + "\nBanyak banyak tobat Nak ")
            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")
#-----------------------------------------------
            elif "Steal group" in msg.text:
                   group = cl.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   cl.sendImageWithURL(msg.to, path)
#-----------------------------------------------
            elif "Name: @" in msg.text:
                    _name = msg.text.replace("Name: @","")
                    _nametarget = _name.rstrip(" ")
                    gs = cl.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                      else:
                        pass

            elif "Bio: @" in msg.text:
                    _name = msg.text.replace("Bio: @","")
                    _nametarget = _name.rstrip(" ")
                    gs = cl.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          cl.sendText(msg.to,"[Status]:\n" + h.statusMessage )
                      else:
                        pass

            elif "Getprofile:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nᴀᴍᴀ :\n" + contact.displayName + "\n\nBɪᴏ :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Pʀᴏғɪʟᴇ Pɪᴄᴛᴜʀᴇ " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cᴏᴠᴇʀ " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass

            elif "Getinfo:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[Dɪꜱᴘʟᴀʏ Nᴀᴍᴇ]:\n" + contact.displayName + "\n\n[Mɪᴅ]:\n" + contact.mid + "\n\n[Bɪᴏ]:\n" + contact.statusMessage + "\n\n[Pʀᴏғɪʟᴇ Pɪᴄᴛᴜʀᴇ]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cᴏᴠᴇʀ]:\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[Dɪꜱᴘʟᴀʏ Nᴀᴍᴇ]:\n" + contact.displayName + "\n\n[Mɪᴅ]:\n" + contact.mid + "\n\n[Bɪᴏ]:\n" + contact.statusMessage + "\n\n[Pʀᴏғɪʟᴇ Pɪᴄᴛᴜʀᴇ]:\n" + str(cu))

            elif "Contact:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Info: @" in msg.text:
                _name = msg.text.replace("Info: @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong","Kalau pagi cowo","Kalau pagi cewe")
                        wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur","Kembaran miper","Tidak beraturan")
                        status = ("Menikah","Pacaran","Jones","Gamon dari mantan")
                        k = random.choice(kelamin)
                        w = random.choice(wajah)
                        s = random.choice(status)
                        cl.sendText(msg.to,"Dᴇᴛᴀɪʟ ɪɴғᴏ :\n Nᴀᴍᴀ : "+xname+"\n Kᴇʟᴀᴍɪɴ : "+k+"\n Wᴀᴊᴀʜ : "+w+"\n Sᴛᴀᴛᴜꜱ Kᴇʜɪᴅᴜᴘᴀɴ : "+s)

            elif "Status: @" in msg.text:
                _name = msg.text.replace("Status: @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        kelamin = ("Keturunan darah biru","Keturunan darah kotor","Saudaranya miper","Keturunan kerajaan","Keturunan ubab","Anaknya miper","Kembaran dijjah")
                        wajah = ("Gajelas","Digantungin doi","Status ngambang kek anu","Pacaran","Bentar lagi Nikah","Menikah","Jomblo","Jonez seumur hidup","Menyedihkan")
                        status = ("Jodohnya miper","Jodohnya Dijjah","Jodohnya artis","Jodohnya dari khayangan","Gapunya jodoh","Jodohnya ganti ganti","Kan jonez gapunya jodoh:'v")
                        k = random.choice(kelamin)
                        w = random.choice(wajah)
                        s = random.choice(status)
                        cl.sendText(msg.to,"Dᴇᴛᴀɪʟ ɪɴғᴏ :\n Nᴀᴍᴀ : "+xname+"\n Kᴇʟᴀᴍɪɴ : "+k+"\n Sᴛᴀᴛᴜꜱ : "+w+"\n Jᴏᴅᴏʜ : "+s)

            elif "love " in msg.text:
                tanya = msg.text.replace("love ","")
                jawab = ("10%\nCoba lah untuk melupakan","20%\nKu tak tau lagi:'","30%\nButuh perjuangan yang berat inih","40%\nCobalah saling mencimtai dengan tulus\nIngatlah kenangan indah kalian","50%\nSegeralah mengerti satu sama lain","60%\nLebih perhatian lagi oke","70%\nAyo sedikit lagi","80%\nWahhh, ada kemungkinan kalian jodoh","90%\nAyo sedikit lgi kak","100%\nKeterangan Moga - Moga Langgeng Ya Kak","0%\nKeterangan Ngak Cinta Sama Sekali :v")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)

            elif msg.text in ["Ajg","Bgst","Bacot","Tai","Bazeng","Anjir","Fck","Fuck","Najiz","Bego","Najis"]:
#              if msg.from_ in admin:
                cl.sendText(msg.to,"Hayo jangan ngomong kasar kak")
                cl.sendText(msg.to,"Aku kick nih.gg")

            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.like(url[25:58], url[66:], likeType=1002)
                     cl.like(url[25:58], url[66:], likeType=1004)
                     cl.like(url[25:58], url[66:], likeType=1003)
                     cl.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     cl.comment(url[25:58], url[66:], wait["comment2"])
                     cl.comment(url[25:58], url[66:], wait["comment3"])
                     cl.comment(url[25:58], url[66:], wait["comment4"])
                     cl.comment(url[25:58], url[66:], wait["comment5"])
                     cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))
#-----------------------------------------------
            elif "zodiak " in msg.text:
                tanggal = msg.text.replace("zodiak ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#----------------------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk,executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
#-------------------------------------------------------------
            elif "Gbc: " in msg.text:
                if msg.from_ in admin or owner:
                    bctxt = msg.text.replace("Gbc: ", "")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendText(manusia, (bctxt))
            elif "Pm cast: " in msg.text:
                if msg.from_ in admin or owner:
					bctxt = msg.text.replace("Pm cast: ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Fbc: " in msg.text:
                if msg.from_ in admin or owner:
                    bctxt = msg.text.replace("Fbc: ", "")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendText(manusia, (bctxt))
#------------------------------------------------------
            elif "Gethome @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Gethome @","")    
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
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
#-----------------------------------------------
            elif "Getpp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpp @","")
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
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
#--------------------------------------------
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
								
            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                cl.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                cl.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                cl.sendText(msg.to,"Send Contact") 

            elif msg.text in ["Autolike on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Autolike off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")

#--------------------------
            elif msg.text in ["Njoin on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Njoin off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")
#--------------------------
            elif msg.text in ["Nleave on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Nleave off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")

            elif msg.text in ["Autoread:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Autoread:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto read Off")

            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                cl.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                cl.sendText(msg.to,"Simisimi Di Nonaktifkan")
##--------------------------
            elif 'music: ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music: ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
#                    r = requests.get('http://ide.ntorp.us/joox/client' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        songz = song[5].encode('utf-8')
                        lyric = songz.replace('ti:','Title -')
                        lyric = lyric.replace('ar:','Artist -')
                        lyric = lyric.replace('al:','Album -')
                        removeString = "[1234567890.:]"
                        for char in removeString:
                            lyric = lyric.replace(char,'')
                        cl.sendText(msg.to, hasil)
                        cl.sendAudioWithURL(msg.to, song[4])
                        cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') + "\n\n" + lyric)
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#------------------------------------------------
            elif 'lirik: ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik: ','')
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
#-----------------------------------
            elif "idline: " in msg.text:
                id = msg.text.replace("idline: ", "")
                find = cl.findContactsByUserId(id)
                for findid in find:
                    try:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': findid.mid}
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
#-----------------------------------
            elif "Getgroup" in msg.text:
                group = cl.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                cl.sendImageWithURL(msg.to, path)
#----------------------------------
            elif "Leavegroup " in msg.text.split():
                if msg.from_ in admin or owner:
                    ng = msg.text.split().replace("Leavegroup ","")
                    gid = cl.getGroupIdsJoined()
                    if msg.from_ in admin or owner:
                        for i in gid:
                            h = cl.getGroup(i).name
                    if h == ng:
                        cl.sendText(i,"Bot di paksa keluar oleh owner!")
                        cl.leaveGroup(i)
                        cl.sendText(msg.to,"Success left ["+ h +"] group")
                #else:
                    #pass
            #else:
                #cl.sendText(msg.to,"Khusus Creator/Admin")
            elif msg.text in ["LG"]: #Melihat List Group
                if msg.from_ in admin or owner:
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
            elif "Invitegrup " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Invitegrup ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#----------------------------------
            elif "Getcontact: " in msg.text:
              if msg.from_ in admin or owner:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
#----------------------------------
            elif "youtube search: " in msg.text.lower():
                 query = msg.text.lower().replace("youtube search: ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'https://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             cl.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'https://www.youtube.com' + a['href'])
                             print '[Command] Youtube Search'

            elif 'youtube: ' in msg.text.lower():
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
	                            print(e)

            elif "Vidio " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Vidio ", "").strip()
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
#---------------------------------
#-----------------------------------------
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin or owner:
                    eltime = time.time() - mulai
                    van = "Bot sudah berjalan selama "+waktu(eltime)
                    cl.sendText(msg.to,van)
#-----------------------------------------
            elif msg.text in ["Bot restart"]:
                if msg.from_ in owner:
                    cl.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
#-----------------------------------------
            elif msg.text in ["Like temen","Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
#-----------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName

                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")

            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")

            elif msg.text in ["Auto on"]:
                if msg.from_ in admin or owner:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join on")
                        else:
                            cl.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join On")
                        else:
                            cl.sendText(msg.to,"Bot join On")

            elif msg.text in ["Auto off"]:
                if msg.from_ in admin or owner:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join off")
                        else:
                            cl.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join off")
                        else:
                            cl.sendText(msg.to,"Bot join off")
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in admin or owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    cl.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")

            elif "Admrem @" in msg.text:
                if msg.from_ in admin or owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist bot"]:
              if msg.from_ in admin or owner:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Sabar Dikit Mamang.....")
                    mc = "🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖"
                    for mi_d in admin:
                        mc += "☄1�7 " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("Besok","Tahun Depan","Minggu Depan","Satu Abad Lagi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Waktu" in msg.text:
	    	       wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	               cl.sendText(msg.to, "         Waktu/Tanggal\n\n" + (wait2['setTime'][msg.to]))
	               cl.sendText(msg.to, "Mungkin Tidak Sesuai Atau Sesuai Dengan Tanggal/Waktu Sekrang Dikarenakan Ini Robot Bukan Manusia :v")
#-----------------------------------------------
#-----------------------------------------------
            elif "Quotes" in msg.text:
                tanya = msg.text.replace(".quotes","")
                jawab = ("Don't cry because it's over, smile because it happened.\nDr. Seuss","I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.\nMarilyn Monroe","Be yourself; everyone else is already taken.\nOscar Wilde","Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.\nAlbert Einstein","Jangan makan, berat\nNanti kamu gendutan:'v","Nggak perlu orang yang sexy maupun rupawan untukku\nCukup kamu yang bisa buat aku bahagia")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)

            elif msg.text in ["pap","Pap"]:
                cl.sendImageWithURL(msg.to, "https://i.pinimg.com/736x/d1/93/25/d19325b71789e33bedb054468c1fd134--girls-generation-tiffany-girls-generation.jpg")

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                cl.sendText(msg.to,p)
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                
                cl.sendText(msg.to,p)

            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                cl.sendText(msg.to,p)
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                
                cl.sendText(msg.to,p)

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                cl.sendText(msg.to,p)
#--------------------------------------
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
                #client.sendText(msg.to, rst)
#-----------------------------------------------
            elif "Search image: " in msg.text:
                search = msg.text.replace("Search image: ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass

            elif 'searchimage' in msg.text.lower():
                try:
                    shi = msg.text.lower().replace("searchimage ","")
                    kha = random.choice(items)
                    url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + shi
                    raw_html = (download_page(url))
                    items = items + (_images_get_all_items(raw_html))
                    items = []
                except:
                    try:
                        start = timeit.timeit()
                        cl.sendImageWithURL(msg.to,random.choice(items))
                        cl.sendText(msg.to,"Total Image Links ="+str(len(items)))
                    except Exception as e:
                        cl.sendText(msg.to,str(e))

            elif "anime: " in msg.text.lower():
                van = msg.text.lower().replace("anime: ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"https://myanimelist.net/anime.php?q=" + van)
                cl.sendText(msg.to,"Bener Gak?")

            elif "Google: " in msg.text:
                a = msg.text.replace("Google: ","")
                b = urllib.quote(a)
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to, "https://www.google.com/" + b)
                cl.sendText(msg.to,"Itu Dia Linknya. . .")
                cl.sendImageWithUrl(msg.to,b)

            elif "playstore: " in msg.text.lower():
                tob = msg.text.lower().replace("playstore: ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Tuh link nya boss")
#-----------------------------------------------
            elif 'instagram: ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram: ","")
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
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

            elif "twitter: " in msg.text.lower():
                a = msg.text.replace("twitter: ","")
                b = urllib.quote(a)
                cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                cl.sendText(msg.to, "https://www.twitter.com/" + b)
                cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
#-----------------------------------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                cl.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                cl.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                cl.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                cl.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                cl.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                cl.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                cl.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                cl.sendText(msg.to,str(trans))
#----------------UpdateFotoProfil----------------#
            elif "Cpp" in msg.text:
                if msg.from_ in admin or owner:
                    path = "Robot.jpg"
                    cl.sendText(msg.to,"Update PP :")
                    cl.sendImage(msg.to,path)
                    cl.updateProfilePicture(path)
#--------------------------CEK SIDER------------------------------
            elif "setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------CEK SIDER------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            		elif "Add: " in cmd:
            			target0 = msg.text.replace("Add: ","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "Del: " in cmd:
            			target0 = msg.text.replace("Del: ","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<List Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n☄1�7" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#----------------------------------------------------------------
#--------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() == 'gift01':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                     'PRDTYPE': 'THEME',
                                     'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() == 'gift02':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                     'PRDTYPE': 'THEME',
                                     'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() == 'gift03':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
																		 'PRDTYPE': 'THEME',
																		 'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
								
            elif msg.text.lower() == 'gift04':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
																		 'PRDTYPE': 'THEME',
																		 'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
								
            elif msg.text.lower() == 'gift05':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
																		 'PRDTYPE': 'THEME',
																		 'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
								
            elif msg.text.lower() == 'gift06':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
																		 'PRDTYPE': 'THEME',
																		 'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
								
            elif msg.text.lower() == 'gift012':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
																		 'PRDTYPE': 'THEME',
																		 'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)

            elif "Gift dia 5000c " in msg.text:
              if msg.from_ in admin or owner:
                       msg.contentType = 13
              if msg.from_ in admin or owner:
                       nk0 = msg.text.replace("Gift dia 5000c ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Cʜᴇᴄᴋ Yᴏᴜʀ Gɪғᴛ Bᴏx")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendText(msg.to,_name + "Dᴏɴᴇ 5000 ᴄᴏɪɴ")
                                except:
                                    msg.contentMetadata = {'mid': target}
																		
								
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
#------------------------------
            elif msg.text in ["Line clone","line clone"]:
					cl.sendText(msg.to,"Key:\nLine1\nLine2\nLine3\nLine4\nLine5")
            elif msg.text in ["Line1","line1"]:
					cl.sendText(msg.to,"Clone 1:\nhttps://drive.google.com/open?id=1M4MvuodyebWZ_3ePUySEh3fdhnoWgLes")
            elif msg.text in ["Line2","line2"]:
					cl.sendText(msg.to,"Clone 2:\nhttps://drive.google.com/open?id=1AKDbRW7O-ql4t1wUYe2KkfGahjXvShsJ")
            elif msg.text in ["Line3","line3"]:
					cl.sendText(msg.to,"Clone 3:\nhttps://drive.google.com/open?id=1zUPVQrI8fq9Z0W6IenqtgB5qtLfZq2if")
            elif msg.text in ["Line4","line4"]:
					cl.sendText(msg.to,"Clone 4:\nhttps://drive.google.com/open?id=1SzUe4lqQehfqYC-FsKmsYT7RkLsYAgJV")
            elif msg.text in ["Line5","line5"]:
					cl.sendText(msg.to,"Clone 5:\nhttps://drive.google.com/open?id=1JfStADgnukTsg1CyACR-PN3_cOxGuGpb")
#--------------------------------------
            elif msg.text in ["hmm","hmmm"]:
					cl.sendText(msg.to,"Waduh kenapa? gatel tenggorokan ya")
            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc","Kam","kam"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Sᴇʟᴀᴍᴀᴛ Dᴀᴛᴀɴɢ Dɪ "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#-------------- Add Friends ------------
            elif "botadd @" in msg.text:
                if msg.from_ in admin or owner:
                  if msg.toType == 2:
                    if msg.from_ in admin or owner:
                      print "[Command]Add executing"
                      _name = msg.text.replace("botadd @","")
                      _nametarget = _name.rstrip('  ')
                      gs = cl.getGroup(msg.to)
                      gs = cl.getGroup(msg.to)
                      gs = cl.getGroup(msg.to)
                      gs = kc.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                        if _nametarget == g.displayName:
                          targets.append(g.mid)
                      if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                      else:
                        for target in targets:
                          try:
                            cl.findAndAddContactsByMid(target)
                            cl.senText(msg.to, "Berhasil Menambah Kan Teman")
                          except:
                            cl.sendText(msg.to,"Error")
                  else:
                    cl.sendText(msg.to,"Perintah Ditolak")
                    cl.sendText(msg.to,"Perintah ini Hanya Untuk Admin")
#-------------------------------------------------
            elif "Mid: @" in msg.text:
                if msg.from_ in admin or owner:
                  _name = msg.text.replace("Mid: @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#--------------------------
            elif msg.text in ["Bye all gc"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in admin or owner:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Bʏᴇ,, Bʏᴇᴇ... " + str(ginfo.name) + "\n\nBᴏᴛꜱ Dɪᴘᴀᴋꜱᴀ Kᴇʟᴜᴀʀ ᴏʟᴇʜ Oᴡɴᴇʀ Bᴏᴛꜱ...!!!\nMᴀᴋᴀꜱɪʜ...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#--------------------------
	    elif "Bcgrup: " in msg.text:
		bc = msg.text.replace("Bcgrup: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin or owner:
		    for i in gid:
			cl.sendText(i,"+bc+""\n\n@Bʀᴏᴀᴅᴄᴀꜱᴛ")
		    cl.sendText(msg.to,"Success BC BosQ")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
	    elif msg.text in ["Bot like","bot like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass
		
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#---------------------------------------------------------------------
            elif msg.text in ["Sp","Speed",".sp"]:
					start = time.time()
					cl.sendText(msg.to, "🏹Proses...➴")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%s/Detik" % (elapsed_time))
#------------------------------------------------------------------
            elif "album" in msg.text:
				if msg.from_ in admin or owner:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â�1�7�1�71¤7 1�71¤7" in msg.text:
				if msg.from_ in admin or owner:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecÃ¢â€ â�1�7�1�71¤7 1�71¤7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
#------------------------------------------------------------------
            elif "#rmegs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("#rmegs ","")
                    ap = cl.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[cl]
                        team=random.choice(klis)
                        cl.findAndAddContactsByMid(Mi_d)
                        cl.createGroup(gName, semua)

            elif "Bot spin" in msg.text:
                if msg.from_ in owner:
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.sendText(msg.to,"Success...!!!!")

            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    cl.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Removed all chat Finish")

            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                cl.sendGifWithURL(msg.to,gore)




        if op.type == 59:
            print op


    except Exception as error:
        print error



        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass


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


def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                          print "Like"
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Sain:\n\n🤖 ŤẸÃϻ  ϻÃŇČỖЖ βỖŤ 🤖\n👉 line.me//ti/p/~tak.dapat.tidur")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
