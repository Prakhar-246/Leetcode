import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if n <= 0 or len(salaries) < n:
        result = None
    else:
        result = salaries.iloc[n - 1]

    return pd.DataFrame({
        f'getNthHighestSalary({n})': [result]
    })