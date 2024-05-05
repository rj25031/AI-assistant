import re

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error occurred during calculation: {e}")
        return None


def match_math_expression(text):
    pattern = r'\b(?:\d+\.\d+|\d+)(?:\s*(?:\*\*|sqrt|square)\s*(?:\d+\.\d+|\d+)|\s*[\+\-\*\/]\s*(?:\d+\.\d+|\d+))+\b'
    
    match = re.search(pattern, text)
    
    if match:
        return calculate(match.group())
    else:
        return None



