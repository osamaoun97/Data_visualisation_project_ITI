import wrangle
from const import *
import plotly.express as px

df = df.copy(deep=True)


def dist_of_length(type_="TV Show"):
    if type_ == "Movie":
        fig = px.histogram(
            df["movie_duration"][
                (df["movie_duration"] != 0) & (df["type"] == type_)
            ].astype(float),
            template="plotly_dark",
            color_discrete_sequence=[MOV_COLOR],
            labels={"value": "Duration by minutes", "count": "Count"},
        )
        fig.add_annotation(
            x=120,
            y=150,
            text="Most movies are between <br> 80 and 120 minutes",
            font=dict(size=15),
            ax=120,
            showarrow=True,
            arrowhead=2,
        )
        fig.update_layout(
            title=dict(text="Distribution of Movies duration", font=dict(size=20)),
            paper_bgcolor="rgba(48,48,48,1.000)",
            plot_bgcolor="rgba(40,36,36,1.000)",
        )

    else:
        fig = px.histogram(
            df["season_count"][
                (df["season_count"] != 0) & (df["type"] == type_)
            ].astype(float),
            color_discrete_sequence=[SHOW_COLOR],
            template="plotly_dark",
            labels={"value": "Number of seasons", "count": "Count"},
        )
        fig.add_annotation(
            x=1.5,
            y=1200,
            text="Most Tv shows are produced <br> for only one season",
            font=dict(size=15),
            ax=120,
            showarrow=True,
            arrowhead=2,
        )
        fig.update_layout(
            title=dict(
                text="Distribution of TV Shows number of seasons", font=dict(size=20)
            )
        )
    fig.update_layout(
        showlegend=False,
        paper_bgcolor="rgba(48,48,48,1.000)",
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    return fig
