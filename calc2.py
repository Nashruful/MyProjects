def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def divide(x, y):
    if x == 0:
        print("can't divide by zero")

    return x / y

operators = { "+":add,
              "-":sub,
              "*":mul,
              "/":divide}

def calculate(x,operator,y):
    if operator in operators:
        operation = operators[operator]
        result = operation(x,y)
        return result
    else:
        return "invalid operator"
x = int(input("enter 1st number: "))
v = input(": ")
c = int(input("enter 2nd number: "))
print(calculate(x,v,c))
