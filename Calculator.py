a = float(input ("Enter the first number:"))
b = float(input ("Enter the second number:"))
op = input ("Enter operator (+, -, *, /, %, **):")


if op == '+':
    print (a + b)
elif op == '-':
    print (a - b)
elif op == '*':
    print (a * b)
elif op == '/':
    print (a / b)
elif op == '%':
    print (a % b)
elif op == '**':
    print (a ** b)
else:
    print ("Envalid Operation")

