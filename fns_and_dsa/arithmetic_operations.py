def perform_operation( num1: float, num2: float, operation: str):
    if operation=='add':
        res = num1 + num2
    elif operation == 'subtract':
        res = num1 - num2
    elif operation == 'multiply': 
        res = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("we cant devide on zero")
        else: res = num1 / num2
    else: print("the opeation should be between add, subtract, multiply and divide")
    return res