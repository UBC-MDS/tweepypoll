# author: Rada Rudyak, Wenxin Xiang, Linh Giang Nguyen
# date: 2022-01-14

import altair as alt
import pandas as pd
import numpy as np
import tweepy
import os
import re

def get_poll_by_id(tweet_id):
    '''
    Extracts poll data from Twitter given the poll ID

    Parameters
    ----------
    tweet_id : str
        id of the tweet containing twitter poll
    
    Returns
    --------
    a dictionary with the following keys:
        poll question,
        poll responses,
        total votes,
        duration,
        date    
    
    Examples
    --------
    >>> get_poll_by_id('4235234')
    '''

    if not(isinstance(tweet_id, int)):
        raise TypeError('Invalid argument type: poll id must be numeric string.')

   # Twitter API credentials
    from dotenv import load_dotenv
    load_dotenv()
    bearer_token = os.environ.get("BEARER_TOKEN")
    #bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAyIYQEAAAAAjvBdCMMh1dT8clkpXhHxzld7Dhs%3DLPl5zMXXOZqznZGe9JP7zHj3Wzx0N4unogLcWl8wfIkwikjQKm'
    
    client = tweepy.Client(bearer_token=bearer_token)

    res_tweet = client.get_tweets(tweet_id, expansions=["attachments.poll_ids", "author_id"], poll_fields=["duration_minutes","end_datetime"])
    res = res_tweet.includes

    poll = res['polls'][0]
    duration = poll['duration_minutes']
    date = poll['end_datetime']
    options = poll['options']
    text = res_tweet.data[0]['text']
    user = res['users'][0].username

    total = 0
    for opt in options:
        total = total + opt['votes']

    rtn = {
        "text" : text,
        "duration" : duration,
        "date" : date,
        "poll options" : options,
        "user" : user,
        "total" : total
    }

    return rtn

def get_polls_from_user(username, tweet_num=5):
     '''
    Get list of poll ids for a given Twitter user
    Parameters
    ----------
    user_id : str
        id of the twitter user
    num : int
        number of polls to return, in desc chronological order
        default = 5
    Returns
    --------
        array of twitter ids
    Examples
    --------
    >>> get_polls_from_user('ChipotleTweets', 3)
    
    '''


def visualize_poll(poll_obj, show_user=False, show_duration=False, show_date=False):
    '''
    Returns a simple bar chart of poll responses
    Option to include additional information in the text box

    Parameters
    ----------
    poll_obj : dictionary
        the output of get_poll_by_id() function
    show_user : bool
        option to display user handle in the textbox
        default = False
    show_duration : bool
        option to display poll duration in the textbox
        default = False
    show_date : bool
        option to display date in the textbox
        default = False

    Returns
    --------
        an altair bar chart for the poll responses
        includes a textbox with additional information if at least one of 
        - show_user
        - show_duration
        - show_date
        was set to True

    Examples
    --------
    >>> visualize_poll('4235234', show_duration=True)

    '''