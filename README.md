# tweepypoll

## Overview

`tweepypoll` is a Python package that allows users to extract and visualize poll data (poll questions, poll options, poll responses, etc.) from Twitter. Our goal is to make `tweepypoll` helpful and user-friendly; any Python beginner can effectively gain access to the data and make their own data-driven decisions. 

## Functions

- `get_poll_by_id`:
    - This function extracts poll data from Twitter given the poll ID.

- `get_polls_from_user`:
    - This function returns a list of poll IDs from a Twitter user which can be fed into the `get_poll_by_id` function.

- `visualize_poll`:
    - This function takes in the output of `get_poll_by_id` function and visualizes the poll information. 

## Related Packages

There are a few existing Python packages that have similar functionality for tweets from Twitter. For example, `pytweet` is a package that helps extract tweets, visualize user habit on tweet posting, and apply sentiment analysis to the data. However, there are no available packages that work specifically on polls from Twitter. 

## Installation

```bash
$ pip install tweepypoll
```

## Usage

- TODO

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
