import argparse

from bsoupVultr import Vultr
from bsoupDigitalOcean import DigitalOcean

parser = argparse.ArgumentParser(description='Extract vultr or digitalocean cloud info')
parser.add_argument('--print', help='print table on terminal', action="store_true")
parser.add_argument('--save_csv', help='save data as csv file', action="store_true")
parser.add_argument('--save_json', help='save data as json file', action="store_true")
parser.add_argument('--digital_ocean', help='use cloud as digitalocean', action="store_true")

args = parser.parse_args()

if __name__ == "__main__":

    if args.digital_ocean:
        cloud = DigitalOcean()
    else:
        cloud = Vultr()

    if args.print:
        cloud.terminal_print()
    
    if args.save_csv:
        cloud.create_csv()

    if args.save_json:
        cloud.create_json()

