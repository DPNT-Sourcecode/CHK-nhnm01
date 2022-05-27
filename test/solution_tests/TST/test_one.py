import pytest

from solutions.sum_r1 import sum_two_integer


class TestSum:
    def test_sum(self):
        assert sum_two_integer(5, 100) == 105

    def test_sum_failure(self):
        with pytest.raises(ValueError):
            sum_two_integer(1, None)

