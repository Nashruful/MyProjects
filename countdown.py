def calculate(expression):
    try:

        return eval(expression)
    except ZeroDivisionError:
        return "U trying to divice by 0! IDIOTAA"
    except Exception as e:
        return "Error: you're entering a letter.. enter numbers only idiot!"


print("Simple Calculator")
print("Enter 'quit' to exit")

while True:
    expression = input("Enter equation: ")

    if expression.lower() == 'quit':
        break

    result = calculate(expression)
    print(f'{expression} = {result}')
