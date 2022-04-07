def func(x):
    return x + 2


def main_func():
    first_call = func(2)
    second_call = func(3)

    result = first_call + second_call
    return result

#tests

from unittest.mock import patch
from app import main_func


@patch(\'app.func\')
def test_main_func(mock_func_first, mock_func_second):
    mock_func_first.return_value = 1
    mock_func_second.return_value = 3
    assert(main_func()) == 4

