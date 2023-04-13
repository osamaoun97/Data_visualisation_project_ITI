from const import *

df = df.copy(deep=True)


def fetch_item(type_, title):
    res = df[(df["type"] == type_) & (df["title"] == title)]
    if type == "TV Show":
        return (
            f"Genre: {res['listed_in'].iloc[0]}",
            f"Directors: {res['director'].iloc[0]}",
            f"Country: {res['country'].iloc[0]}",
            f"Date added: {res['date_added'].dt.date.iloc[0]}",
            f"Duration: {res['duration'].iloc[0]}",
            f"Description: {res['description'].iloc[0]}",
        )
    else:
        return (
            f"Genre: {res['listed_in'].iloc[0]}",
            f"Directors: {res['director'].iloc[0]}",
            f"Country: {res['country'].iloc[0]}",
            f"Date added: {res['date_added'].dt.date.iloc[0]}",
            f"Duration: {res['duration'].iloc[0]}",
            f"Description: {res['description'].iloc[0]}",
        )
