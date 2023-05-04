import json
from datetime import datetime
import xlrd


def main():
    book = xlrd.open_workbook("myDomains.xls")
    sh = book.sheet_by_index(0)

    domains = [sh.cell_value(rowx=x, colx=0).encode('idna').decode('utf-8') for x in range(1, sh.nrows)]
    domains_sorted = sorted(domains)
    output = {
        'domains': domains_sorted,
        'date fetched': datetime.now().strftime('%Y-%m-%d')
    }
    with open('mozilla-owned-dns-domains.json', 'w') as f:
        json.dump(output, f, indent=2)


if __name__ == "__main__":
    main()