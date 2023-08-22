import os
from configparser import ConfigParser
import time
import psycopg2
import requests


class Parser:
    """Класс для парсинга hh.ru"""

    def __init__(self, url: str, employer: str):
        self.employer_url = None
        self.url = url
        self.employer = employer

    def get_employers(self):
        """
        Метод для получения списка работодателей с платформы HeadHunter
        """
        employers_lst = []
        for page in range(20):
            params = {'per_page': 100,
                      'page': page,
                      'text': self.employer,
                      'search_field': 'name',
                      'order_by': "publication_time",
                      'archived': False,
                      }
            vacancies = requests.get(self.url, params=params).json()
            employers_lst.extend(vacancies['items'])
            for el in employers_lst:
                if el['name'] == self.employer and el['open_vacancies'] > 10:
                    self.employer_url = el['vacancies_url']
                    return el

    def get_vacancies_url(self):
        return self.employer_url

    def get_vacancies(self):
        """
        Метод для получения списка вакансий определенного работодателя с платформы HeadHunter
        """
        vacancies_lst = []
        for page in range(20):
            params = {'per_page': 100,
                      'page': page,
                      'search_field': 'name',
                      'area': 1,
                      'order_by': "publication_time",
                      'archived': False,
                      }
            vacancies = requests.get(self.employer_url, params=params).json()
            vacancies_lst.extend(vacancies['items'])
            if (vacancies['pages'] - page) <= 1:
                break
            time.sleep(0.5)
        return vacancies_lst


class DBCreator:
    """Класс для создания базы данных, создания и заполнения таблиц"""

    def __init__(self, filename):
        self.filename = filename

    def config(self, section="postgresql"):
        """Метод получает словарь из файла с параметрами для подключения к БД"""
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(
                'Section {0} is not found in the {1} file.'.format(section, self.filename))
        return db

    def db_creator(self):
        pass

    def table_create(self):
        pass


class DBManager:
    """класс для работы с данными в БД."""
    password = os.getenv("PASSQL")

    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password=password
    )

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        pass

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию."""
        pass

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'."""
        pass
