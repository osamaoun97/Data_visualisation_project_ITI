from const import *
import plotly.express as px


df = df.copy(deep=True)


def production_by_month(type_="TV Show"):
    df["month"] = df["date_added"].dt.month
    res = df.groupby(["month", "type"]).size().reset_index(name="count")
    res = res.sort_values(by=["month"], ascending=False)
    res = res.replace({"month": MONTHS})
    ans = res[(res["type"] == type_)]
    if type_ == "TV Show":
        fig = px.bar(
            ans,
            text_auto="2s",
            y="month",
            x="count",
            orientation="h",
            template='plotly_dark',
            color_discrete_sequence=[SHOW_COLOR],
            labels={"month": "Release Month", "count": "Count by Month"},
        )
        fig.update_xaxes(range=[0, 300])
        fig.update_layout(
            title=dict(text="Tv shows Released By Month", font=dict(size=20)),
            paper_bgcolor='rgba(48,48,48,1.000)',
            plot_bgcolor="rgba(40,36,36,1.000)",
        )
    else:
        fig = px.bar(
            ans,
            text_auto="2s",
            y="month",
            x="count",
            orientation="h",
            template='plotly_dark',
            color_discrete_sequence=[MOV_COLOR],
            labels={"month": "Release Month", "count": "Count by Month"},
        )
        fig.update_xaxes(range=[0, 650])
        fig.update_layout(
            title=dict(text="Movies Released By Month", font=dict(size=20)),
            paper_bgcolor='rgba(48,48,48,1.000)',
            plot_bgcolor="rgba(40,36,36,1.000)",
        )
    fig.update_traces(textposition="outside")
    return fig
