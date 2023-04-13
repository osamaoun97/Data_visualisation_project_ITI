from const import *
import plotly.express as px


df = df.copy(deep=True)


def show_longest_by_type(type_):
    if type_ == "TV Show":
        res = (
            df[["title", "season_count"]]
            .sort_values(by="season_count", ascending=False)
            .iloc[:5, :]
        )
        res["season_count"] = res["season_count"].astype(int)
        res = res.sort_values(by="season_count", ascending=True)
        fig = px.bar(
            res,
            text_auto="2s",
            y="title",
            x="season_count",
            orientation="h",
            template='plotly_dark',
            color_discrete_sequence=[SHOW_COLOR],
            labels={"title": "Show Title", "season_count": "Number of seasons"},
        )
        fig.update_traces(textposition="outside")
        fig.update_xaxes(range=[0, 22])
        fig.update_layout(
            title=dict(
                text="The longest TV Shows",
                font=dict(size=20),
            ),
            paper_bgcolor='rgba(48,48,48,1.000)',
            plot_bgcolor="rgba(40,36,36,1.000)",
        )
    else:
        res = (
            df[["title", "movie_duration"]]
            .sort_values(by="movie_duration", ascending=False)
            .iloc[:5, :]
        )
        res["movie_duration"] = res["movie_duration"].astype(int)
        res = res.sort_values(by="movie_duration", ascending=True)
        fig = px.bar(
            res,
            text_auto="2s",
            y="title",
            x="movie_duration",
            orientation="h",
            template='plotly_dark',
            color_discrete_sequence=[MOV_COLOR],
            labels={
                "title": "Movie Title",
                "movie_duration": "Movie Duration by minutes",
            },
        )
        fig.update_traces(textposition="outside")
        fig.update_xaxes(range=[0, 400])
        fig.update_layout(
            title=dict(
                text="The longest Movies",
                font=dict(size=20),
            ),
            paper_bgcolor='rgba(48,48,48,1.000)',
            plot_bgcolor="rgba(40,36,36,1.000)",
        )

    return fig
