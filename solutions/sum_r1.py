import logging


def sum_two_integer(input_one, input_two):
    try:
        int(input_one)
        int(input_two)
    except ValueError:
        logging.ERROR(f"")

    pass



