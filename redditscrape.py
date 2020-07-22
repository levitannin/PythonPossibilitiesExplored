# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:48:51 2020

@author: Levitannin

Using a Web API to get data: 
    Three things to consider when using a web-based API
    
    Authorization methods:      allows data provider to know who is collecting
                                    their data.  Personal accounts often enough.
    Rate limiting:              applied to data collection, particularly free 
                                    services.  Some API providers have commercial
                                    plans for larger call needs.
    API Endpoints:              Web-based APIs will follow a RESTful interface
                                    (Representational State Transfer), which uses
                                    the same actions of HTTP: GET, POST, and DELETE.
"""

import requests 
from time import sleep
import os
import hashlib
from interuptingcow import timeout
from lxml import etree
from lxml.html import parse

CLIENT_ID = "Given ID by Reddit"
CLIENT_SECRET = "Given Secret by Reddit"

USER_AGENT = "python:cti gathering (by /u/levitannin)"

USERNAME = "levitannin"
PASSWORD = None

def login(USERNAME, PASSWORD):
    if PASSWORD is None:
        PASSWORD = getpass.getpass("Enter reddit password for user {}: ".format(USERNAME))
    
    headers = {"User-Agent": USER_AGENT}
    client_auth = requests.auth.HTTPBasicsAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": USERNAME, "password": PASSWORD}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    return response.json()

def get_links(subreddit, token, n_pages=2):
    stories = []
    
    #   The following is the 'cursor' or navitagor for changing pages.
    after = None
    for page_number in range(n_pages):
        headers = {"Authorization": "bearer {}".format(token['access_token']),
            "User-Agent": USER_AGENT}
        url = "https://oauth.reddit.com/r/{}?limit=100".format(subreddit)
        
        if after:
            url += "&after={}".format(after)
        
        response = requests.get(url, headers=headers)
        result = response.json()
        
        after = result['data']['after']
        
        sleep(2)
        
        stories.extend([(story['data']['title'], story['data']['url'], story['data']['score'])
                       for story in result['data']['children']])
    
    return stories

def reddit_dive():
    token = login(USERNAME, PASSWORD)
    
    stories = get_links("worldnews", token)
    
    #   Following designed for linux architecture more than windows.
    data = os.path.join(os.path.expanduser("~/workspace"), "Data", "websites", "raw")
    
    errorCount = 0
    
    for title, url, score in stories:
        output_filename = hashlib.md5(url.encode().hexdigest())
        fullpath = os.path.join(data, output_filename + ".txt")
        
        #   If there is an error with the website, just skip it.
        try:
            with timeout(5, exception = RuntimeError):
                response = requests.get(url)
                sleep(2)
                data = response.text
                with open(fullpath, 'w') as outf:
                    outf.write(data)
        except (Exception, RuntimeError) as e:
            errorCount += 1
            print(e)
            #   Can call raise instead, to see what the error is and debug the problem
    parse(data)
    
def parse(data):
    #   This is redundant and will be updated once this program is re-written.
    filenames = [os.path.join(data, filename)
             for filename in os.listdir(data)]
    text_output_folder = os.path.join(os.path.expanduser("~/workspace"), "Data",
                                  "websites", "textonly")
    
    skip_node_types = ["script", "head", "style", etree.Comment]
    
def get_text_from_file(filename):
    with open(filename) as inf:
        html_tree = parse(inf)
    return get_text_from_node(html_tree.getroot())

def get_text_from_node(node):
    if len(node) == 0:
        # No children, just return text from this item
        if node.text and len(node.text) > 100:
            return node.text
        else:
            return ""
    
    results = (get_text_from_node(child) for child in node
                     if child.tag not in skip_node_types)
    return "\n".join(r for r in results if len(r) > 1)

if __name__ == '__main__':
    reddit_dive()

    '''#   The API endpoint call to /r/<subredditname> automatically begins gathering
    #   "HOT" posts.
    subreddit = "worldnews"
    url = "https://oauth.reddit.com/r/{}".format(subreddit)
    
    #   Headers set for two reasons:
    #       Use the auth token recieved earlier
    #       set the user agent to stop requests from being heavily restricted.
    headers = {"Authorization": "bearer {}".format(token['access_token']),
               "User-Agent": USER_AGENT}
    response = requests.get(url, headers = headers)
    
    result = response.json()
    for story in result['data']['children']:
        print(story['data']['title'])'''
