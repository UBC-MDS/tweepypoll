# tweepypoll

## Overview

`tweepypoll` is a Python package that allows users to extract and visualize poll data (poll questions, poll options, poll responses, etc.) from Twitter. Our goal is to make `tweepypoll` helpful and user-friendly; any Python beginner can effectively gain access to the data and make their own data-driven decisions. In particular, it could be a useful package for people doing social media journalism, or those studying social media interactions.

## Functions

- `get_poll_by_id`:
    - This function extracts poll data from Twitter given the poll ID.

- `get_polls_from_user`:
    - This function retrieves a list of poll IDs from a Twitter user. These ids can be fed into the `get_poll_by_id` and `visualize_poll` functions.

- `visualize_poll`:
    - This function takes in the output of `get_poll_by_id` function and visualizes the poll information. 

## Related Packages

There are a few existing Python packages that have similar functionality for tweets from Twitter. For example, `pytweet` is a package that helps extract tweets, visualize user habit on tweet posting, and apply sentiment analysis to the data. However, there are no available packages that work specifically on polls from Twitter. 

## Installation

```bash
$ pip install tweepypoll
```

## Usage

```bash
from tweepypoll.tweepypoll import get_poll_by_id
get_poll_by_id(tweet_id)
```
**tweet_id** is numeric, such as 1481040318325739523


```bash
from tweepypoll.tweepypoll import get_polls_from_user
get_polls_from_user('user_id')
```
where **user_is** is a string username, such as 'tacobell'


```bash
from tweepypoll.tweepypoll import visualize_poll
visualize_poll(poll_obj, show_user=False, show_duration=False, show_date=False)
```
**poll_obj** is a dict outputted by get_poll_by_id(), **show_user, show_duration, show_date** are optional booleans to display username, poll duration and poll end date, respectively

## Contributors

- Wenxin Xiang
- Rada Rudyak
- Linh Giang Nguyen

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`tweepypoll` was created by Wenxin Xiang, Rada Rudyak, Linh Giang Nguyen. It is licensed under the terms of the MIT license.

## Credits

`tweepypoll` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
