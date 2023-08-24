import os
from configparser import ConfigParser
import time
import psycopg2
import requests
from src.utils import config


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
                    return [el['id'], el['name'], el['open_vacancies'], el['vacancies_url']]

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


class DB:
    """Класс для подключения к базе данных"""

    def __init__(self, db_name: str):
        self.__params = config()
        self.conn = psycopg2.connect(dbname='postgres', **self.__params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.cur.execute(f"CREATE DATABASE {db_name}")
        self.conn.close()
        self.__params.update({'dbname': db_name})
        self.conn = psycopg2.connect(**self.__params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def conn_close(self):
        return self.conn.close()


class DBCreator(DB):
    """Класс для создания и заполнения таблиц"""

    def __init__(self, db_name: str):
        super().__init__(db_name)

    def create_employers_table(self):
        self.cur.execute('''CREATE TABLE employers
                            (
                                company_id int PRIMARY KEY,
                                company_name varchar(100) NOT NULL,
                                open_vacancies int
                            )'''
                         )

    def create_vacancies_table(self):
        self.cur.execute('''CREATE TABLE vacancies
                                    (
                                        vacancy_id int NOT NULL,
                                        company_id int NOT NULL,
                                        title varchar(100),
                                        salary_from int,
                                        salary_to int,
                                        vacancy_url varchar(100),
                                        description varchar(100)
                                    )'''
                         )
        self.cur.execute("""ALTER TABLE vacancies ADD CONSTRAINT fk_company_id 
                            FOREIGN KEY(company_id) REFERENCES employers(company_id)""")

    def into_table(self, *args, name):
        self.cur.execute(f"INSERT INTO {name} VALUES {args}")

class DBManager(DB):
    """класс для работы с данными в БД."""
    def __init__(self, db_name: str):
        super().__init__(db_name)

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

# qwer = DBCreator("qwerty")
