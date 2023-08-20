
import json
from src.classes import Parser, DBCreator, DBManager
filename = "config.ini"
url = "https://api.hh.ru/employers"
employers = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон', 'ВкусВилл', 'VK', 'СИБУР, Группа компаний']



db_creator = DBCreator(filename)



for employer in employers:
    hh_parser = Parser(url, employer)
    print(json.dumps(hh_parser.get_employers(), ensure_ascii=False, indent=2))
