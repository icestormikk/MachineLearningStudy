import os.path
import random
import re
from typing import Any

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from PIL import Image

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
    sb.scatterplot(x='new_cases', y='new_deaths', data=df)
    plt.show()


def pandas_seaborn_test():
    """
    Функция для визуализации данных в двумерной плоскости
    :return:
    """
    data = [round(random.random() * 10, 2) for i in range(100)]
    years = range(2000, 2100, 1)
    sb.set_style("whitegrid")
    plt.bar(years, data)
    plt.show()


def pandas_seaborn_test_datasets():
    """
    Работа с наборами данных и их визуализация в виде heatmap
    :return:
    """
    data = sb.load_dataset("flights").pivot_table(index='year', columns='month', values='passengers', observed=False,
                                                  margins=True)
    sb.heatmap(data)
    plt.show()


def pandas_seaborn_test_images():
    """
    Функция, в которой я тестировал работу с изображениями
    :return: None
    """
    data = Image.open("./kitten.jpg")
    arr = np.array(data)
    print(arr.shape)
    plt.imshow(data)
    plt.show()


def pandas_seaborn_test_stackoverflow():
    """
    Функция с пробным кодом для работы с результатами опроса среди пользователей портала StackOverflow
    :return: None
    """

    def column_split_by_delimiter(col_series, delimiter=";"):
        result_df = col_series.to_frame()
        variants = []
        for idx, value in col_series[col_series.notnull()].items():
            for option in value.split(delimiter):
                if option not in variants:
                    variants.append(option)
                    result_df[option] = False
                result_df.at[idx, option] = True
        return result_df[variants]

    target_filepath = "data/stackoverflow/survey_results_public.csv"
    if not os.path.isfile(target_filepath):
        get_file_by_url(
            "https://raw.githubusercontent.com/JovianML/opendatasets/master/data/stackoverflow-developer"
            "-survey-2020/survey_results_public.csv",
            target_filepath
        )

    data = pd.read_csv(target_filepath)
    # исправляем NaN значения
    # data['Age1stCode'] = pd.to_numeric(data.Age1stCode, errors='coerce')
    # data['YearsCode'] = pd.to_numeric(data.YearsCode, errors='coerce')
    # data['YearsCodePro'] = pd.to_numeric(data.YearsCodePro, errors='coerce')

    # Убираем "невалидные" значения возраста
    # data.drop(data[data.Age < 10].index, inplace=True)
    # data.drop(data[data.Age > 100].index, inplace=True)

    # Удаление вариантов выбора пола, подразумевающих множественный выбор
    # data.where(~(data['Gender'].str.contains("[;,]+", na=False)), np.nan, inplace=True)

    # Получение 15 записей, у которых в столбце "пол" указано Man
    # smpl = data.sample(15).where(data.Gender.str.contains("Man"))
    # print(smpl[['Respondent', 'Gender']])

    # Получение топ-20 стран с самым большим количеством пользователей и вывод его на экран в виде BarChart
    # top_by_country = data['Country'].value_counts(sort=True).head(20)
    # sb.barplot(x=top_by_country.index, y=top_by_country)
    # plt.xticks(rotation=75)
    # plt.show()

    # Отображение данных по полу в виде PieChart
    # genders = data['Gender'].where(~(data['Gender'].str.contains("[;,]+", na=False))).value_counts()
    # plt.pie(genders, labels=genders.index, autopct="%1.1f%%")
    # plt.show()

    user_devtypes = column_split_by_delimiter(data['DevType'], ";")
    res = pd.DataFrame()
    for devtype in user_devtypes.columns:
        res.add(devtype, data[data['DevType'].str.contains(devtype, na=False) & data['Gender'].str.contains("Woman")]
                .value_counts())
