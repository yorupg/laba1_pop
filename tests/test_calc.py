import pytest

from toolkit.calculator import calculator
from toolkit.validator import validator

'''здесь проверяю корректность работы калькулятора (валидатор также проверяется здесь, 
ошибки токенизатора возвращаются с кодами -1 и -2, это выражение без чисел и без знаков соответственно
текстом эти ошибки выдаются при вызове функции, но для работы кода мне нужно чтобы на этапе токенизации
ошибки выдавались кодами -1 и -2 (верное выражение возвращается с кодом 0))'''

def test_missing_operand():
    test_string_1 = "12 12"
    result = validator(test_string_1)
    
    assert result == 'пропущен операнд'
    
def test_double_operand():
    test_string_2 = "1 ** 5"
    result = validator(test_string_2)
    
    assert result == 'несколько бинарных операторов подряд'

def test_no_numbers():
    test_string_3 = '++-+-'
    result = calculator(test_string_3)
    
    assert result == -1

def test_empty_expression():
    test_string_4 = '     '
    result = validator(test_string_4)
    
    assert result == 'пустое выражение'
    
def test_calculator_1():
    test_string_5 = '2 + 2*2'
    result = calculator(test_string_5)
    
    assert result == 6.0
    
def test_calculator_2():
    test_string_6 = '10 / 4'
    result = calculator(test_string_6)
    
    assert result == 2.5
    
def test_calculator_3():
    test_string_7 = '1 + -2'
    result = calculator(test_string_7)
    
    assert result == -1.0
    
def test_calculator_4():
    test_string_8 = '2/4 + 3*4'
    result = calculator(test_string_8)
    
    assert result == 12.5

def test_invalid_symbol():
    test_string_9 = '2 + asd + 885'
    result = validator(test_string_9)
    
    assert result == 'недопустимый символ'
    
def test_division_by_zero():
    test_string_10 = '2 *2 +48/0'
    result = calculator(test_string_10)
    
    assert result == 'деление на 0 запрещено'
    
def test_too_many_points():
    test_string_11 = '2 *2 +48..5-85.5'
    result = validator(test_string_11)
    
    assert result == 'ошибка ввода, в числе больше одной точки'
    
def test_calculator_5():
    test_string_12 = '5-3 + -9 * -1 /6 -9'
    result = calculator(test_string_12)
    
    assert result == -5.5

def test_absolute_error():
    test_string_13 = '1/5000'
    result = calculator(test_string_13)
    
    assert result == pytest.approx(0.0002, abs = 1e-6)
    
    

