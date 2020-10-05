from bs4 import BeautifulSoup
import requests

import utils

class DigitalOcean():
    def __init__(self):
        self.url = 'https://www.digitalocean.com/pricing/'
        self.header = []
        self.body = []

    def get_data(self):
        info = requests.get(self.url)
        soup = BeautifulSoup(info.text, 'html.parser')

        basic_table = soup.find('table')

        self.header = [th.text.strip() for th in basic_table.find_all('th') if th.text != '']

        for tr in basic_table.tbody.find_all("tr"):
            line = {}
            for i, td in enumerate(tr.find_all("td")):
                if td.text != '':
                    line[self.header[i]] = td.text.strip()
            self.body.append(line)

    def terminal_print(self):
        self.get_data()
        utils.terminal_print(self.header, self.body)
    
    def create_csv(self):
        self.get_data()
        utils.export_csv(self.header, self.body, 'digitalocean.csv')

    def create_json(self):
        self.get_data()
        utils.export_json(self.body, 'digitalocean.json')