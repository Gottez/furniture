from decimal import Decimal
from datetime import date
import pytest
from calculate_discount import calculate_discount

_discount_valid_test_data = [

    pytest.param(date(2022, 11, 25), Decimal("0.01"), Decimal("0"), id="Testcase 1"),
    pytest.param(date(2022, 11, 25), Decimal("0.02"), Decimal("0"), id="Testcase 2"),
    pytest.param(date(2022, 11, 25), Decimal("99.98"), Decimal("0"), id="Testcase 3"),
    pytest.param(date(2022, 11, 25), Decimal("99.99"), Decimal("0"), id="Testcase 4"),
    pytest.param(date(2022, 11, 25), Decimal("100"), Decimal("0"), id="Testcase 5"),
    pytest.param(date(2022, 11, 25), Decimal("499.98"), Decimal("0"), id="Testcase 6"),
    pytest.param(date(2022, 11, 25), Decimal("499.99"), Decimal("0"), id="Testcase 7"),
    pytest.param(date(2022, 11, 25), Decimal("500"), Decimal("0"), id="Testcase 8"),

    pytest.param(date(2022, 11, 26), Decimal("0.01"), Decimal("0.15"), id="Testcase 9"),
    pytest.param(date(2022, 11, 26), Decimal("0.02"), Decimal("0.15"), id="Testcase 10"),
    pytest.param(date(2022, 11, 26), Decimal("99.98"), Decimal("0.15"), id="Testcase 11"),
    pytest.param(date(2022, 11, 26), Decimal("99.99"), Decimal("0.15"), id="Testcase 12"),
    pytest.param(date(2022, 11, 26), Decimal("100"), Decimal("0.19"), id="Testcase 13"),
    pytest.param(date(2022, 11, 26), Decimal("499.98"), Decimal("0.19"), id="Testcase 14"),
    pytest.param(date(2022, 11, 26), Decimal("499.99"), Decimal("0.19"), id="Testcase 15"),
    pytest.param(date(2022, 11, 26), Decimal("500"), Decimal("0.28"), id="Testcase 16"),

    pytest.param(date(2022, 11, 28), Decimal("0.01"), Decimal("0.05"), id="Testcase 18"),
    pytest.param(date(2022, 11, 28), Decimal("0.02"), Decimal("0.05"), id="Testcase 19"),
    pytest.param(date(2022, 11, 28), Decimal("99.98"), Decimal("0.05"), id="Testcase 20"),
    pytest.param(date(2022, 11, 28), Decimal("99.99"), Decimal("0.05"), id="Testcase 21"),
    pytest.param(date(2022, 11, 28), Decimal("100"), Decimal("0.1"), id="Testcase 22"),
    pytest.param(date(2022, 11, 28), Decimal("499.98"), Decimal("0.1"), id="Testcase 23"),
    pytest.param(date(2022, 11, 28), Decimal("499.99"), Decimal("0.1"), id="Testcase 24"),
    pytest.param(date(2022, 11, 28), Decimal("500"), Decimal("0.2"), id="Testcase 25"),

    pytest.param(date(2022, 12, 23), Decimal("0.01"), Decimal("0.05"), id="Testcase 30"),
    pytest.param(date(2022, 12, 23), Decimal("0.02"), Decimal("0.05"), id="Testcase 31"),
    pytest.param(date(2022, 12, 23), Decimal("99.98"), Decimal("0.05"), id="Testcase 32"),
    pytest.param(date(2022, 12, 23), Decimal("99.99"), Decimal("0.05"), id="Testcase 33"),
    pytest.param(date(2022, 12, 23), Decimal("100"), Decimal("0.1"), id="Testcase 34"),
    pytest.param(date(2022, 12, 23), Decimal("499.98"), Decimal("0.1"), id="Testcase 35"),
    pytest.param(date(2022, 12, 23), Decimal("499.99"), Decimal("0.1"), id="Testcase 36"),
    pytest.param(date(2022, 12, 23), Decimal("500"), Decimal("0.2"), id="Testcase 37"),

    pytest.param(date(2022, 12, 24), Decimal("0.01"), Decimal("0.15"), id="Testcase 38"),
    pytest.param(date(2022, 12, 24), Decimal("0.02"), Decimal("0.15"), id="Testcase 39"),
    pytest.param(date(2022, 12, 24), Decimal("99.98"), Decimal("0.15"), id="Testcase 40"),
    pytest.param(date(2022, 12, 24), Decimal("99.99"), Decimal("0.15"), id="Testcase 41"),
    pytest.param(date(2022, 12, 24), Decimal("100"), Decimal("0.19"), id="Testcase 42"),
    pytest.param(date(2022, 12, 24), Decimal("499.98"), Decimal("0.19"), id="Testcase 43"),
    pytest.param(date(2022, 12, 24), Decimal("499.99"), Decimal("0.19"), id="Testcase 44"),
    pytest.param(date(2022, 12, 24), Decimal("500"), Decimal("0.28"), id="Testcase 45"),

    pytest.param(date(2022, 12, 28), Decimal("0.01"), Decimal("0"), id="Testcase 46"),
    pytest.param(date(2022, 12, 28), Decimal("0.02"), Decimal("0"), id="Testcase 47"),
    pytest.param(date(2022, 12, 28), Decimal("99.98"), Decimal("0"), id="Testcase 48"),
    pytest.param(date(2022, 12, 28), Decimal("99.99"), Decimal("0"), id="Testcase 49"),
    pytest.param(date(2022, 12, 28), Decimal("100"), Decimal("0"), id="Testcase 50"),
    pytest.param(date(2022, 12, 28), Decimal("499.98"), Decimal("0"), id="Testcase 51"),
    pytest.param(date(2022, 12, 28), Decimal("499.99"), Decimal("0"), id="Testcase 52"),
    pytest.param(date(2022, 12, 28), Decimal("500"), Decimal("0"), id="Testcase 53"),

    pytest.param(date(2022, 11, 29), Decimal("100"), Decimal("0.1"), id="Testcase 59"),
    pytest.param(date(2022, 11, 30), Decimal("100"), Decimal("0.1"), id="Testcase 60"),
    pytest.param(date(2022, 12, 1), Decimal("100"), Decimal("0.1"), id="Testcase 61"),
    pytest.param(date(2022, 12, 2), Decimal("100"), Decimal("0.1"), id="Testcase 62"),
    pytest.param(date(2022, 12, 3), Decimal("100"), Decimal("0.19"), id="Testcase 63"),
    pytest.param(date(2022, 12, 5), Decimal("100"), Decimal("0.1"), id="Testcase 64"),
    pytest.param(date(2022, 12, 6), Decimal("100"), Decimal("0.1"), id="Testcase 65"),
    pytest.param(date(2022, 12, 7), Decimal("100"), Decimal("0.1"), id="Testcase 66"),
    pytest.param(date(2022, 12, 9), Decimal("100"), Decimal("0.1"), id="Testcase 67"),
    pytest.param(date(2022, 12, 10), Decimal("100"), Decimal("0.19"), id="Testcase 68"),
    pytest.param(date(2022, 12, 12), Decimal("100"), Decimal("0.1"), id="Testcase 69"),
    pytest.param(date(2022, 12, 13), Decimal("100"), Decimal("0.1"), id="Testcase 70"),
    pytest.param(date(2022, 12, 14), Decimal("100"), Decimal("0.1"), id="Testcase 70"),
    pytest.param(date(2022, 12, 15), Decimal("100"), Decimal("0.1"), id="Testcase 72"),
    pytest.param(date(2022, 12, 16), Decimal("100"), Decimal("0.1"), id="Testcase 73"),
    pytest.param(date(2022, 12, 17), Decimal("100"), Decimal("0.19"), id="Testcase 74"),
    pytest.param(date(2022, 12, 19), Decimal("100"), Decimal("0.1"), id="Testcase 75"),
    pytest.param(date(2022, 12, 20), Decimal("100"), Decimal("0.1"), id="Testcase 76"),
    pytest.param(date(2022, 12, 21), Decimal("100"), Decimal("0.1"), id="Testcase 77"),
    pytest.param(date(2022, 12, 22), Decimal("100"), Decimal("0.1"), id="Testcase 78")
]


