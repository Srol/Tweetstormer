import urllib2
import time
import json
import os
import base64
from slacker import Slacker
from twython import Twython

def scrape_storm(tweetID):
	slack = Slacker("Insert Slack bot user token")
	APP_KEY = 'Insert Twitter App Key'
	APP_SECRET = 'Insert Twitter App Secret'
	OAUTH_TOKEN = 'Insert Twitter OAUTH Token'
	OAUTH_TOKEN_SECRET = 'Insert Twitter Token Secret'
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	status = twitter.show_status(id=tweetID)	
	phantomJScloudKey = "insert PhantomJS Cloud Key"		
	up = 1
	channel = "#tweetstormer"
	while status['in_reply_to_status_id_str'] is not None:
		tweetURL = "http://twitter.com/" + status['user']['screen_name'] + "/status/" + status['id_str']
		baseRequest = 'https://phantomjscloud.com/api/browser/v2/' + phantomJScloudKey + "/"
		headers = {'content-type':'application/json'}
		payload = {"pages":[{"url": tweetURL,"renderType": "png","outputAsJson": True,"renderSettings": {"viewport": {"height": 800,"width": 600}}}]}
		req = urllib2.Request(baseRequest, json.dumps(payload), headers)
		response = urllib2.urlopen(req)
		results = json.loads(response.read())
		print '\nresponse status code'
		print response.code
		print '\nresponse headers (pay attention to pjsc-* headers)'
		print response.headers
		with open("content.png", "wb") as responseFile:
			responseFile.write(results['content']['data'].decode('base64'))
		os.rename("content.png", "screenshot" + str(up) +".png")
#		urllib.urlretrieve(baseRequest, "screenshot" + str(up) +".jpg")
		slack.files.upload("screenshot" + str(up) +".png", channels=channel)
		status = twitter.show_status(id=status['in_reply_to_status_id_str'])
		up += 1
		time.sleep(3)
	else:
		tweetURL = "http://twitter.com/" + status['user']['screen_name'] + "/status/" + status['id_str']
		baseRequest = 'https://phantomjscloud.com/api/browser/v2/ak-h84tj-5hfgn-vbcjn-3r88q-rz5tx/'
		headers = {'content-type':'application/json'}
		payload = {"pages":[{"url": tweetURL,"renderType": "png","outputAsJson": True,"renderSettings": {"viewport": {"height": 800,"width": 600}}}]}
		req = urllib2.Request(baseRequest, json.dumps(payload), headers)
		response = urllib2.urlopen(req)
		results = json.loads(response.read())
		print '\nresponse status code'
		print response.code
		print '\nresponse headers (pay attention to pjsc-* headers)'
		print response.headers
		with open("content.png", "wb") as responseFile:
			responseFile.write(results['content']['data'].decode('base64'))
		os.rename("content.png", "lastscreenshot.png")
		slack.files.upload("lastscreenshot.png", channels=channel)
	slack.chat.post_message(channel, "Tweetstorm Over")