import urllib2
import json
import datetime
from abc import ABCMeta
from urllib import urlencode
from abc import abstractmethod
from urlparse import urlunparse
from bs4 import BeautifulSoup
from time import sleep

__author__ = "Jason Brooks"


class TwiiterSearch:

	__metaclass__ = ABCMeta

	def __init__(self, rate_delay, error_delay=5):
		"""
		:param_rate_delay: How long to pause between calls to Twitter
		:param_error_delay: How to pause when an error occurs
		"""
		self.rate_delay = rate_delay
		self.error_delay = error_delay

	def search(self. query):
		"""
		Scrape items from Twitter
		:param_query: Query to search Twitter with. Takes form of queries constructed with using Twitters
		advanced search: https://twitter.com/search-advanced
		"""

	def execute_search(self. url):
		"""
		Executes a search to Twitter for the given URL
		:param url to search Twitter with
		:return: A json object with data from Twitter
		"""

	def parse_tweets(items_html):
		"""
		Parses Tweets from the given HTML
		:param items_html: The html block with tweets
		:return: A JSON list of tweets
		"""

	def construc_url(query, max_position=None):
		"""
		For a given query, will construct a URL to search Twitter with
		:param query: The query term used to search twitter
    :param max_position: The max_position value to select the next pagination of tweets
    :return: A string URL
		"""

	def save_tweets(self, tweets):
		"""
		Abstract method that's called with a list of Tweets
		When implementing this class you do whatever you want with these Tweets.
		"""

class TwitterSearchImp(TwitterSearch):

	def __init__(self, rate_delay, error_delay, max_tweets):
		"""
    :param rate_delay: How long to pause between calls to Twitter
    :param error_delay: How long to pause when an error occurs
    :param max_tweets: Maximum number of tweets to collect for this example
		"""

	def save_tweets(self, tweets):
		"""
		Just prints outs Tweets
		:return:
		"""




















