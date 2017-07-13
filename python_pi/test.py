import webbrowser
import os
from os.path import join, dirname,abspath
import json
import sys
import codecs
import csv
#http://www.tweepy.org/
from bs4 import BeautifulSoup
from selenium import webdriver
import tweepy
from watson_developer_cloud import PersonalityInsightsV2
#Get your Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

personality_insights = PersonalityInsightsV2(
    username='',
    password='',url='')


def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 200

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
    #tweets_for_csv = [[tweet.text.encode("utf-8")] for tweet in tweets]
	#write to a new csv file from the array of tweets
	print("writing to my_tweets.csv".format(username))
	with open("my_tweets.csv.txt".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


if __name__ == '__main__':
    #get_tweets(sys.argv[2])
    filepath=join('./sunburst-chart-master/examples/profiles','personality_analysis.json')
    chartpath=join('./sunburst-chart-master/examples','example_v2.html')
    #print(filepath)
    f=open(filepath,'w+')
    with open(join(dirname(__file__), './my_tweets.csv.txt')) as \
    personality_text:
     json.dump(personality_insights.profile(text=personality_text.read()), f)
    driver = webdriver.Chrome() #I actually used the chromedriver and did not test firefox, but it should work.
    profile_link="https://www.linkedin.com/in/"
    v=sys.argv[1]
    n=profile_link+v
    driver.get('https://www.linkedin.com/')
    elem = driver.find_element_by_name('session_key')
    elem.clear()
    elem.send_keys('') # enter your email id or phone number

    elem = driver.find_element_by_name('session_password')
    elem.clear()
    elem.send_keys('')
    elem.send_keys(u'\ue007')

    driver.get(n)
    html=driver.page_source
    soup=BeautifulSoup(html) #specify parser or it will auto-select for you

    firefox_path=""
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    webbrowser.get('firefox').open_new_tab(chartpath)
    #summary=soup.find('section', { "id" : "experience" })
    #print(summary.getText().encode('utf-8'))
    f.close();
    
    #get tweets for username passed at command line
   
