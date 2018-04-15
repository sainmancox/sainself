from humanfriendly import format_timespan, format_size, format_number, format_length
import requests, urllib, urllib.parse

msg = op.message
text = msg.text
msg_id = msg.id
receiver = msg.to
sender = msg._from

def sendMentionV2(to, text="", mids=[]):
	arrData = ""
	arr = []
	mention = "@zeroxyuuki "
	if mids == []:
		raise Exception("Invalid mids")
	if "@!" in text:
		if text.count("@!") != len(mids):
			raise Exception("Invalid mids")
		texts = text.split("@!")
		textx = ""
		for mid in mids:
			textx += str(texts[mids.index(mid)])
			slen = len(textx)
			elen = len(textx) + 15
			arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
			arr.append(arrData)
			textx += mention
		textx += str(texts[len(mids)])
	else:
		textx = ""
		slen = len(textx)
		elen = len(textx) + 15
		arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
		arr.append(arrData)
		textx += mention + str(text)
	alin.sendMessage(msg.to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	
	
					elif msg.text.lower().startswith("searchfilm"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/film.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "[ Result Film ]"
								anu += "\nTitle : {}".format(str(data["Title"]))
								anu += "\nYear : {}".format(str(data["Year"]))
								anu += "\nRated : {}".format(str(data["Rated"]))
								anu += "\nReleased : {}".format(str(data["Released"]))
								anu += "\nDuration : {}".format(str(data["Runtime"]))
								anu += "\nGenre : {}".format(str(data["Genre"]))
								path = str(data["Poster"])
								alin.sendImageWithURL(msg.to, str(path))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,hasil pencarin tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower() == "quotes":
						try:
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/quotes.php?apikey={}".format(str(apiKey)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								alin.sendMessage(msg.to, str(data["result"]))
							else:
								sendMentionV2(msg.to, "Maaf @!,terjadi error yang tidak diketahui", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("randomnumber"):
						try:
							sep = msg.text.split(" ")
							query = msg.text.replace(sep[0] + " ","")
							cond = query.split("-")
							no = cond[0]
							nos = cond[1]
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/random.php?apikey={}&min={}&max={}".format(str(apiKey), no, nos))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "Hasil Random Number : [ {} ]".format(str(data["url"]))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,terjadi error yang tidak diketahui", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("searchimage"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/gambarg.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								path = str(data["url"])
								alin.sendImageWithURL(msg.to, str(path))
							else:
								sendMentionV2(msg.to, "Maaf @!,hasil pencarian tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("cuaca"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/cuaca.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "Lokasi : {}".format(str(data["respon"]["tempat"]))
								anu += "\nCuaca : {}".format(str(data["respon"]["cuaca"]))
								anu += "\nStatus : {}".format(str(data["respon"]["deskripsi"]))
								anu += "\nSuhu : {}".format(str(data["respon"]["suhu"]))
								anu += "\nKelembapan : {}".format(str(data["respon"]["kelembapan"]))
								anu += "\nKecepatan Angin : {}".format(str(data["respon"]["angin"]))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,lokasi tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("jadwalshalat"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/shalat.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "Subuh : {}".format(str(data["respon"]["shubuh"]))
								anu += "\nDzuhur : {}".format(str(data["respon"]["dzuhur"]))
								anu += "\nAshar : {}".format(str(data["respon"]["ashar"]))
								anu += "\nMaghrib : {}".format(str(data["respon"]["maghrib"]))
								anu += "\nIsya : {}".format(str(data["respon"]["isya"]))
								path = str(data["peta_gambar"])
								alin.sendImageWithURL(msg.to, str(path))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,lokasi tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("searchmusic"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/joox.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "[ Result Music ]"
								anu += "\nTitle : {}".format(str(data["info"]["judul"]))
								anu += "\nArtist : {}".format(str(data["info"]["penyanyi"]))
								anu += "\nAlbum : {}".format(str(data["info"]["album"]))
								anu += "\nURL : {}".format(str(data["audio"]["mp3"]))
								anu += "\n\n{}".format(str(data["lirik"]))
								alin.sendImageWithURL(msg.to, str(data["gambar"]))
								alin.sendMessage(msg.to, str(anu))
								alin.sendAudioWithURL(msg.to, str(data["audio"]["mp3"]))
							else:
								sendMentionV2(msg.to, "Maaf @!,hasil pencarian tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("searchquran"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							cond = search.split("|")
							ayat1 = cond[0]
							ayat2 = cond[1]
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/alquran.php?apikey={}&id={}&from={}&to={}".format(str(apiKey), str(search), ayat1, ayat2))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "\nNama Surat : {}".format(str(data["nama_surat"]))
								anu += "\nArti Surat : {}".format(str(data["arti_surat"]))
								for ayat in data["ayat"]:
									anu += "\n{}".format(str(ayat))
								for arti in data["arti"]:
									anu += "\nTerjemahan :"
									anu += "\n{}".format(str(arti))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,terjadi error yang tidak diketahui", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("fs"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/fs.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								path = str(data["url"])
								alin.sendImageWithURL(msg.to, str(path))
							else:
								sendMentionV2(msg.to, "Maaf @!,terjadi error yang tidak diketahui", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("tts"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/tts.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								path = str(data["result"])
								alin.sendAudioWithURL(msg.to, str(path))
							else:
								sendMentionV2(msg.to, "Maaf @!,terjadi error yang tidak diketahui", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("instapost"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/ig_post.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								anu = "[ Instagram Post ]"
								anu += "\nLike : {}".format(str(data["like"]))
								anu += "\nComment : {}".format(str(len(data["comment"])))
								anu += "\nCaption : {}".format(str(data["caption"]))
								alin.sendMessage(msg.to, str(anu))
							else:
								sendMentionV2(msg.to, "Maaf @!,url tidak valid", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("instastory"):
						try:
							sep = msg.text.split(" ")
							search = msg.text.replace(sep[0] + " ","")
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/ig_story.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if data["status"] == "success":
								for picture in data["pict_url"]:
									alin.sendImageWithURL(msg.to, str(picture))
								for video in data["video_url"]:
									alin.sendVideoWithURL(msg.to, str(video))
							else:
								sendMentionV2(msg.to, "Maaf @!,username tidak ditemukan atau akun private", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))
					elif msg.text.lower().startswith("searchyoutube"):
						try:
							sep = msg.text.split(" ")
							query = msg.text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
							api = requests.get("https://farzain.xyz/api/yt_search.php?apikey={}&id={}".format(str(apiKey), str(search)))
							data = api.text
							data = json.loads(data)
							if len(cond) == 1:
								if data["status"] == "success":
									no = 0
									anu = "[ Result Youtube ]"
									for youtube in data["respons"]:
										no += 1
										anu += "\n{}. {}".format(str(no), str(youtube["title"]))
									anu += "\n[ Total Result {} Youtube ]".format(str(len(data["respons"])))
									anu += "\n\nUntuk melihat details download,silahkan gunakan command Searchyoutube {}|List nomor".format(str(search))
									alin.sendMessage(msg.to, str(anu))
								else:
									sendMentionV2(msg.to, "Maaf @!,hasil pencarin tidak ditemukan", [sender])
							elif len(cond) == 2:
								num = int(str(cond[1]))
								if num <= len(data["respons"]):
									vid = data["respons"][num - 1]
									api = requests.get("https://farzain.xyz/api/yt_download.php?apikey={}&id={}".format(str(apiKey), str(vid["video_id"])))
									data = api.text
									data = json.loads(data)
									if data != []:
										no = 0
										anu = "[ {} ]".format(str(data["title"]))
										for download in data["respons"]:
											no += 1
											anu += "\n{}. Type : {}".format(str(no), str(download["type"]))
											anu += "\n    Size : {}".format(str(download["size"]))
											anu += "\n    URL : {}".format(str(download["url"]))
										alin.sendMessage(msg.to, str(anu))
									else:
										sendMentionV2(msg.to, "Maaf @!,hasil download tidak ditemukan", [sender])
						except Exception as error:
							alin.sendMessage(msg.to, str(error))