from toolkit.tokenizator import tokenizator
from toolkit.validator import validator
from toolkit.errors import (DIVISION_BY_ZERO)

def calculator(expr:str) -> float:
    """ считает значение выражения """
    is_valid = validator(expr)
    if is_valid != True:
        return is_valid
    numbers, symbols, code = tokenizator(expr)
    
    if code == -2 and len(numbers) == 1:
        return float(numbers[0])
    if code != 0:
        return code
    symbol = 0
    while symbol < len(symbols):
        if symbols[symbol] == '*':
            result = numbers[symbol] * numbers[symbol+1]
            numbers[symbol] = result
            numbers.pop(symbol+1)
            symbols.pop(symbol)
                    
        elif symbols[symbol] == '/':
            if numbers[symbol+1] == 0.0: 
                return DIVISION_BY_ZERO
            else:
                result = numbers[symbol] / numbers[symbol+1]
                numbers[symbol] = result
                numbers.pop(symbol+1)
                symbols.pop(symbol)
        else: 
            symbol += 1 
                
    symbol = 0  
    while symbol < len(symbols):                      
        if symbols[symbol] == '+':
                    result = numbers[symbol] + numbers[symbol+1]
                    numbers[symbol] = result
                    numbers.pop(symbol+1)
                    symbols.pop(symbol)   
                                
        elif symbols[symbol] == '-':
                    result = numbers[symbol] - numbers[symbol+1]
                    numbers[symbol] = result
                    numbers.pop(symbol+1)
                    symbols.pop(symbol)
        else:
            symbol += 1
                
                
    return float(numbers[0]) 
        

            