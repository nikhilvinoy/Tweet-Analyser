#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:55:27 2020

@author: elkanio
"""
import tweepy
import streamlit as st 
from textblob import TextBlob
import pandas as pd
import numpy as mp


consumerKey = "WAyiRJKZ5FJrcqHRZMaFp13Qb"
consumerSecret = "r3zkYd9sGIfnyq1J9rGL5NTHtzGcX4wg1xkvGtsApqjYxBH2xo"
accessToken  = "243162284-F3CmpGkXKlHJrjNuHKMEWP54n8akeqnrOATdaWcJ"
accessTokenSecret  = "0YHerOKzM9NrOpf9EzuhZkdSsoQZCeYBdRPt0BDYV24a2"


#Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret) 
    
# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret) 
    
# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)



def app():
    st.title("Tweet Analyzer")


	activities=["Tweet Analyzer","Generate Twitter Data"]

	choice = st.sidebar.selectbox("Select Your Activity",activities)

	

	if choice=="Tweet Analyzer":

		st.subheader("Analyze the tweets of your favourite Personalities")

		st.subheader("This tool performs the following tasks :")

		st.write("1. Fetches the 5 most recent tweets from the given twitter handle")
		st.write("2. Generates a Word Cloud")
		st.write("3. Performs Sentiment Analysis a displays it in form of a Bar Graph")


		


		raw_text = st.text_area("Enter the exact twitter handle of the Personality (without @)")



		st.markdown("<--------     Also Do checkout the another cool tool from the sidebar")

		Analyzer_choice = st.selectbox("Select the Activities",  ["Show Recent Tweets","Generate WordCloud" ,"Visualize the Sentiment Analysis"])


		if st.button("Analyze"):

			
			if Analyzer_choice == "Show Recent Tweets":

				st.success("Fetching last 5 Tweets")
                
                def Show_last_tweets(raw_text):
                    posts = api.user_timeline(screen_name=raw_text, count = 10, lang ="en", tweet_mode="extended")
                    
                    
                    def tweets():
                        
                        l = []
                        i = 1
                        for tweet in posts[:5]:
                            l.append(tweet.full_text)
                            i = i+1
                        return l
                    
                   recent_tweets = tweets()
                   return recent_tweets
               
                recent_tweets = Show_last_tweets(raw_text)

