import requests
import time
import json
#url = "https://api.hh.ru/employers"
#keyword = 'ВкусВилл'


def get_vacancies(keyword, url):
    """
    Получение списка вакансий с платформы HeadHunter
    """


    employers_lst = []
    for page in range(20):
        params = {'per_page': 100,
                  'page': page,
                  'text': keyword,
                  'search_field': 'name',
                  'order_by': "publication_time",
                  'archived': False,
                  }
        vacancies = requests.get(url, params=params).json()
        employers_lst.extend(vacancies['items'])
        for el in employers_lst:
            if el['name'] == keyword and el['open_vacancies'] > 10:
                return el


#print(json.dumps(get_vacancies(keyword, url), ensure_ascii=False, indent=2))


