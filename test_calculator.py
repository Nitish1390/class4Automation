from calculator import *



def test_addition():
        result = add(5, 3)
        assert result == 8

def test_subtraction():
        result = substract(10, 5)
        assert result == 5

def test_multiplication():
        result = multiply(2, 3)
        assert result == 6

def test_division():
        result = division(10, 2)
        assert result == 5
    
def test_division_by_zero():
        result = division(3, 0)
        assert result == 'infinity'

def test_sqrt():
       result = sqrt(4)
       assert result == 2


