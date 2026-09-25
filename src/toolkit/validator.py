import re

from toolkit.errors import (
    DOUBLE_OPERATOR,
    EMPTY_EXPRESSION,
    INPUT_ERROR,
    INVALID_SYMBOL,
    MISSING_OPERAND,
    TOO_MANY_POINTS,
)
from toolkit.tokenizator import tokenizator

correct_symbols_re = r"[^\d\.+\-\*\/]"
count_points_re = r"\.\d*\."
operand_re = r"\d\.?( +| +[^\+\-\*\/]*)\.?\d"
def validator(expr: str) -> bool:
    """ проверяет корректность введённого выражения """
    operand = re.search(operand_re, expr)
    if operand != None: 
        return MISSING_OPERAND
    
    expr = expr.replace(' ', '')
    """ удаляю все пробелы и проверяю пустое ли выражение """
    if expr == '': 
        return EMPTY_EXPRESSION
    
    if '**' in expr or '//' in expr or '+*' in expr or '-*' in expr or '+/' in expr \
        or '-/' in expr or '*/' in expr or '/*' in expr:
        return DOUBLE_OPERATOR
    
    numbers = tokenizator(expr)[0]
    temp = expr.replace('-','+').replace('*','+').replace('/','+')
    if '+++' in temp and len(numbers)>0:
        return DOUBLE_OPERATOR   
    
    symbols_re = re.search(correct_symbols_re, expr)
    """ проверяю есть ли недопустимые символы"""
    if symbols_re != None:
        return INVALID_SYMBOL    
    
    count_points = re.search(count_points_re, expr)
    """ считаю количество точек в числе """
    if count_points != None: 
        return TOO_MANY_POINTS
    
    if (expr[-1] in '+-*/' or expr[0] in '*/') and len(numbers)>0:
            return INPUT_ERROR
    
    if (expr[:2] == "--" or expr[:2] == "++" or expr[:2] == "+-" or expr[:2] == "-+" ) and len(numbers)>0:
        """ проверяю не начинается ли выражение с нескольких операторов"""
        return INPUT_ERROR
        
    return True
    