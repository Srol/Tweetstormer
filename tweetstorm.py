from slacker import Slacker
from flask import Flask, request, redirect
from rq import Queue
from worker import conn
from utils import scrape_storm

app = Flask(__name__)
slack = Slacker("Insert slack bot user token")
q = Queue(connection=conn)

@app.route('/tweetstorm', methods=['POST'])
def tweetstorm():
	if request.method == "POST" and request.form.get("token") == "Insert Slack slash command key":
		tweetID = request.form.get('text')
		userName = request.form.get("user_name")
		channel = request.form.get('channel_name')
		if tweetID:
			slack.chat.post_message(channel, "@" + userName + " requested a tweetstorm be archived. Screenshots will be posted in #x-bot-tweetstorms.")
			result = q.enqueue(scrape_storm, args=(tweetID,), timeout=600)
			return "Tweetstorm process has been added."
		else:
			return "invalid data provided"
	else:
		return "error"