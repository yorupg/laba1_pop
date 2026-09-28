from toolkit.constants import DISTANCE_METRICS, MASS_METRICS, TEMPERATURE_METRICS
from toolkit.errors import BELOW_ZERO, INCORRECT_DATA, WRONG_CATEGORY, WRONG_VALUE

ABSOLUTE_ZERO_IN_CELSIUS = 273.15

from_f_to_c = lambda f: (f - 32) / 1.8
from_c_to_f = lambda c: c * 1.8 + 32
""" лямбда функция переводит фаренгейты в цельсии или цельсии в фаренгейты """

def get_category(unit):
    """ сопоставляет категорию значения """
    if unit in MASS_METRICS: return 'massa'
    if unit in DISTANCE_METRICS: return 'dlina'
    if unit in TEMPERATURE_METRICS: return 'temperatura'


def convert(value, from_unit, target_unit):
    category = get_category(from_unit)
    """" конвертация """
    match category:
        case "massa":
            """ работаю с переводом единиц массы """
            if value>=0:
                if from_unit=='kg' and target_unit=='g': return f"{value * 1000} {target_unit}"
                if from_unit=='g' and target_unit=='kg': return f"{value / 1000} {target_unit}"
                if from_unit==target_unit: return f"{value} {target_unit}"
            else: 
               return WRONG_VALUE 
        case "dlina":
            temp = value
            if value>=0:
                """ работаю с переводом единиц длины """
                if from_unit == 'mm': temp/=1000
                if from_unit=='cm': temp/=100
                if from_unit=='km': temp *=1000
                if target_unit=='m':  return f"{temp} {target_unit}"
                if target_unit=='mm': return f"{temp * 1000} {target_unit}"
                if target_unit=='cm': return f"{temp * 100} {target_unit}"
                if target_unit=='km': return f"{temp / 1000} {target_unit}"
            else: 
                return  WRONG_VALUE 
        case "temperatura":
            """ работаю с переводом единиц температуры """
            temp = 0
            if from_unit=='c': temp=value
            if from_unit=='k': temp=value - ABSOLUTE_ZERO_IN_CELSIUS
            if from_unit=='f': temp = from_f_to_c(value)
            if temp>=(-ABSOLUTE_ZERO_IN_CELSIUS):
                if target_unit=='c': return f"{temp} {target_unit}"
                if target_unit=='k': return f"{temp + ABSOLUTE_ZERO_IN_CELSIUS} {target_unit}"
                if target_unit=='f': return f"{from_c_to_f(temp)} {target_unit}"
            else: return BELOW_ZERO 

def converter(expr: list) -> float:
    if len(expr)!=3: return INCORRECT_DATA
    """ проверяет точно ли передано 3 аргумента """
    value = float(expr[0])
    input_metric = expr[1].lower()
    output_metric = expr[2].lower()
    

    if get_category(input_metric) == get_category(output_metric):
        """проверяет точно ли пользователь может осуществить конвертацию"""
        return convert(value, input_metric, output_metric)
    else: return 'данный тип не поддерживается'
    
