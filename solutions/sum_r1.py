import logging


def sum_two_integer(input_one, input_two):
    try:
        int(input_one)
        int(input_two)
    except ValueError:
        logging.error("Input is not a integer")
    if 0 <= input_one <= 100 and 0 <= input_two <= 100:
        return sum(input_one, input_two)





