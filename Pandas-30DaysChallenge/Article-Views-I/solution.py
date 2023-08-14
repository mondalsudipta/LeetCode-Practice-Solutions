import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:

    df = views[views["author_id"] == views["viewer_id"]]
    df1 = df.drop_duplicates(subset="author_id")
    result_df = df1.rename(columns={"author_id": "id"})
    return result_df[["id"]].sort_values(by="id")
