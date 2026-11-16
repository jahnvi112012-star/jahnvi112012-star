a = input("Enter an operator (+, -, *, /): ")
b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

if a == '+':
    print("Answer =", b + c)

elif a == '-':
    print("Answer =", abs(b - c))

elif a == '*':
    print("Answer =", b * c)

elif a == '/':
    if c != 0:
        print("Answer =", b / c)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operator!")
