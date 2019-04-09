import pytest


# contents of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5, 'not equal'


if __name__ == '__main__':
    # pytest.main('--html=./sample_result/result.html')
    pytest.main()