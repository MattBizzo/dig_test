import argparse

from bsoupVultr import Vultr

parser = argparse.ArgumentParser(description='Extract vultr or digitalocean cloud info')
parser.add_argument('--print', help='print table on terminal', action="store_true")
parser.add_argument('--save_csv', help='save data as csv file', action="store_true")
parser.add_argument('--save_json', help='save data as json file', action="store_true")

args = parser.parse_args()


if __name__ == "__main__":

    cloud = Vultr()

    if args.print:
        cloud.terminal_print()
    
    if args.save_csv:
        cloud.create_csv()

    if args.save_json:
        cloud.create_json()

