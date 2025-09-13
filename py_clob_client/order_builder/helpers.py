from math import floor, ceil
from decimal import Decimal
from decimal import ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN


def round_down(x: float, sig_digits: int) -> float:
    return floor(x * (10**sig_digits)) / (10**sig_digits)

def round_normal(x: float, sig_digits: int) -> float:
    return round(x * (10**sig_digits)) / (10**sig_digits)

def round_up(x: float, sig_digits: int) -> float:
    return ceil(x * (10**sig_digits)) / (10**sig_digits)


def remove_trailing_zeros(value: Decimal) -> Decimal:
    if value == value.to_integral():
        return value.to_integral()
    else:
        return value.normalize()

def quantize_decimal(value: Decimal, decimal_places: int = 6, rounding: str = ROUND_HALF_EVEN) -> Decimal:
    value = value.quantize(Decimal(f'1e{-decimal_places}'), rounding=rounding)
    return remove_trailing_zeros(value)

def round_down_decimal(x: Decimal, sig_digits: int) -> Decimal:
    return quantize_decimal(x, sig_digits, ROUND_DOWN)

def round_normal_decimal(x: Decimal, sig_digits: int) -> Decimal:
    return quantize_decimal(x, sig_digits, ROUND_HALF_EVEN)

def round_up_decimal(x: Decimal, sig_digits: int) -> Decimal:
    return quantize_decimal(x, sig_digits, ROUND_UP)


def to_token_decimals(x: float) -> int:
    f = (10**6) * x
    if decimal_places(f) > 0:
        f = round_normal(f, 0)
    return int(f)


def decimal_places(x: float) -> int:
    return abs(Decimal(x.__str__()).as_tuple().exponent)
