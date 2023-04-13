from const import *
import pandas as pd
import plotly.express as px


df = df.copy(deep=True)


def production_by_country(type_):
    df_production = pd.DataFrame()
    for country in COUNTRIES:
        df_temp = (
            df_copy[df_copy["country"].str.match(country)]
            .groupby(["type"])
            .size()
            .reset_index(name="count")
        )
        df_temp["country"] = country
        df_production = pd.concat([df_production, df_temp])

    df_prod = df_production[df_production["type"] == type_]

    fig = px.choropleth(
        df_prod,
        template='plotly_dark',
        locationmode="country names",
        locations="country",
        color="count",
        hover_name="country",
        hover_data={"type": True, "country": False},
        color_continuous_scale="Greys" if type_ == "Movie" else "redor",
    )

    fig.update_layout(
        title=dict(text=f"Number of {type_}s by country", font=dict(size=20)),
        paper_bgcolor='rgba(48,48,48,1.000)',
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    return fig
