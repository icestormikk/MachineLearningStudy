import os.path
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt

from numpy_pandas.numpy.numpy_functions import get_file_by_url


def read_csv_file(csv_filepath: str) -> Any:
    try:
        return pd.read_csv(csv_filepath)
    except Exception as e:
        print(f"Error while reading: {e}")
        return None


def pandas_test():
    name = 'italy-covid-daywise.csv'
    if not os.path.isfile(f"./{name}"):
        name = 'italy-covid-daywise.csv'
        get_file_by_url(
            "https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw"
            "/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv",
            name
        )

    df = read_csv_file(f"./{name}")
    # выбор n-го количества случайных строк
    print(df.sample(5))
    # суммирование данных в конкретном столбце
    print(df.new_cases.sum())
    # фильтрация данных из набора
    print(df[df.new_tests > 30000])
    # сортировка данных
    print(df.sort_values('date', ascending=False))
    # преобразование данных и группировка
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month
    df['day'] = pd.DatetimeIndex(df['date']).day
    print(df)
    print(df.groupby('year')[['new_cases']].sum())

    # вывод на экран графика с данными
    df['new_deaths'].cumsum().plot(title='Total Deaths')
    plt.show()
