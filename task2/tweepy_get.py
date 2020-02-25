import tweepy
import re
from PIL import Image, ImageDraw, ImageFont
import os
import configparser
import json

def tweepy_get(keyword):
	config = configparser.ConfigParser()
	file = 'keys'
	if os.path.exists(file) :
		config.read(file)
		auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
		auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())  
		api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

		search_results = api.user_timeline(keyword)
		with open("data.json","w") as f:
			json.dump(search_results,f)
	else :
		with open('data.json', 'r') as f:
			search_results = json.load(f)

	num = 0
	highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
	for tweet in search_results:
		gap = '\n'
		for key, value in tweet.items():
			if key == 'text':
				tweet_list = list(value)
		list_num = 0
		for i in range(len(tweet_list)):
			if (i % 45) == 0:
				tweet_list.insert(i,gap)
		# tweet_list.insert(55, gap)
		tweet = ''.join(tweet_list)
		print(tweet)

		num += 1
		text_noem = highpoints.sub('--emoji--', tweet)
		text_noem = text_noem.encode('utf8')

		fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
		image = Image.open('origin.png')
		draw = ImageDraw.Draw(image)
		draw.text((100,200), tweet, font=fnt, fill= "white")
		filename = "img/" + keyword + str(num) + ".png"
		image.save(filename)


# tweepy_get('BostonDynamics')
# a = os.path.exists('img/BostonDynamics1.png')
# print(a)




