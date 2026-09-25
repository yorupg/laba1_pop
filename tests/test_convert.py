import pytest

from toolkit.converter import converter

'''здесь проверяю корректность работы конвертера'''

def test_converter_1():
    test_string_1 = [1000, 'g', 'kg']
    result = converter(test_string_1)
    
    assert result == '1.0 kg'

def test_converter_2():
    test_string_2 = [500, 'mm', 'm']
    result = converter(test_string_2)
    
    assert result == '0.5 m'
    
def test_converter_3():
    test_string_3 = [10, 'c', 'f']
    result = converter(test_string_3)
    
    assert result == '50.0 f'
    
def test_converter_4():
    test_string_4 = [1, 'kg', 'kg']
    result = converter(test_string_4)
    
    assert result == '1.0 kg'

def test_converter_5():
    test_string_5 = [1, 'km', 'm']
    result = converter(test_string_5)
    
    assert result == '1000.0 m'
    
def test_wrong_category_1():
    test_string_6 = [1, 'kg', 'km']
    result = converter(test_string_6)
    
    assert result == 'данный тип не поддерживается'
    
def test_wrong_value():
    test_string_7 = [-1, 'kg', 'g']
    result = converter(test_string_7)
    
    assert result == 'неверное числовое значение'
    
def test_below_zero():
    test_string_8 = [-280, 'c', 'k']
    result = converter(test_string_8)
    
    assert result == 'ниже абсолютного нуля'
 
def test_wrong_category_2():
    test_string_9 = [1000, 'kg', 'mg']
    result = converter(test_string_9)
    
    assert result == 'данный тип не поддерживается'   

def test_absolute_error():
    test_string_10 = [52, 'k', 'c']
    result = converter(test_string_10)
    
    assert float(result[:-2]) == pytest.approx(-221.15, abs = 1e-6)

    