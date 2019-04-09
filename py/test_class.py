import pytest


# contents of test_class.py
class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')


if __name__ == '__main__':
    pytest.main('-q --html=a.html')
    # pytest.main('q')
