from collections import Counter

price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

special_offers = {
    "A": {
        "quantity": 3,
        "price": 130,
        "description": "3 for the price of 130"
    },
    "B": {
        "quantity": 2,
        "price": 45,
        "description": "2 for the price of 45"
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not skus:
        return -1

    skus = skus.upper()
    skus_counter = Counter(skus)

    total = 0

    for item in skus_counter:
        if item not in price_map:
            return -1

        total += price_map[item]

    return total
