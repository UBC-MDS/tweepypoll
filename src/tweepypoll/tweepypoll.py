# author: Rada Rudyak, Wenxin Xiang, Linh Giang Nguyen
# date: 2022-01-14

import tweepy
import os
import pandas as pd
import altair as alt
import re
import numpy as np

def get_poll_by_id(poll_id):
    '''
    Extracts poll data from Twitter given the poll ID

    Parameters
    ----------
    poll_id : str
        id of the twitter poll
    
    Returns
    --------
    a dictionary with the following keys:
        poll question,
        poll options,
        total responses,
        duration,
        date    
    
    Examples
    --------
    >>> get_poll_by_id('4235234')
    '''

def get_polls_from_user(username, tweet_num = 10):
    '''
    Get list of poll ids for a given Twitter user

    Parameters
    ----------
    username : str
        username of the twitter user
    tweet_num: int
        number of the most recent tweets to be 
        default = 10
        maximum = 100, minimum = 5 per request by Twitter API
        
    Returns
    --------
        array of twitter ids

    Examples
    --------
    >>> get_polls_from_user('PollzOnTwitta')
    
    '''
    
    # Check argument validity
    if not(isinstance(username, str)):
        raise TypeError('Invalid argument type: username must be a string.')
    elif not(isinstance(tweet_num, int) and tweet_num >= 5 and tweet_num <= 100):
        raise TypeError('Invalid argument: input tweet_num must be >= 5 and <= 100.')

    # Twitter API credentials
    from dotenv import load_dotenv
    load_dotenv()
    bearer_token = os.environ.get("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)
    
    # Get user_id from username
    users = client.get_users(usernames=username, user_fields=['id'])

    for user in users.data:  
        user_id = user.id

    # Get tweets specified by the requested user ID
    tweets = client.get_users_tweets(id=user_id, 
                                     max_results=tweet_num,
                                     expansions="attachments.poll_ids")

    # Get poll_ids from tweets if available
    poll_ids = []

    for tweet in tweets.data:
        if "attachments" in tweet.data.keys():
            attachments = tweet.data['attachments']
            poll_id = attachments['poll_ids']
            poll_ids.append(poll_id)
        else:
            pass  
    
    return poll_ids

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
