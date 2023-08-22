import json
from src.classes import Parser, DBCreator, DBManager
def main():
    filename = "config.ini"
    url = "https://api.hh.ru/employers"
    employers = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон', 'ВкусВилл',
                 'VK', 'СИБУР, Группа компаний']

    employers_list = []  # Список employers дополнен данными с сайта hh
    employers_url_list = []  # Список только url работадателей, для дальнейшего парсинга вакансий
    vacancies_list = [] # Список вакансий
    for employer in employers:
        hh_parser = Parser(url, employer)

#       employers_list.append(hh_parser.get_employers())
#       print(hh_parser.get_employers())
        print(len(hh_parser.get_employers()))

#       employers_url_list.append(hh_parser.get_vacancies_url())
#       print(hh_parser.get_vacancies_url())
        print(len(hh_parser.get_vacancies_url()))

#       vacancies_list.append(hh_parser.get_vacancies())
#       print(hh_parser.get_vacancies())
        print(len(hh_parser.get_vacancies()))


#   print(json.dumps(employers_list, ensure_ascii=False, indent=2))
#   print(employers_url_list)
#   print(vacancies_list)

if __name__ == '__main__':
    main()
