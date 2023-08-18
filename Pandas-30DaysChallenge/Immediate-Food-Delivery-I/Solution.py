import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    df = delivery
    df = (
        df[df["order_date"] == df["customer_pref_delivery_date"]][
            ["delivery_id"]
        ].count()
    ) / (delivery[["delivery_id"]].count())

    df = round(df * 100, 2)
    df = pd.DataFrame({"immediate_percentage": df})
    return df
