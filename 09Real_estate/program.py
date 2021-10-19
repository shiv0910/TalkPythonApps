import csv
import os
try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

def print_header():
    print("-------------------------------------------------")
    print("           REAL ESTATE DATA MINING APP")
    print("-------------------------------------------------")
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, "data", "SacramentoRealEstateTransactions2008.csv")

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:

        reader = csv.DictReader(fin)   #dictreader returns dictionary not rows
        purchases = []

        for row in reader:
            #print(type(row), row)
            #print(f"Bed count: {row['beds']}")
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0]).__dict__)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=",")
        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]




# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print("found header: " + header)

#         lines = []
#         for line in fin:
#             line_data = line.strip().split(",")
#             bed_count = line_data[4]
#             lines.append(line_data)

#         print(lines[:5])

# def get_price(p):
#     return p.price

def query_data(data): # : list[Purchase]):
    # if data was sorted by price
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print(
        f"The most expensive house was ${high_purchase.price:,} with {high_purchase.beds} beds and {high_purchase.baths} baths.")

    # least expensive house?
    low_purchase = data[0]
    print(f"The least expensive house was  ${low_purchase.price:,} with {low_purchase.beds} beds and {low_purchase.baths} baths.")

    # average price house?


    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price # projection or items to create
        for p in data # the set to process
    ]

    avg_price = statistics.mean(prices)
    print(f"The average house price is ${int(avg_price):,}.")


    # average price of 2 bedroom houses ?
    # prices = []
    # baths = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)
    #         baths.append(pur.baths)


    # two_bed_homes = [
    #     p   # projection or items to create
    #     for p in data # the set to process
    #     if p.beds == 2 # test / condition / filter
    # ]
    # avg_price = statistics.mean([p.price for p in two_bed_homes])  # [ list comprehensions ]
    # avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    # avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])

    # print(f"Average 2-bedroom house is ${int(avg_price):,}, with {int(avg_baths)} baths and at{int(avg_sqft):,} sqft.")

    """list comprehension + generator. to convert to generator change the list [] to () and add a homes list instead"""
    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))
    print(f"The average 2-bedroom home is ${int(avg_price):,} at {round(avg_sqft):,} sqft with {round(avg_baths)} baths.")


def announce(item, msg):
    print(f"Pulling {item} for {msg}")
    return item

if __name__ == '__main__':
    main()


