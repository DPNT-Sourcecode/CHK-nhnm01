def validate_input_unsigned(input_value: int, max_value: int = 100):
    return 0 <= input_value <= max_value


def sum_two_integer(input_one: int, input_two: int):
    if validate_input_unsigned(input_one) and validate_input_unsigned(input_two):
        return input_one + input_two
    else:
        raise ValueError("The input provided is not between 0 to 100")

