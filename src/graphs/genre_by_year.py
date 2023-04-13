from const import *
import plotly.express as px

df = df.copy(deep=True)


def genre_by_year(genre, type_):
    res = (
        df[(df["listed_in"].str.contains(genre)) & (df["type"] == type_)]
        .groupby(["year_added"])
        .size()
        .reset_index(name="count")
    )
    fig = px.line(
        res,
        x="year_added",
        y="count",
        template='plotly_dark',
        color_discrete_sequence=[MOV_COLOR if type_ == "Movie" else "#E50914"],
        labels={
            "year_added": "Year added",
            "count": "Count by year",
        },
    )
    fig.update_xaxes(showgrid=False)
    fig.update_layout(
        title=dict(
            text=f"{genre} {type_}s Trend over the years",
            font=dict(size=20),
        ),
        paper_bgcolor='rgba(48,48,48,1.000)',
        plot_bgcolor="rgba(40,36,36,1.000)",
    )

    return fig
