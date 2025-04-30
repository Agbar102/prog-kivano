import requests
from bs4 import BeautifulSoup


MAIN_LINK = "https://www.kivano.kg"


def get_response(url):
    response = requests.get(url)
    return response.text


def parser_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    div_lists = soup.find_all('div', class_='item product_listbox oh')
    items_list = []
    for item in div_lists:
        items_list.append(
            {'title': item.find('strong').get_text(),
            'link': MAIN_LINK + item.find('a')['href'],
             'description': item.find('div', class_='product_text pull-left').
             get_text(strip=True).replace('\xa0', ''),
             'price': item.find('div', class_='listbox_price text-center').get_text(strip=True).replace(' сом', '')
             }

        )
        print(items_list)


def result_parse(sub_category):
    html_text = get_response(MAIN_LINK + "/" + sub_category)
    parser_text(html_text)


# result_parse('tovary-dlya-krasoty')
result_parse('tovary-dlya-krasoty?page=2')









