from typing import List

MAX_NUMBER_BASE = 9
MIN_NUMBER_BASE = 2

def solution(expressions: List[str]):
    
    """
    44 + 5 
    51 - 49 = 2
    10 - 2 = 8
    
    dec
    21 - 5 = 16
    hexa
    21 - 5 = 12
    
    14 + 3 = 17
    14 + 3 = 21
    
    Goal:
    1. Find out which number system 2 ~ 9
        - full addition equation
          10 - diff(act_value - dec_value) = x number system
        - full subtration equation
          10 - diff(dec_value - act_value) = x number system
    2. Fill in the "X"
        - Possible values are numeric value or "?"
        
    input:
        expressions - ex. "A + B = C"
        
    Output:
        
    """
    
    comp_expr_indices = [expr for expr in expressions if "X" not in expr]
    base = get_number_base(comp_expr_indices)
    if base == 0:
        base = get_number_base_from_digits(expressions)
    
    breakpoint()

    evaluated_exprs = []
    for expr in expressions:
        if "X" in expr:
            if base != 0:
                x_val = eval_with_base(expr, base)
            else:
                x_val = "?"
            evaluated_exprs.append(
                expr.replace("X", str(x_val))
            )
    
    return evaluated_exprs


def convert_num_to_base(num, base):
    result = 0
    digit_offset = 0
    
    while True:
        q, r = divmod(num, base)
        result += r * pow(10, digit_offset)
        if q == 0:
            break
        num = q
    return result

def convert_num_to_decimal(num, base):
    result = 0
    pwr = 0
    while num > 0:
        num, digit = divmod(num, 10)
        result += digit * pow(base, pwr)
        pwr += 1
    return result


def eval_with_base(expr: List[str], base: int):
    left, right = map(lambda x: x.strip(), expr.split("="))
    [num1, op, num2] = map(lambda x: x.strip(), left.split(" "))
    dec_num1 = convert_num_to_decimal(int(num1))
    dec_num2 = convert_num_to_decimal(int(num2))
    
    if op == "+":
        return convert_num_to_base(dec_num1 + dec_num2, base)
    elif op == "-":
        return convert_num_to_base(dec_num1 - dec_num2, base)
    
    raise Exception("unrecognized op")


def get_largest_digit(nums: List[int]):
    largest_digit = 0
    for num in nums:
        while num > 0:
            digit = num % 10
            largest_digit = max(largest_digit, digit)
            num //= 10
    return largest_digit


def get_number_base_from_digits(expressions: List[str]):
    expr_terms = []
    for expr in expressions:
        expr_terms.extend(expr.split(" "))
    
    numbers = map(
        lambda x: int(x),
        filter(
            lambda x: x.isnumeric(), 
            expr_terms
        ),
    )
    if get_largest_digit(numbers) == (MAX_NUMBER_BASE - 1):
        return MAX_NUMBER_BASE
    return 0


def get_digit_delta(decimal_value, actual_value):
    delta = 0
    while decimal_value > 0:
        dec_digit = decimal_value % 10
        act_digit = actual_value % 10
        
        delta = abs(dec_digit - act_digit)
        if delta > 0:
            break
            
        decimal_value //= 10
        actual_value //= 10
            
    return delta


def get_number_base(expressions: List[str]) -> int:
    for expr in expressions:
        left, right = map(lambda x: x.strip(), expr.split("="))

        delta = get_digit_delta(
            decimal_value=eval(left),
            actual_value=int(right),
        )
            
        if delta != 0:
            if "+" in left:
                return delta
            elif "-" in left:
                return 10 - delta
    
    return 0


if __name__ == "__main__": 
    expr = 	["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
    solution(expr)
