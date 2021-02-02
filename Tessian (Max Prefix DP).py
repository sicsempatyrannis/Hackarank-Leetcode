# -*- coding: utf-8 -*-
def is_valid(expression):
    operators = ['+', '-', '*', '/']
    str_list = expression.split()
    op_count = 0
    dig_count = 0
    
    if len(str_list) <= 2:
        return False
    
    for i in str_list:
        if i in operators:
            op_count += 1
        
        if i.isdigit():
            if int(i) < 1:
                return False
            dig_count += 1
            
        if len(i) > 1 and not i.isdigit():
            return False
        
        if i.isalpha():
            dig_count += 1
        
        if not i.isdigit() and not i.isalpha() and i not in operators:
            return False
                
    if dig_count - op_count != 1:
        return False
        
    return True

def is_operator(c):
    return c.isdigit()

def expression_value(expression):
    
    expression = expression.split()
    
    stack = []
    
    for i in expression[::-1]:
        if is_operator(i):
            stack.append(int(i))
            
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            print(v1, v2)
            v = {'+':v1+v2, '-':v1-v2, '*':v1*v2, '/':v1//v2}
            stack.append(v[i])
    
    return stack.pop()

def any_chars(expression):
    for i in expression:
        if i.isalpha():
            return False
        
    return True


            
            
def max_result_expression(expression, variables):
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].
          
    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    
    if len(expression) == 1 and expression.isdigit():
        return int(expression)
    
    if not is_valid(expression):
        return None
    
    if any_chars(expression):
        return expression_value(expression)
    
    
    else:
        variable_list = variables.keys()
        curr_max = -99999
        
        for i in variable_list:
            low, high = variables[i]
            for j in range(low, high):
                if j > 0:
                    new_expression = expression.replace(i, str(j))
                    curr_max = max(curr_max, max_result_expression(new_expression, variables))
                    ret = curr_max

    return ret

print(max_result_expression('9', {}))