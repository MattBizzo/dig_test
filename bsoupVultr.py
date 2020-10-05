from bs4 import BeautifulSoup, NavigableString
import requests

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

        print(f'{self.header[0]:<10} {self.header[1]:<10} {self.header[2]:<10} {self.header[3]:<10} {self.header[4]:<10} {self.header[5]:<10}')
        print('==============================================================')

        for b in self.body:
            bench, storage, cpu, mem, band, price = b.values()
            print(f'{bench:<10} {storage:<10} {cpu:<10} {mem:<10} {band:<10} {price:<10}')
