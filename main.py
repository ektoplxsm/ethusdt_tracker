import requests
from bs4 import BeautifulSoup
import time


class Currency:
    ETH_DOLLAR = 'https://www.google.com/search?q=eth+usd&oq=&aqs=chrome.3.35i39i362l2j46i39i199i362i465j35i39i362l5.3321536j0j15&sourceid=chrome&ie=UTF-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    current_converted_price = 0
    difference = 1 * current_converted_price / 100

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.ETH_DOLLAR, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll('span', {"class": "pclqee"})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price())
        if currency >= self.current_converted_price + self.difference:
            print("Курс изменился на +1%")
        elif currency <= self.current_converted_price - self.difference:
            print("Курс изменился на -1%")
        print("Стоимость ETHUSDT : = " + str(currency) + "$")
        time.sleep(1)
        self.check_currency()


currency = Currency()
currency.check_currency()
