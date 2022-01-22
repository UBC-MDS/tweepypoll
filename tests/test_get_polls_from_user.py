from pytest import raises
from tweepypoll.tweepypoll import get_polls_from_user

def test_get_polls_from_user():
    """
    Test existing functionalities of get_polls_from_user()
    6 tests in total.
    """
    result = get_polls_from_user('PollzOnTwitta')

    # test output type
    assert type(result) == list

    # test output size (for an existing user)
    assert len(result) >= 0
    assert len(result) <= 100

    # test tweet_num argument, default = 10
    n = 20
    result = get_polls_from_user('PollzOnTwitta', tweet_num=n)
    assert len(result) <= n  