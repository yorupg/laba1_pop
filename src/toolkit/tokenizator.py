import re


def tokenizator(expr: str):
    expr = expr.replace(' ' , '')
    """ стирает пробелы, чтобы не учитывать их"""
    digit_re = r"(?:^|(?<=[*/+-]))(?P<digit1>[+-]?(?:\d+(?:\.\d*)?|\.\d+))|(?P<digit2>(?:\d+(?:\.\d*)?|\.\d+))"

    float_digits = []
    digits = re.findall(digit_re, expr)

    if digits == []:
        """ проверяет есть ли в выражении числа """
        return ([], [], -1)
    for (digit, sign_digit) in digits:
        digit = digit if digit != '' else sign_digit
        float_digit = float(digit)
        number = digit.lstrip("+-")
        if len(number) > 1 and number[0] == "0" and number[1] != ".":
            """ проверяю наличие чисел с незначащими нулями """
            return ([], [], -3)
        float_digits.append(float_digit)           

    signs = []
    sign_re = r"(?<=[\d.])(?P<sign>[*/+-])"
    signs_re = re.findall(sign_re, expr)
    if signs_re == []:
        """проверяет есть ли в выражении знаки """
        return (float_digits, [], -2)
    for (sign) in signs_re: 
        signs.append(sign) # noqa: PERF402
    
    return (float_digits, signs, 0)
