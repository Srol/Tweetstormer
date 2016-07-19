# Tweetstormer

This is a bot that collects screenshots from long Twitter threads, such as Tweetstorms. 

Embedding individual tweets from like a 40-tweet sequence can bog down a webpage. This bot collects screenshots instead that can be embedded as images instead.

## How it works.

Find the very last tweet in the series you want to get screenshots of (last meaning most recent and at the end of the chain.) 

Type `/tweetstorm <tweetid>` in Slack, where `<tweetid>` is the number at the end of the URL for a tweet. The bot will then begin downloading screenshots of tweets into `#tweetstormer`, or any other channel you designate in utils.py

## Set-up

1. Clone this repository onto your local computer.
2. Obtain API keys and tokens for the following services and add them to tweetstorm.py and utils.py:
⋅⋅* Twitter
⋅⋅* Slack bot user
⋅⋅* Slack slash command
⋅⋅* phantomjscloud
3. Create a Heroku app and add its URL plus the endpoint "/tweetstorm" to the Slack slash command configuration.
4. Push the repository to Heroku and activate the redis-to-go add-on.
5. Basically it. 

## Caveat Emptor

This only works for tweet sequences that have been properly linked by replying to each other. If tweets are not linked, it will only screenshot the one you provide the ID for and nothing more.

The bot is written in Python, but gets most of what it dones through phantom.js. My original version used selenium's webdriver feature to do this directly inside the bot, but I couldn't match the display font properly. So instead I use a third party service, [phantomjscloud](https://phantomjscloud.com/). If you can figure it out, be my guest. I don't even know javascript and am mostly guessing.