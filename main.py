from src.utils import get_vacancies
import json

url = "https://api.hh.ru/employers"
keyword = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон', 'ВкусВилл', 'VK', 'СИБУР, Группа компаний']
for el in keyword:
    print(json.dumps(get_vacancies(el, url), ensure_ascii=False, indent=2))
