import json
import requests
import psycopg2
import os
import csv
import time

password = os.getenv("PASSQL")

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password=password
)


def get_vacancies(keyword):
    """
    Получение списка вакансий с платформы HeadHunter
    """
    vacancies_lst = []
    for page in range(5):
        params = {'per_page': 100,
                  'page': page,
                  'text': keyword,
                  'search_field': 'name',
                  'order_by': "publication_time",
                  'archived': False,
                  }
        vacancies = requests.get('https://api.hh.ru/vacancies', params=params).json()
        vacancies_lst.extend(vacancies['items'])
        if (vacancies['pages'] - page) <= 1:
            break
        time.sleep(0.5)
    return vacancies_lst


jsonObj = get_vacancies('python')

employers_list = []  # Создаем список с работодателями

for vac in jsonObj:
    employers_list.append(vac['employer']['name'])  # заполняем список работодателями

print(len(employers_list))
employers_list = set(employers_list)  # убираем повторения в списке работодателей

for emp in employers_list:
    print(emp)

print(len(employers_list))
