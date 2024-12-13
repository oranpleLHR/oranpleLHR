def calculator():
    global output
    title = ("This is a simple calculater")
    print(title)

    num1 = float(input("enter the first number: "))
    ope = input("enter the operator (+, -, *, /): ")
    num2 = float(input("enter the second number: "))

    if ope =='+':
        output = num1 + num2
    elif ope =='-':
        output = num1 - num2
    elif ope == '*':
        output = num1 * num2
    elif ope == '/':
        if num2 != 0:
            output = num1 / num2
        else:
            return "num2 can not be 0"
    else: return "the given operation is invalid"

    return f"the result is: {output}"

print(calculator())