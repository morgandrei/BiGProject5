import json
from src.classes import Parser, DBCreator, DBManager


def main():

    url = "https://api.hh.ru/employers"
    employers = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон', 'ВкусВилл',
                 'VK', 'СИБУР, Группа компаний']

    employers_list = []  # Список employers дополнен данными с сайта hh
    employers_url_list = []  # Список только url работадателей, для дальнейшего парсинга вакансий
    vacancies_list = []  # Список вакансий
    db_name = input("Введите имя новой базы данных: ")
    new_bd = DBCreator(db_name)
    new_bd.create_employers_table()
    new_bd.create_vacancies_table()
    print(f"Создана новая база данных '{db_name}'")

    for employer in employers:
        hh_parser = Parser(url, employer)

 #       employers_list.append(hh_parser.get_employers())
        args = hh_parser.get_employers()
        new_bd.into_table(*args[:3], name='employers')
        print(args[-1:])


#        employers_url_list.append(hh_parser.get_vacancies_url())
#       print(hh_parser.get_vacancies_url())


#        vacancies_list.append(hh_parser.get_vacancies())
 #       print(json.dumps(hh_parser.get_vacancies(), ensure_ascii=False, indent=2))

    new_bd.conn_close()
if __name__ == '__main__':
    main()
