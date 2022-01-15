from requests import get
from datetime import datetime


def currency_rates(currency_pair):
    currency_pair = currency_pair.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    if currency_pair not in content:
        return None
    date = content[:content.find('" name')]
    date = date[date.rfind('"') + 1:]
    date = datetime.strptime(date, "%d.%m.%Y")
    content = content[content.rfind(currency_pair):]
    content = content[:content.find('</Value>')]
    content = content[content.rfind('>') + 1:]
    content = float(content.replace(',', '.'))
    return f'Курс {currency_pair} на {date} равен {content} '


if __name__ == '__main__':
    print(currency_rates('usd'))