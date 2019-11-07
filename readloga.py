#!/usr/bin/python3

import os
from datetime import datetime
class Logline():
	def __init__(self ip, login, passws, date, zone, reqtype, url, httptype, status, size, referer, uagent, timing):
	self.ip =ip
	self.login = login
	self.passws =passws
	self.date = date
	self.zone = zone
	self.reqtype = reqtype
	self.url = url
	self.httptype = httptype
	self.status = status
	self.size =size
	self.referer = referer
	self.uagent = uagent
	self.timig = timing

adict = {}
apath = os.path.expanduser("~/a.log")
print("chemin etedu en ", apath)
with open(apath) as fd:
	for line in fd:
		ip, login, passws, date, zone, reqtype, \
		url, httptype, status, size, referer,\
		uagenttrash = line.split(None, 11)
		#print(ip)
		#print(date)
		#print(date[1:])


		#datetime_object = datetime.strp_time('07/Nov/2019:09:32:42',
		#				     '%d/xb/xY:%H:%M:%S')

		datetime_object = datetime.strptime(date[1:],
							'%d/%b/%Y:%H:%M:%S')

		#print(datetime_object)
		#print(useragenttrash)
		#print(useragenttrash.split('"'))
		#print(useragenttrash.split'"')[1])
		uagent = uagenttrash.split('"')[1]
		timing = uagenttrash.split('"')[2]
		#print(uagent)
		#print(timing.split())
		reqtime = timing.split()[0]
		alogLine = Logline(ip, login, passws, date, zone, reqtype,
				url, httptype, status, size, referer,
				uagent, timing)
		#print(reqtime)
		if ip in adict:
			adict[ip].append(line)
		else:
			adict[ip] = [line]

print(adict["63.143.42.252"][0].uagent)
print(adict["63.143.42.252"][0].date)
print(adict["63.143.42.252"][0].ip)
#print(adict["37.252.227.107"])
