from tweepypoll import tweepypoll
import pandas as pd
import altair as alt

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


def test_visualize_poll():
    """Test visualize_poll on a dictionary input"""

    # test settings on altair plot
    assert isinstance(
        test_plot, alt.Chart
    ), "The type of the argument 'poll_obj' mush be a dictionary"
    assert (
        test_plot.encoding.x.field == "votes"
    ), "x_axis should be mapped to the x axis"
    assert (
        test_plot.encoding.y.field == "label"
    ), "y_axis should be mapped to the y axis"
    assert test_plot.mark == "bar", "mark should be a bar"

    # unit test for chart plot
    df = pd.DataFrame({"label": ["Cat", "Dog", "Guinea pig"], "votes": [156, 256, 56]})
    expected = (
        alt.Chart(
            df, title=alt.TitleParams(text="What's your favorate pet?", anchor="start")
        )
        .mark_bar()
        .encode(
            alt.Y("label", title=""),
            alt.X("votes", title="Votes"),
            alt.Color("label", title="Options"),
            alt.Tooltip("votes"),
        )
        .configure_axis(
            labelFontSize=15,
            titleFontSize=15,
        )
        .configure_title(fontSize=20)
        .properties(height=200, width=400)
    )
    assert test_plot == expected, "Bar chart plot incorrectly!"
