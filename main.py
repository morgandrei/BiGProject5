from src.utils import get_employers
import json

url = "https://api.hh.ru/employers"
keyword = ['СБЕР', 'Яндекс', 'Тинькофф', 'Почта России', 'Ventra', 'Лаборатория Касперского', 'МегаФон', 'ВкусВилл', 'VK', 'СИБУР, Группа компаний']
for employer in keyword:
    print(json.dumps(get_employers(employer, url), ensure_ascii=False, indent=2))
