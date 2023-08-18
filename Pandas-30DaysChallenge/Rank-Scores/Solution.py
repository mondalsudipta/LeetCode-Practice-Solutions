# solution 1

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores_sorted = scores.sort_values(by="score", ascending=False)
    scores_sorted["rank"] = scores_sorted["score"].rank(ascending=False, method="dense")

    return scores_sorted[["score", "rank"]]


# solution 2 

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores["rank"] = scores["score"].rank(ascending=False, method="dense")
    scores_sorted = scores.sort_values(by="rank").reset_index(drop=True)

    return scores_sorted[["score", "rank"]]
