from tweepypoll.tweepypoll import visualize_poll
import pandas as pd
import altair as alt


def test_visualize_poll():
    """Test visualize_poll on a dictionary input"""

    sample_poll_obj = {
        "text": "Important research!!!",
        "duration": 1440,
        "date": "2022-01-22T04:01:08.000Z",
        "poll options": [
            {"position": 1, "label": "Cookies", "votes": 29},
            {"position": 2, "label": "Cupcakes", "votes": 5},
            {"position": 3, "label": "Donuts", "votes": 24},
            {"position": 4, "label": "Ice Cream", "votes": 25},
        ],
        "user": "GregShahade",
        "total": 83,
    }

    test_plot = visualize_poll(sample_poll_obj)

    # test settings on altair plot
    assert isinstance(
        test_plot, alt.Chart
    ), "The type of the output mush be a altair chart"
    assert (
        test_plot.encoding.x.shorthand == "votes"
    ), "The votes should be mapped to the x axis"
    assert (
        test_plot.encoding.y.shorthand == "label"
    ), "The label should be mapped to the y axis"
    assert test_plot.mark == "bar", "mark should be a bar"
    assert (
        test_plot.encoding.color.title == "Options"
    ), "Option should be the legend title"

    # check if show_user=True, correct user name is printed
    assert (sample_poll_obj["user"] == "GregShahade", "The user name is not correct.")

    # check if show_date=True, correct date and time is printed
    assert (
        pd.Timestamp(sample_poll_obj["date"]).strftime("%Y-%m-%d %H:%M:%S")
        == "2022-01-22 04:01:08"
    ), "Date and time is not correct."

    # check if show_duration=True, correct duration is printed
    assert sample_poll_obj["duration"] / 60 == 24.0, "Duration is not correct."

    # check if show_total_responses=True, correct total response is printed
    df = pd.DataFrame(sample_poll_obj["poll options"])
    assert (
        df["votes"].sum() == sample_poll_obj["total"]
    ), "Total response is not correct."
