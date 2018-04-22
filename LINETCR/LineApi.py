# -*- coding: utf-8 -*-
from Api import Poll, Talk, channel
from lib.curve.ttypes import *
import requests
import shutil
import json
import subprocess
from random import randint
from gtts import gTTS

def def_callback(str):
    print(str)

class LINE:

  mid = None
  authToken = None
  cert = None
  channel_access_token = None
  token = None
  obs_token = None
  refresh_token = None


  def __init__(self):
    self.Talk = Talk()
    self._session = requests.session()

  def login(self, mail=None, passwd=None, cert=None, token=None, qr=False, callback=None):
    if callback is None:
      callback = def_callback
    resp = self.__validate(mail,passwd,cert,token,qr)
    if resp == 1:
      self.Talk.login(mail, passwd, callback=callback)
    elif resp == 2:
      self.Talk.login(mail,passwd,cert, callback=callback)
    elif resp == 3:
      self.Talk.TokenLogin(token)
    elif resp == 4:
      self.Talk.qrLogin(callback)
    else:
      raise Exception("invalid arguments")

    self.authToken = self.Talk.authToken
    self.cert = self.Talk.cert

    self.Poll = Poll(self.authToken)
    self.channel = channel.Channel(self.authToken)
    self.channel.login()

    self.mid = self.channel.mid
    self.channel_access_token = self.channel.channel_access_token
    self.token = self.channel.token
    self.obs_token = self.channel.obs_token
    self.refresh_token = self.channel.refresh_token
    self._headers = {
              'X-Line-Application': 'DESKTOPMAC 10.10.2-YOSEMITE-x64 MAC 4.5.0',
              'X-Line-Access': self.authToken,
              'User-Agent': 'Line/8.3.2 iPad4,1 9.0.2'
#              'User-Agent': 'Line/6.0.0 iPad4,1 9.0.2'
               }


  """User"""

  def getProfile(self):
    return self.Talk.client.getProfile()

  def getSettings(self):
    return self.Talk.client.getSettings()

  def getUserTicket(self):
    return self.Talk.client.getUserTicket()

  def updateProfile(self, profileObject):
    return self.Talk.client.updateProfile(0, profileObject)

  def CloneContactProfile(self, mid):
    contact = self.getContact(mid)
    profile = self.getProfile()
    profile.displayName = contact.displayName
    profile.statusMessage = contact.statusMessage
    profile.pictureStatus = contact.pictureStatus
    self.updateDisplayPicture(profile.pictureStatus)
    return self.updateProfile(profile)

  def updateSettings(self, settingObject):
    return self.Talk.client.updateSettings(0, settingObject)


  """Operation"""

  def fetchOperation(self, revision, count):
        return self.Poll.client.fetchOperations(revision, count)

  def fetchOps(self, rev, count):
        return self.Poll.client.fetchOps(rev, count, 0, 0)

  def getLastOpRevision(self):
        return self.Talk.client.getLastOpRevision()

  def stream(self):
        return self.Poll.stream()

  """Message"""

  def kedapkedip(self, tomid, text):
        M = Message()
        M.to = tomid
        t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82"
        t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
        rst = t1 + text + t2
        M.text = rst.replace("\n", " ")
        return self.Talk.client.sendMessage(0, M)

  def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

  def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
  def post_content(self, url, data=None, files=None):
        return self._session.post(url, headers=self._headers, data=data, files=files)
    
  def like(self, mid, postid, likeType=1001):

        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "likeType" : likeType,
            "activityExternalId" : postid,
            "actorId" : mid
        }

        r = requests.post(
            "http://" + self.host + "/mh/api/v23/like/create.json?homeId=" + mid,
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

  def comment(self, mid, postid, text):
        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "commentText" : text,
            "activityExternalId" : postid,
            "actorId" : mid
        }

        r = requests.post(
            "http://" + self.host + "/mh/api/v23/comment/create.json?homeId=" + mid,
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

  def sendImage(self, to_, path):
        M = Message(to=to_, text=None, contentType = 1)
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
        print r
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

  def stalk_instagram():
        """ Function to stalk instagram account and return user profile and top 5 pic """

        try:
            def get_instagram_page_keyword():
                """ Function to return full instagram page link """

                # Find the index of apostrophe
                index_start = text.find("'") + 1
                index_stop = text.rfind("'")

                # Determine whether 2 apostrophe are exist and the text exist
                text_available = (index_stop - index_start) >= 1

                # If user (keyword) exist, crop it
                if text_available:
                    keyword = text[index_start:index_stop]
                    return keyword

                else:
                    return "keyword not found"

            def get_insta_raw_data(page_url):
                """ Function to crawl instagram page to get various data about someone """

                # Try to open instagram page
                try:
                    req = urllib.request.Request(page_url, headers={'User-Agent': "Magic Browser"})
                    con = urllib.request.urlopen(req)
                    page_source_code_text = con.read()
                    mod_page = BeautifulSoup(page_source_code_text, "html.parser")

                except:
                    report = Lines.general_lines("failed to open page") % page_url
                    line_bot_api.push_message(address, TextSendMessage(text=report))
                    raise

                # Parse the raw data, get the script part , select the longest one
                try:
                    rawdatas = mod_page.find_all("script")
                    temp = []
                    for x in rawdatas:
                        temp.append(str(x))
                    rawdatas = max(temp, key=len)

                    # Crop the pre-json part
                    json_raw_text = str(rawdatas)
                    index_start = json_raw_text.find("{")
                    index_stop = json_raw_text.rfind("}") + 1
                    rawdatas = str(json_raw_text[index_start:index_stop])

                except:
                    report = Lines.general_lines("formatting error") % "instagram's page"
                    line_bot_api.push_message(address, TextSendMessage(text=report))
                    raise

                # Convert to JSON data
                json_rawdata = json.loads(rawdatas)

                return json_rawdata

            def get_insta_user_data(json_rawdata):
                """ Function to get insta user data """

                # Get user fullname
                try:
                    insta_fullname = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["full_name"]
                except:
                    insta_fullname = "no data"

                # Get user username
                try:
                    insta_username = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["username"]
                except:
                    insta_username = "no data"

                # Get user biography
                try:
                    insta_biography = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["biography"]
                except:
                    insta_biography = "no data"

                # Get user follower count
                try:
                    insta_follower = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["followed_by"]["count"]
                except:
                    insta_follower = "no data"

                # Get user following count
                try:
                    insta_following = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["follows"]["count"]
                except:
                    insta_following = "no data"

                # Get user privacy status
                try:
                    insta_private = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["is_private"]
                except:
                    insta_private = "no data"

                # Return all the data found
                return insta_fullname, insta_username, insta_biography, insta_follower, insta_following, insta_private

            def get_insta_media_data(json_rawdata):
                """ Function to get insta media data """

                # Try to get the medias data
                try:
                    insta_media = json_rawdata["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"]
                except:
                    report = Lines.general_lines("formatting error") % "posted-media's"
                    line_bot_api.push_message(address, TextSendMessage(text=report))
                    raise

                # Set default value
                insta_image_link_list = []
                insta_image_caption_list = []
                insta_image_like_list = []

                # Get top 5 image / video data
                for item in insta_media:
                    if len(insta_image_link_list) < 5:

                        # Get the media link
                        try:
                            insta_image = item["thumbnail_src"]
                            insta_image_link_list.append(insta_image)
                        except:
                            break

                        # Get the media caption
                        try:
                            insta_image_caption = str(item["caption"]).strip()
                            insta_image_caption_list.append(insta_image_caption)
                        except:
                            insta_image_caption_list.append("-")

                        # Get the media like count
                        try:
                            insta_image_like = item["likes"]["count"]
                            insta_image_like_list.append(insta_image_like)
                        except:
                            insta_image_like_list.append("0")

                    # If there's more than 5 item in image_link_list, stop it
                    else:
                        break

                return insta_image_link_list, insta_image_caption_list, insta_image_like_list

            def send_header():
                """ Function to send header , confirmation that stalking on the way """

                report = (Lines.stalk_instagram("header")).format(keyword)
                line_bot_api.push_message(address, TextSendMessage(text=report))

            def send_insta_user_info(insta_fullname, insta_username, insta_biography, insta_follower, insta_following):
                """ Function to send instagram page user information """

                # Generate report about user information
                report = [Lines.stalk_instagram("user information header")]
                try:
                    report.append(" ")
                    report.append("Fullname : " + str(insta_fullname))
                    report.append("Instagram username: " + str(insta_username))
                    report.append(" ")
                    report.append("Biography : " + str(insta_biography))
                    report.append(" ")
                    report.append("Follower : " + str(insta_follower))
                    report.append("Following : " + str(insta_following))
                except:
                    pass

                report = "\n".join(report)
                line_bot_api.push_message(address, TextSendMessage(text=report))

            def send_insta_user_pic(insta_image_link_list, insta_image_caption_list, insta_image_like_list):
                """ Function to send instagram page media (up to 5) """

                image_count = len(insta_image_link_list)

                carousel_text = []
                header_pic = []
                alt_text = ("Stalking " + keyword + "'s instagram...")
                # Generate and format the data used by carousel
                for i in range(0, image_count):

                    # Format image likes count
                    image_like_count = str(insta_image_like_list[i])+" ♥"

                    # Format image caption
                    if len(insta_image_caption_list[i]) > 45:
                        image_caption = str("\"" + insta_image_caption_list[i][:45] + "...\"")
                    else:
                        image_caption = str("\"" + insta_image_caption_list[i] + "\"")

                    # Join them together and append to carousel text
                    carousel_text.append(str(image_like_count) + "\n" + image_caption)

                    # Append image link to header pic
                    header_pic.append(insta_image_link_list[i])

                if image_count == 0:
                    report = Lines.stalk_instagram("picture count 0")
                    line_bot_api.push_message(address, TextSendMessage(text=report))

                # Else, send result in form of carousel
                else:
                    columns = []
                    for i in range(0, len(header_pic)):
                        carousel_column = CarouselColumn(text=carousel_text[i][:60], thumbnail_image_url=header_pic[i], actions=[
                                URITemplateAction(label='See detail..', uri=header_pic[i])])
                        columns.append(carousel_column)

                    carousel_template = CarouselTemplate(columns=columns)
                    template_message = TemplateSendMessage(alt_text=alt_text, template=carousel_template)
                    line_bot_api.push_message(address, template_message)

            cont = True
            json_rawdata = None

            # Get the full version link
            keyword = get_instagram_page_keyword()
            page_url = "http://www.instagram.com/" + keyword + "/"

            # If the keyword is not found, stop the process
            if keyword == "keyword not found":
                report = Lines.general_lines("search fail") % "instagram id"
                line_bot_api.push_message(address, TextSendMessage(text=report))
                cont = False

            # If full version link is available, try to get raw data
            if cont:
                send_header()
                json_rawdata = get_insta_raw_data(page_url)

                # If the data is unavailable, stop the process
                if json_rawdata is None:
                    report = Lines.general_lines("failed to open page") % str(keyword + "'s instagram")
                    line_bot_api.push_message(address, TextSendMessage(text=report))
                    cont = False

            # If the raw data is available, crawl user information and check if it's private or not
            if cont:
                # Get and send insta page user information
                insta_fullname, insta_username, insta_biography, insta_follower, insta_following, insta_private = get_insta_user_data(json_rawdata)
                send_insta_user_info(insta_fullname, insta_username, insta_biography, insta_follower, insta_following)

                if insta_private:
                    report = Lines.stalk_instagram("private")
                    line_bot_api.push_message(address, TextSendMessage(text=report))
                    cont = False

            # If it's not private, crawl top 5 pic and send it
            if cont:
                # Get and send insta page user media
                insta_image_link_list, insta_image_caption_list, insta_image_like_list = get_insta_media_data(json_rawdata)
                send_insta_user_pic(insta_image_link_list, insta_image_caption_list, insta_image_like_list)

        except Exception as exception_detail:
            function_name = "Stalk Instagram"
            OtherUtil.random_error(function_name=function_name, exception_detail=exception_detail)

  def daftarBerita(self):
        page = urllib.request.urlopen(self.link)
        soup = BeautifulSoup(page, "html.parser")
        artikel = soup.find_all("div", class_="article__title")
        dataList={}
        counter =0
        for element in artikel:
            dataList[counter] = {}
            dataList[counter]["judul"] = element.a.get_text()
            dataList[counter]["link"] = element.a["href"]
            counter = counter +1
        beritanotVideo = [data for data,info in dataList.items() if not info['judul'].lower().startswith(("video", "vlog")) if not 'galeri' in info['link']]
        dataListBaru = {}
        for x in beritanotVideo:
            dataListBaru[x] ={}
            dataListBaru[x]["judul"] = dataList[x]["judul"] 
            dataListBaru[x]["link"] = dataList[x]["link"]
        
        return dataListBaru
        
  def rangkumanBerita(self):
        stopwords = open('id.stopwords.02.01.2016.txt','r').read().split('\n')
        halamanBerita = urllib.request.urlopen(self.link)
        soup = BeautifulSoup(halamanBerita, "html.parser")
        isi = soup.find("h3", class_="read__content")
        if(len(isi)<2):
            return ""
        isi = isi.find_all("p")
        
        isiParagraf=[]
        for paragraf in isi:
            teks = paragraf.get_text()
            isiParagraf.append(teks)
        isiParagraf = [x for x in isiParagraf if not x.startswith('Baca')]
        
        satuParagraf=[]
        for data in isiParagraf:
            isi = re.split(r'\. +', data)
            isi =[x for x in isi if not x=='']
            satuParagraf.extend(isi)
        
        globaldatakata={}
        datakataperkal ={}
        counterkal =0
        for kalimat in satuParagraf:
            hapuskurung = re.sub(r'([^A-Za-z0-9-\/\.]+)', ' ', kalimat)
            hapustitiktypo = re.sub(r'\s\.\s', ' ', hapuskurung)
            hapustitikawaldanakhir = re.sub(r'(\.\s)|(\.$)', ' ', hapustitiktypo)
            tokenisasi = re.split(r'\s+', hapustitikawaldanakhir)
            token =[x for x in tokenisasi if not x=='']
            # stemmer
            token =[stemmer.stem(x) for x in token]
            datakataperkal[counterkal]={}
            #kata unik
            for kata in token:
                if not kata in stopwords:
                    datakataperkal[counterkal][kata]=0
                    if not kata in globaldatakata.keys():
                        globaldatakata[kata]=0

            for kataunik in datakataperkal[counterkal]:
                for kata in token:
                    if(kataunik==kata):
                        datakataperkal[counterkal][kata] = datakataperkal[counterkal][kata] + 1
                        globaldatakata[kata]= globaldatakata[kata] + 1

            counterkal = counterkal +1
            
        score = {}
        for kal in datakataperkal:
            score[kal] =0
            for kata in globaldatakata.keys():
                for katakal in datakataperkal[kal].keys():
                    if(kata == katakal):
                        tf = 1 + np.log10(datakataperkal[kal][katakal])
                        idf = np.log10(len(globaldatakata)/globaldatakata[kata])
                        bobot = tf * idf
                        score[kal] = score[kal] + bobot
        
        urutbesarkecil = list(sorted(score, key=score.__getitem__, reverse=True))
        batas =0
        dataRangkuman=[]
        for x in urutbesarkecil:
            dataRangkuman.append(x)
            batas = batas+1
            if(batas >= len(datakataperkal)/2):
                break
        rangkuman =np.sort(dataRangkuman) 
        hasil =[]
        for index in rangkuman:
            hasil.append(satuParagraf[index])
        return hasil

  def sendImageWithURL(self, to_, url):
        """Send a image with given image url
        :param url: image url to send
        """
        path = 'pythonLine.data'
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
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

  def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
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
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

  def sendVideo(self, to_, path):
        M = Message(to=to_,contentType = 2)
        M.contentMetadata = {
              'VIDLEN' : '0',
              'DURATION' : '0'
        }
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

  def sendVideoWithURL(self, to_, url):
        path = 'pythonLines.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
               shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise e

  def removeAllMessages(self, lastMessageId):
	      return self.Talk.client.removeAllMessages(0, lastMessageId)

  def sendEvent(self, messageObject):
        return self._client.sendEvent(0, messageObject)

  def sendChatChecked(self, mid, lastMessageId):
        return self.Talk.client.sendChatChecked(0, mid, lastMessageId)

  def getMessageBoxCompactWrapUp(self, mid):
        return self.Talk.client.getMessageBoxCompactWrapUp(mid)

  def getMessageBoxCompactWrapUpList(self, start, messageBox):
        return self.Talk.client.getMessageBoxCompactWrapUpList(start, messageBox)

  def getRecentMessages(self, messageBox, count):
        return self.Talk.client.getRecentMessages(messageBox.id, count)

  def getMessageBox(self, channelId, messageboxId, lastMessagesCount):
        return self.Talk.client.getMessageBox(channelId, messageboxId, lastMessagesCount)

  def getMessageBoxList(self, channelId, lastMessagesCount):
        return self.Talk.client.getMessageBoxList(channelId, lastMessagesCount)

  def getMessageBoxListByStatus(self, channelId, lastMessagesCount, status):
        return self.Talk.client.getMessageBoxListByStatus(channelId, lastMessagesCount, status)

  def getMessageBoxWrapUp(self, mid):
        return self.Talk.client.getMessageBoxWrapUp(mid)

  def getMessageBoxWrapUpList(self, start, messageBoxCount):
        return self.Talk.client.getMessageBoxWrapUpList(start, messageBoxCount)

  def getCover(self,mid):
        h = self.getHome(mid)
        objId = h["result"]["homeInfo"]["objectId"]
        return "http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + mid+ "&oid=" + objId

  """Contact"""


  def blockContact(self, mid):
        return self.Talk.client.blockContact(0, mid)


  def unblockContact(self, mid):
        return self.Talk.client.unblockContact(0, mid)


  def findAndAddContactsByMid(self, mid):
        return self.Talk.client.findAndAddContactsByMid(0, mid)


  def findAndAddContactsByMids(self, midlist):
        for i in midlist:
            self.Talk.client.findAndAddContactsByMid(0, i)

  def findAndAddContactsByUserid(self, userid):
        return self.Talk.client.findAndAddContactsByUserid(0, userid)

  def findContactsByUserid(self, userid):
        return self.Talk.client.findContactByUserid(userid)

  def findContactByTicket(self, ticketId):
        return self.Talk.client.findContactByUserTicket(ticketId)

  def getAllContactIds(self):
        return self.Talk.client.getAllContactIds()

  def getBlockedContactIds(self):
        return self.Talk.client.getBlockedContactIds()

  def getContact(self, mid):
        return self.Talk.client.getContact(mid)

  def getContacts(self, midlist):
        return self.Talk.client.getContacts(midlist)

  def getFavoriteMids(self):
        return self.Talk.client.getFavoriteMids()

  def getHiddenContactMids(self):
        return self.Talk.client.getHiddenContactMids()


  """Group"""

  def findGroupByTicket(self, ticketId):
        return self.Talk.client.findGroupByTicket(ticketId)

  def acceptGroupInvitation(self, groupId):
        return self.Talk.client.acceptGroupInvitation(0, groupId)

  def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.Talk.client.acceptGroupInvitationByTicket(0, groupId, ticketId)

  def cancelGroupInvitation(self, groupId, contactIds):
        return self.Talk.client.cancelGroupInvitation(0, groupId, contactIds)

  def createGroup(self, name, midlist):
        return self.Talk.client.createGroup(0, name, midlist)

  def getGroup(self, groupId):
        return self.Talk.client.getGroup(groupId)

  def getGroups(self, groupIds):
        return self.Talk.client.getGroups(groupIds)

  def getGroupIdsInvited(self):
        return self.Talk.client.getGroupIdsInvited()

  def getGroupIdsJoined(self):
        return self.Talk.client.getGroupIdsJoined()

  def inviteIntoGroup(self, groupId, midlist):
        return self.Talk.client.inviteIntoGroup(0, groupId, midlist)

  def kickoutFromGroup(self, groupId, midlist):
        return self.Talk.client.kickoutFromGroup(0, groupId, midlist)

  def leaveGroup(self, groupId):
        return self.Talk.client.leaveGroup(0, groupId)

  def rejectGroupInvitation(self, groupId):
        return self.Talk.client.rejectGroupInvitation(0, groupId)

  def reissueGroupTicket(self, groupId):
        return self.Talk.client.reissueGroupTicket(groupId)

  def updateGroup(self, groupObject):
        return self.Talk.client.updateGroup(0, groupObject)
  def findGroupByTicket(self,ticketId):
        return self.Talk.client.findGroupByTicket(0,ticketId)

  """Room"""

  def createRoom(self, midlist):
    return self.Talk.client.createRoom(0, midlist)

  def getRoom(self, roomId):
    return self.Talk.client.getRoom(roomId)

  def inviteIntoRoom(self, roomId, midlist):
    return self.Talk.client.inviteIntoRoom(0, roomId, midlist)

  def leaveRoom(self, roomId):
    return self.Talk.client.leaveRoom(0, roomId)

  """TIMELINE"""

  def new_post(self, text):
    return self.channel.new_post(text)

  def like(self, mid, postid, likeType=1001):
    return self.channel.like(mid, postid, likeType)

  def comment(self, mid, postid, text):
    return self.channel.comment(mid, postid, text)

  def activity(self, limit=20):
    return self.channel.activity(limit)

  def getAlbum(self, gid):

      return self.channel.getAlbum(gid)
  def changeAlbumName(self, gid, name, albumId):
      return self.channel.changeAlbumName(gid, name, albumId)

  def deleteAlbum(self, gid, albumId):
      return self.channel.deleteAlbum(gid,albumId)

  def getNote(self,gid, commentLimit, likeLimit):
      return self.channel.getNote(gid, commentLimit, likeLimit)

  def getDetail(self,mid):
      return self.channel.getDetail(mid)

  def getHome(self,mid):
      return self.channel.getHome(mid)

  def createAlbum(self, gid, name):
      return self.channel.createAlbum(gid,name)

  def createAlbum2(self, gid, name, path):
      return self.channel.createAlbum(gid, name, path, oid)


  def __validate(self, mail, passwd, cert, token, qr):
    if mail is not None and passwd is not None and cert is None:
      return 1
    elif mail is not None and passwd is not None and cert is not None:
      return 2
    elif token is not None:
      return 3
    elif qr is True:
      return 4
    else:
      return 5

  def loginResult(self, callback=None):
    if callback is None:
      callback = def_callback

      prof = self.getProfile()

      print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      print("╠➣ Mid Kamu -> " + prof.mid)
      print("╠➣ Nama Akun -> " + prof.displayName)
      print("╠➣ AuthToken Kamu -> " + self.authToken)
      print("╠➣ Cert Kamu -> " + self.cert if self.cert is not None else "")
      