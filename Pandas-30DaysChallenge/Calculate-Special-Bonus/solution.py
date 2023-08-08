import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    df1 = employees[
        (~employees["name"].str.startswith("M")) & (employees["employee_id"] % 2 != 0)
    ][["employee_id", "salary"]]

    df2 = employees[
        (employees["name"].str.startswith("M")) | (employees["employee_id"] % 2 == 0)
    ][["employee_id", "salary"]].assign(salary=0)

    return (
        pd.concat([df1, df2])
        .sort_values("employee_id")
        .rename(columns={"salary": "bonus"})
    )
