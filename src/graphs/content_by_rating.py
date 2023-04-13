from const import *
import pandas as pd
import plotly.express as px

df = df.copy(deep=True)


def content_by_rating():
    res = (
        df.groupby(["rating"])
        .size()
        .reset_index(name="count")
        .sort_values("count")
        .copy(deep=True)
    )
    res = res[res["rating"] != "Missing"]

    res["ratings_ages"] = res["rating"].map(RATINGS_AGE)
    res["ratings_ages"] = pd.Categorical(
        res["ratings_ages"], categories=["Kids", "Older Kids", "Teens", "Adults"]
    )
    res = res.sort_values("ratings_ages")

    fig = px.bar(
        res,
        x="rating",
        y="count",
        template='plotly_dark',
        labels={
            "rating": "Maturity Ratings",
            "count": "Count by rating",
            "ratings_ages": "Rating Ages",
        },
        color_discrete_sequence=["#a66968", "#564d4d", "#831010", "#073763"],
        color="ratings_ages",
    )

    fig.add_annotation(
        x=12.5,
        y=2300,
        text="Highest content added <br> was to Adults (18+) followed by <br> Teens (16+)",
        showarrow=True,
        arrowhead=1,
        ax=-150,
        ay=-90,
        font=dict(size=13),
    )

    fig.update_layout(
        title=dict(text="Content added by Maturity Ratings", font=dict(size=20)),
        paper_bgcolor='rgba(48,48,48,1.000)',
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    return fig
