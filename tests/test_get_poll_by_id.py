from tweepypoll.tweepypoll import get_poll_by_id
import pytest

def test_get_poll_by_id():
    """Test that function returns a dictionary"""
    rtn = get_poll_by_id([1484375486473986049])[0]
    assert isinstance(
        rtn, dict
    ), "This function must return a dictionary"

    """Test that the 'poll options' in return dict is a list"""
    opts = get_poll_by_id([1484375486473986049])[0]['poll options']
    assert isinstance(
        opts, list
    ), "Poll options is not returning a list"

    """Test that a known poll returns correct total"""
    actual = get_poll_by_id([1484375486473986049])[0]['total']
    expected = 83
    assert actual == expected, "The function is not returning correct total votes"

    """Test that function throws error when the id passed isn't numeric."""
    with pytest.raises(TypeError) as e:
        get_poll_by_id('hello')
    assert str(e.value) == 'Invalid argument type: input tweet_id must be a list of numeric IDs.'

    """Test that function notifies user if tweet does not contain a poll"""
    with pytest.raises(TypeError) as e:
        get_poll_by_id([1482319795408146433])[0]
    assert str(e.value) == 'Provided tweet does not contain a poll!'
