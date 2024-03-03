def calculate(expression):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    parts = expression.split()
    try:
        result = float(parts[0])
        i = 1

        while i <len(parts):
            operator = parts[i]
            if operator not in operators:
                print("Invalid operator '{}' at position {}. Please use one of '+', '-', '*', or '/'.".format(operator, i))
                return None
            i+= 1
            next_num = float(parts[i])
            result = operators[operator](result, next_num)

        return result
    except (ValueError, IndexError):
        print("Invalid expression. Please enter a valid expression with numbers and operators")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

expression = input("enter an expression: ")
result = calculate(expression)
if result is not None:
    print(result)
