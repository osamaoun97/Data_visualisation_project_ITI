from const import *
import plotly.express as px

df = df.copy(deep=True)


def content_by_year():
    res = df.groupby(["year_added", "type"]).size().reset_index(name="count")
    fig = px.line(
        res,
        x="year_added",
        y="count",
        color="type",
        template='plotly_dark',
        color_discrete_sequence=[MOV_COLOR, "#E50914"],
        labels={"year_added": "Year added", "count": "Count by year", "type": "Type: "},
    )
    fig.update_xaxes(showgrid=False)

    fig.add_annotation(
        x=2020,
        y=1200,
        text="""Sharp drop due to <br>COVID-19""",
        showarrow=True,
        arrowhead=1,
        ax=-120,
        ay=20,
        xshift=-20,
        yshift=20,
        font=dict(size=13),
    )

    fig.update_layout(
        title=dict(text="Content added over the years", font=dict(size=20)),
        paper_bgcolor='rgba(48,48,48,1.000)',
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    return fig
