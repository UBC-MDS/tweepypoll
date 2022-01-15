# author: Rada Rudyak, Wenxin Xiang, Linh Giang Nguyen
# date: 2022-01-14

import altair as alt

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

def get_polls_from_user(user_id, num=5):
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