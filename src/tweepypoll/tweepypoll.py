# author: Rada Rudyak, Wenxin Xiang, Linh Giang Nguyen
# date: 2022-01-14

import altair as alt
import pandas as pd

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

def visualize_poll(poll_obj, show_duration=False, show_date=False, show_total_responses=False):
    '''
    Returns a simple bar chart of poll responses
    Option to include additional information in the text box

    Parameters
    ----------
    poll_obj : dictionary
        the output of get_poll_by_id() function
    show_duration : bool
        option to display poll duration
        default = False
    show_date : bool
        option to display date
        default = False
    show_total_responses : bool
        option to display total responses in the poll
        default = False

    Returns
    --------
        an altair bar chart for the poll responses
        includes a textbox with additional information if at least one of 
        - show_duration
        - show_date
        was set to True

    Examples
    --------
    >>> visualize_poll('4235234', show_duration=True)

    '''
    # Check for valid inputs
    if not isinstance(poll_obj, dict):
        raise Exception("The type of the argument 'poll_obj' mush be a dictionary")
    
    # convert dictionary to pd.DataFrame
    df = pd.DataFrame(poll_obj["poll options"])
    
    # extract poll date and save as a string of length 1
    if show_date == True: 
        print(f"The end date and time of the poll: {pd.Timestamp(poll_obj['date']).strftime('%Y-%m-%d %H:%M:%S')}") # len()=1
    
    # extract duration and save as a string of length 1
    if show_duration == True:
        print(f"The duration of poll in hours: {poll_obj['duration'] / 60:.1f}h")
    
    # show total responses
    if show_total_responses == True:
        print(f"The total response of the poll: {df['votes'].sum()}")
    
    plot = alt.Chart(
        df, 
        title=alt.TitleParams(
            text=poll_obj['poll question'],
            anchor="start"
        )).mark_bar().encode(
        alt.Y('label', title=''),
        alt.X('votes', title='Votes'),
        alt.Color('label',title='Options'),
        alt.Tooltip('votes')
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=15,
    ).configure_title(fontSize=20
                     ).properties(
        height=200, width=400
    )
    
    return plot
    