from calculations import Calculator

if __name__ == "__main__":
    calc = Calculator()

    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")

    choice = input("Enter choice (1/2/3/4/5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    if choice == '1':
        print(f"Result: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc.divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {calc.power(num1, num2)}")
