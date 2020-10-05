from bs4 import BeautifulSoup, NavigableString
import requests

import utils

def tag_cleaning(tag, pos):
    words = ['Geekbench Score', 'SSD', '_', 'Ram', 'Bandwidth', '_']
    tag = tag.replace("\t", '').replace('\n', '')
    tag = tag.replace(words[pos], "").strip()
    return tag

class Vultr():
    def __init__(self):
        self.url = 'https://www.vultr.com/products/cloud-compute/#pricing'
        self.header = []
        self.body = []

    def get_data(self):
        info = requests.get(self.url)
        soup = BeautifulSoup(info.text, 'html.parser')

        header_tags = soup.select('.pt__header > .pt__cell')

        for tag in header_tags:
            self.header.append(tag.text)

        tbody = soup.find('div', {"class": "pt__body"})

        for line in tbody:
            if not type(line) == NavigableString:
                table_dict = {}
                for i, tag in enumerate(line.select('.pt__row-content > .pt__cell')):
                    clear_tag = tag_cleaning(tag.text, i)
                    table_dict[self.header[i]] = clear_tag
                self.body.append(table_dict)

    def terminal_print(self):
        self.get_data()

        utils.terminal_print(self.header, self.body)
    
    def create_csv(self):
        self.get_data()
        utils.export_csv(self.header, self.body, 'vultr.csv')

