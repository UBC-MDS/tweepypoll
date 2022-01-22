# author: Rada Rudyak, Wenxin Xiang, Linh Giang Nguyen
# date: 2022-01-14

import altair as alt
import pandas as pd
import numpy as np
import tweepy
import os
import re

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
    print("Test")
        # Twitter API credentials
    try:
        consumer_key = os.environ.get('TWITTER_CONS_KEY')
        consumer_secret = os.environ.get('TWITTER_CONS_SEC')
        access_key = os.environ.get('TWITTER_ACCS_KEY')
        access_secret = os.environ.get('TWITTER_ACCS_SEC')
    except KeyError:
        raise Exception('Need authentication tokens! Please make sure you have those as environment variables.')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

def get_polls_from_user(username, num=5):
    '''
    Get list of poll ids for a given Twitter user
    Parameters
    ----------
    username : str
        username of the twitter user
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
    
    # check argument validity
    if not(isinstance(username, str)):
        raise TypeError('Invalid argument type: username must be a string.')
    elif not(isinstance(num, int)):
        raise TypeError('Invalid argument: input n_tweets must be >= 0.')

    # Twitter API credentials
    try:
        consumer_key = '4tuMyUqRb6oTR99QSqp32KR3V'
        consumer_secret = 'O4GgyHAMsIE70YxbUBQ0pizV4gnL8JVek8Jy2LeYK4h908bUX2'
        access_key = '1483563822497492993-8NIPFIRy0AlHdn35iBrCUcg5EW56nU'
        access_secret = '9o3Tgy7sUt2mEa37wTKnUSj8xBC7TRUYtX8RCq4R9FFOX'
    except KeyError:
        raise Exception('Need authentication tokens! Please make sure you have those as environment variables.')

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    Client = tweepy.Client(auth)
    #auth.set_access_token(access_key, access_secret)
    #Client = tweepy.Client(consumer_key, consumer_secret)

    # get first batch of tweets
    tweets = []
    latest = Client.get_users_tweets(id=username)
    tweets.extend(latest)
        
    # request recursively to get all tweets
    oldest = latest[-1].id
    while(len(latest) > 0 and len(tweets) < num):
        latest = Client.get_users_tweets(id=username,
                                   max_results=10)
        tweets.extend(latest)
        
        oldest = latest[-1].id # TODO: error out sometimes
        
    # format output dataframe   
    # output = pd.DataFrame([[tweet.created_at, tweet.text] for tweet in tweets],
    #                      columns=['time', 'tweet'])
    # output = output[:num]
    output = tweets

    return output


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