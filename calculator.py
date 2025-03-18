def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


print('Select Operation :')
print('1.Add')
print('2.Sub')
print('3.Multiply')
print('4.Division')

while True:
    choice = input("Enter choice(1/2/3/4) :")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
        except ValueError:
            print('Invalid input. Please enter a number')
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        cont = input("Do you want to continue? (y/n): ")
        if cont == "no":
            break
    else:
        print("Invalid Input")