@pytest.mark.parametrize("day,total,expected_discount", _discount_valid_test_data)
def test_valid_discount(day: date, total: Decimal, expected_discount: Decimal):
    discount = calculate_discount(day, total)
    assert discount == expected_discount


invalid_test_data = [

    pytest.param(date(2022, 11, 27), Decimal("1"), id="Testcase 17"),
    pytest.param(date(2022, 12, 4), Decimal("1"), id="Testcase 26"),
    pytest.param(date(2022, 12, 8), Decimal("1"), id="Testcase 27"),
    pytest.param(date(2022, 12, 11), Decimal("1"), id="Testcase 28"),
    pytest.param(date(2022, 12, 18), Decimal("1"), id="Testcase 29"),
    pytest.param(date(2022, 12, 25), Decimal("1"), id="Testcase 54"),
    pytest.param(date(2022, 12, 26), Decimal("1"), id="Testcase 55"),
    pytest.param(2022, Decimal("1"), id="Testcase 56 (date=not a date)"),
    pytest.param(date(2022, 12, 24), 1, id="Testcase 57 (total=not a decimal"),
    pytest.param(date(2022, 12, 24), Decimal("-0.01"), id="Testcase 58(total=negative number")]


@pytest.mark.parametrize("day,total", invalid_test_data)
def test_invalid_arguments(day: date, total: Decimal):
    with pytest.raises(ValueError):
        calculate_discount(day, total)

