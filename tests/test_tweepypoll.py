from tweepypoll.tweepypoll import visualize_poll
import pandas as pd
import altair as alt


def test_visualize_poll():
    """Test visualize_poll on a dictionary input"""

    sample_poll_obj = {
        "poll question": "What's your favorate pet?",
        "poll options": [
            {"label": "Cat", "votes": 156},
            {"label": "Dog", "votes": 256},
            {"label": "Guinea pig", "votes": 56},
        ],
        "duration": 1440,
        "date": "2019-11-28T20:26:41.000Z",
    }
    test_plot = visualize_poll(sample_poll_obj)

    # test settings on altair plot
    assert isinstance(
        test_plot, alt.Chart
    ), "The type of the argument 'poll_obj' mush be a dictionary"
    assert (
        test_plot.encoding.x.shorthand == "votes"
    ), "votes should be mapped to the x axis"
    assert (
        test_plot.encoding.y.shorthand == "label"
    ), "label should be mapped to the y axis"
    assert test_plot.mark == "bar", "mark should be a bar"
    assert (
        test_plot.encoding.color.title == "Options"
    ), "Option should be the legend title"

    # check if show_date=True, correct date and time is printed
    assert (
        pd.Timestamp(sample_poll_obj["date"]).strftime("%Y-%m-%d %H:%M:%S")
        == "2019-11-28 20:26:41"
    ), "Date and time is not correct."

    # check if show_duration=True, correct duration is printed
    assert sample_poll_obj["duration"] / 60 == 24.0, "Duration is not correct."

    # check if show_total_responses=True, correct total response is printed
    df = pd.DataFrame(sample_poll_obj["poll options"])
    assert df["votes"].sum() == 468, "Total response is not correct."
