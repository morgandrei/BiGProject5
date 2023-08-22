import requests
import time
import json




#print(json.dumps(get_vacancies(keyword, url), ensure_ascii=False, indent=2))

def get_vacansies_by_employer(keyword):
    vacancies_lst = []
    for page in range(20):
        params = {'per_page': 100,
                  'page': page,
                  'employer': keyword,
                  'search_field': 'name',
                  'order_by': "publication_time",
                  'archived': False,
                  }
        vacancies = requests.get("https://api.hh.ru/employers/3529", params=params).json()
        vacancies_lst.extend(vacancies['items'])
        return vacancies_lst

def get_vacancies(url):
    """
    Получение списка вакансий с платформы HeadHunter
    """
    vacancies_lst = []
    for page in range(5):
        params = {'per_page': 100,
                    'page': page,
#                    'text': keyword,
                    'search_field': 'name',
                    'order_by': "publication_time",
                    'archived': False,
                    }
        vacancies = requests.get(url, params=params).json()
        vacancies_lst.extend(vacancies['items'])
        if (vacancies['pages'] - page) <= 1:
            break
        time.sleep(0.5)
    return vacancies_lst

print(json.dumps(get_vacancies("https://api.hh.ru/vacancies?employer_id=3809"), ensure_ascii=False, indent=2))
#rint(get_vacancies("https://api.hh.ru/vacancies?employer_id=3809"))
