import json
import csv

def terminal_print(header, body):
    print(f'{header[0]:<10} {header[1]:<10} {header[2]:<10} {header[3]:<10} {header[4]:<10} {header[5]:<10}')
    print('==============================================================')

    for b in body:
        b1, b2, b3, b4, b5, b6 = b.values()
        print(f'{b1:<10} {b2:<10} {b3:<10} {b4:<10} {b5:<10} {b6:<10}')


def export_csv(header, table, file_name):
    for _ in table:
        with open(file_name, "w") as newfile:
            writer = csv.DictWriter(newfile, header)
            writer.writeheader()
            for row in table:
                if row:
                    writer.writerow(row)

def export_json(table, file_name):
    with open(file_name, 'w') as newfile:
        json.dump(table, newfile)
