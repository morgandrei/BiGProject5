from src.classes import Parser, DBCreator, DBManager


def main():
    url = "https://api.hh.ru/employers"
    employers = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон',
                 'ВкусВилл',
                 'VK', 'СИБУР, Группа компаний']

    db_name = input("Введите имя новой базы данных: ")
    new_bd = DBCreator(db_name)
    new_bd.create_employers_table()  #
    new_bd.create_vacancies_table()  #
    print(f"Создана новая база данных '{db_name}'")

    for employer in employers:
        hh_parser = Parser(url, employer)

        #       employers_list.append(hh_parser.get_employers())
        args_employer = hh_parser.get_employers()
        new_bd.into_table(*args_employer[:3], name='employers')  #
        print(args_employer[-1:])

        for vac in hh_parser.get_vacancies():
            if vac['snippet']['requirement'] is None:
                requirement = ''
            else:
                requirement = vac['snippet']['requirement']
            if vac['snippet']['responsibility'] is None:
                responsibility = ''
            else:
                responsibility = vac['snippet']['responsibility']
            description = requirement + responsibility
            edit_description = description.replace('\'', '')
            if vac['salary'] is None:
                salary_from = 0
                salary_to = 0
            else:
                if vac['salary']['from'] is not None:
                    salary_from = vac['salary']['from']
                if vac['salary']['to'] is not None:
                    salary_to = vac['salary']['to']
            args_vacancy = [vac['id'], vac['employer']['id'], vac['name'], salary_from, salary_to,
                            vac['alternate_url'], edit_description]

            new_bd.into_table(*args_vacancy, name='vacancies')


    new_bd.conn_close()


if __name__ == '__main__':
    main()
