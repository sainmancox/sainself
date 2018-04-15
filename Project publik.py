

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if wait["auto"] == True:
                kr.acceptGroupInvitation(op.param1)
                kr.sendText(op.param1, "Jᴀɴɢᴀɴ ɪɴᴠɪᴛᴇ ꜱᴇᴍʙᴀʀᴀɴɢ ᴏʀᴀɴɢ! Sᴇʟᴀɪɴ ᴅᴀᴘᴀᴛ ɪᴊɪɴ ᴅᴀʀɪ ᴏᴡɴᴇʀ ᴀᴛᴀᴜ ᴀᴅᴍɪɴ. Tᴇʀɪᴍᴀ Kᴀꜱɪʜ")

        if op.type == 5:
            if wait["autoAdd"] == True:
                kr.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait["message"]))

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
                            Name = kr.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kr.sendText(op.param1, "Hey u!! " + "" + nick[0] + "" + "yang abis vcs. . .\npap deh sini (-__-)   ")
#                                       balas = ["Hey u!! " + "" + nick[0] + "" + "yang abis vcs. . .\npap deh sini (-__-)   ","Hey u!! " + "" + nick[1] + "" + "kang cilok, betah banget jadi sider. . .\ngift aim ih (-__-)   ","Hey u!! " + "" + Name + "" + "\nkang intip tetangga???\nSini gabung chat...   "]
#                                       ret_ = "." + random.choice(balas)
#                                       kr.sendText(msg.to,ret_)
                                    else:
                                        kr.sendText(op.param1, "Hey u!! " + "" + nick[1] + "" + "kang cilok, betah banget jadi sider. . .\ngift aim ih (-__-)   ")
                                else:
                                    kr.sendText(op.param1, "Hey u!! " + "" + Name + "" + "\nkang intip tetangga???\nSini gabung chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass


            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = kr.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Don't Tag Me! iam Bussy!" ,cName + " Ada perlu apa ?", "Kenapa" ,cName + " Kangen?","Kangen bilang gak usah tag tag" ,cName + " Apasi?" ,cName + " Pulang gih" ,cName + " Ngapain Ngetag?", "Saya lagi off" ,cName + " Kenapa Tag saya?","SPAM PC aja" ,cName + " Jangan Suka Tag gua, " ,cName + " Kamu siapa?" ,cName + " Kalo sange nggak usah Tag-Tag! Langsung Pc Aja" ,cName + " Maaf... Tidak Melayani Manusia RUWET!!!\ndalam bentuk dan jenis apapun" ,cName + " KAMU KOK JANCOK YA?" ,cName + " Ruwet Tak Pancal RAIMU"]
                     ret_ = "." + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  lang = 'id'
                                  tts = gTTS(text=ret_, lang=lang)
                                  tts.save("hasil.mp3")
                                  kr.sendAudio(msg.to,"hasil.mp3")
                                  kr.sendText(msg.to,ret_)
                                  break


        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                contact = kr.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                kr.sendMessage(c)
                kr.sendImageWithURL(op.param1,image)
                kr.sendText(op.param1, "Pᴇʀɢɪ ʏᴀɴɢ ᴊᴀᴜʜ " + kr.getContact(op.param2).displayName + "")
                kr.sendText(op.param1, "Gᴀᴋ ᴜꜱᴀʜ ʙᴀʟɪᴋ!!! 😈👿")
                kr.sendText(op.param1, "Bᴀʟɪᴋ ʟᴀɢɪ ᴛᴀᴋ ᴍᴀꜱᴜᴋɪɴ ɢᴀɢᴀɴɢ ᴄᴀɴɢᴋᴜʟ ⛏")
                print "MEMBER HAS LEFT THE GROUP"