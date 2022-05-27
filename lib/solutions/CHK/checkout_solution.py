from collections import Counter

price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

special_offers = {
    "A": [
        {
            "quantity": 3,
            "price": 130,
            "description": "3 for the price of 130"
        },
        {
            "quantity": 5,
            "price": 200,
            "description": "5 for the price of 200"
        }
    ],
    "B": [
        {
            "quantity": 2,
            "price": 45,
            "description": "2 for the price of 45"
        }
    ],
    "E": [
        {
            "quantity": 2,
            "price": 40,
            "description": "Buy one get one free"
        }
    ]
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not len(skus):
        return 0

    if not skus:
        return -1

    skus_counter = Counter(skus)

    total = 0

    for item, count in skus_counter.items():
        if item not in price_map:
            return -1

        while count > 0:
            if item in special_offers:
                best_offer_by_qty = 0
                price = 0

                for offer in special_offers[item]:
                    if count >= offer['quantity'] >= best_offer_by_qty:
                        price = offer['price']
                        best_offer_by_qty = offer['quantity']

                count -= best_offer_by_qty
                total += price
            else:
                count -= 1
                total += price_map[item]

    return total


