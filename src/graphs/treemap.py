from const import *
import plotly.express as px
import pandas as pd
from collections import Counter
import plotly.express as px

df = df.copy(deep=True)


def treemap_graph(type_):
    res = df[df["type"] == type_].copy(deep=True)
    res["listed_in"] = res["listed_in"].replace("Missing", np.nan)
    res = res.dropna(subset=["listed_in"])
    listed_in = list(re.split("\s?,\s?", ", ".join(res["listed_in"].to_list())))
    res = pd.DataFrame(Counter(listed_in).most_common(10), columns=["Genre", "count"])
    res[f"{type_} Genres"] = f"{type_} Genres"
    fig = px.treemap(
        res,
        color="count",
        color_continuous_scale="Greys" if type_ == "Movie" else "OrRd",
        path=[f"{type_} Genres", "Genre"],
        template="plotly_dark",
        values="count",
    )
    fig.update_traces(root_color="lightgrey")
    fig.data[0].textinfo = "label+text+value"
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        title=dict(text=f"Top 10 genres in {type_}s", font=dict(size=20)),
        paper_bgcolor="rgba(48,48,48,1.000)",
        plot_bgcolor="rgba(40,36,36,1.000)",
    )
    return fig
