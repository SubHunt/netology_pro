import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import json


HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


def get_headers():
    return Headers(browser='firefox', os='win').generate()


def main():
    """  Данаая функция ищет на сайте hh.ru только те вакансии, у которых в описании есть ключевые слова "Django" и "Flask"
        По умолчанию поиск идет по краткому описанию, так же можно сделать глубокий поиск по подробному описанию на детальной
        странице вакансии, но это увеличивает время запроса значительно, потому что нужно "проваливаться" по каждой ссылке.
    """
    hh_main_html = requests.get(url=HOST, headers=get_headers()).text
    # В теории должно было помочь с unicode
    # hh_main_html = requests.get(HOST, headers=get_headers())
    # hh_main_html.encoding = response.apparent_encoding
    # hh_main_html = response.text
    if requests.codes.ok == 200:
        soup = BeautifulSoup(hh_main_html, features='lxml', from_encoding='utf-8')
        # Забираем список вакансий...hh.ru через bs4 отдает первые 20 вакансий
        """У методов find и find_all есть атрибуты:
        1. class_ - поиск по классу тега
        2. id - поиск по id тега
        3. attrs - поиск по всем элементам тега.
        Поиск по всем элементам осуществляется с помощью словаря, в который можно перечислить наименования атрибутов тегов, 
        как ключи, а значения - как значения:`soup.find('span', attrs={"data-qa": "vacancy-serp__vacancy-compensation"})
        """
        vacancy_list_tag = soup.find('div', id='a11y-main-content')
        vacancy_tag = vacancy_list_tag.find_all(class_='serp-item')
        vacancies = []
        for vacancy in vacancy_tag:
            link = vacancy.find('a', class_='serp-item__title')['href']
            # Поле с ЗП может отсутствовать, пробуем ее получить в противном случае сообщаеем что ЗП не указана
            try:
                salary = vacancy.find('span', class_='bloko-header-section-3').text
            except Exception:
                salary = 'Зарплата не указана'
            company = vacancy.find('a', class_="bloko-link_kind-tertiary").text
            # .bloko-text встречается несколько раз и не вложенно, забираем второй встречающийся через select
            address = vacancy.select('.bloko-text')[1].text
            # В поле город, так же находится через запятую и ближайшее метро, оно нам не нужно, забираем только город
            city = address.split(",")[0]
            # Поиск по краткому описанию на странице со списком вакансий
            description_body = vacancy.find(class_='g-user-content').text
            # Глубокий поиск по подробноуму описанию на детальной странице вакансии. Время поиска значительно выше...
            # description_html = requests.get(link, headers=get_headers()).text
            # description_body = BeautifulSoup(description_html, features='lxml').find(class_='g-user-content').text
            if 'Django' in description_body or 'Flask' in description_body:
                vacancies.append({
                    'link': link,
                    'salary': salary,
                    'company':company,
                    'city': city,
                    'description': description_body
                })
        pprint(vacancies)
        return vacancies
    else:
        print('Ошибка подключения к сайту {HOST}')


def write_json(vac):
    """ Записывает полученный список словарей с нужными вакансиями в json файл
    """
    with open('vacancies.json', mode='w', encoding='utf-8') as f:
        json.dump(vac, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    list_vacancies = main()
    write_json(list_vacancies)
    print('Файл "vacancies.json" с вакансиями готов!')

