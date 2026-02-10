import pytest
import random
from empoyer import Employee, RAISE_AMOUNT  # теперь импортируется

@pytest.fixture
def emp():
    return Employee('Ivanov', 1000)

def test_default_raise(emp):
    emp.give_raise()
    assert emp.salary == 1000 + RAISE_AMOUNT  # использует константу

def test_custom_raise(emp):
    emp.give_raise(raise_amount=500)
    assert emp.salary == 1000 + 500

def test_random_raise(emp):
    rand = random.randint(100, 1000)
    emp.give_raise(raise_amount=rand)
    assert emp.salary == 1000 + rand