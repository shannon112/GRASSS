import twstock

fubon_contracted_stock_ids = [
    "00900",
    "00895",
    "00885",
    "00903",
    "00892",
    "00897",
    "006208",
    "00692",
    "00662",
    "006205",
    "0052",
    "00639",
    "00645",
    "00652",
    "00700",
    "00709",
    "00717",
    "00730",
    "00733",
    "00783",
    "00712",
    "00731",
    "00877",
    "006207",
    "00636",
    "00701",
    "00875",
    "00878",
    "00881",
    "00893",
    "00757",
    "0050",
    "0055",
    "0056",
    "0061",
    "00646",
    "00713",
    "00739",
    "00762",
    "00850",
    "00861",
    "00876",
    "006206",
    "00752",
    "00891",
    "00896",
    "00888",
    "00728",
    "00899",
    "1101",
    "1102",
    "1210",
    "1215",
    "1216",
    "1301",
    "1303",
    "1326",
    "1402",
    "1434",
    "1476",
    "1590",
    "2002",
    "2049",
    "2105",
    "2207",
    "2301",
    "2303",
    "2308",
    "2317",
    "2324",
    "2327",
    "2330",
    "2344",
    "2345",
    "2353",
    "2354",
    "2356",
    "2357",
    "2377",
    "2379",
    "2382",
    "2385",
    "2395",
    "2408",
    "2409",
    "2412",
    "2454",
    "2474",
    "2492",
    "2548",
    "2603",
    "2609",
    "2615",
    "2633",
    "2801",
    "2834",
    "2880",
    "2881",
    "2882",
    "2883",
    "2884",
    "2885",
    "2886",
    "2887",
    "2888",
    "2890",
    "2891",
    "2892",
    "2912",
    "3008",
    "3034",
    "3037",
    "3045",
    "3105",
    "3231",
    "3481",
    "3702",
    "3711",
    "4904",
    "4938",
    "5347",
    "5871",
    "5876",
    "5880",
    "6239",
    "6488",
    "6505",
    "6669",
    "8046",
    "8299",
    "8454",
    "9904",
    "9910",
    "9921",
    "9945",
]

my_interested_stock_ids = [
    "0050",
    "2330",
    "2454",
    "2379",
    "3034",
    "2884",
    "2885",
    "2892",
]
test_stock_ids = ["2330", "2454"]


def gen_stock_name_list(id_list):
    stock_name_list = []
    for id in id_list:
        stock_name_list.append(get_stock_name(id))
    return stock_name_list


def get_stock_name(id):
    if id in twstock.codes:
        return twstock.codes[id].name
    return "unknown"


class MyStock:
    def __init__(self, id="", price=0.0, quantity=0, cost=0.0, dividend=0.0):
        self.id = id  # str
        self.price = price
        self.quantity = quantity
        self.cost = cost
        self.dividend = dividend

    def print_info(self):
        print(self.id, self.price, self.quantity, self.cost, self.dividend)

    def combine(self, combined_stock):
        assert self.id == combined_stock.id
        self.price = (
            self.price * self.quantity + combined_stock.price * combined_stock.quantity
        )
        self.quantity += combined_stock.quantity
        self.price /= self.quantity
        self.cost += combined_stock.cost
