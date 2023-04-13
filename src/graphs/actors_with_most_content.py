from const import *
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
from dash_bootstrap_templates import load_figure_template

df = df.copy(deep=True)
load_figure_template("DARKLY")


def actors_with_most_content(country, type_="TV Show"):
    res = df[(df["cast"] != "Missing") & (df["type"] == type_)].copy(deep=True)
    res["from_country"] = res["country"].apply(
        lambda x: 1 if country.lower() in x.lower() else 0
    )
    small = res[res["from_country"] == 1]
    cast = ", ".join(small["cast"].fillna("")).split(", ")
    tags = Counter(cast).most_common(10)
    tags = [tag for tag in tags if "" != tag[0]]
    labels, values = [tag[0] + "  " for tag in tags], [tag[1] for tag in tags]

    if not labels or not values:
        fig = go.Figure(template='plotly_dark')
        fig.add_annotation(
            x=2.5,
            y=1.5,
            text=f"No available actors names for {country}",
            font=dict(size=20),
            showarrow=False,
        )
        fig.update_layout(
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            paper_bgcolor='rgba(48,48,48,1.000)',
            plot_bgcolor="rgba(40,36,36,1.000)",
        )
        return fig

    if type_ == "Movie":
        color = MOV_COLOR
        x_label = "Number of movies"

    else:
        color = SHOW_COLOR
        x_label = "Number of TV shows"
    fig = px.bar(
        y=labels[::-1],
        x=values[::-1],
        text_auto="2s",
        orientation="h",
        template='plotly_dark',
        color_discrete_sequence=[color],
        labels={"y": "Actors", "x": x_label},
    )
    fig.update_layout(
        title=dict(text=f"Top 10 {country} Actors for {type_}s", font=dict(size=20)),
        paper_bgcolor='rgba(48,48,48,1.000)',
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    fig.update_traces(textfont_color="#000000" if type_ == "Movie" else "#ffffff")
    return fig
