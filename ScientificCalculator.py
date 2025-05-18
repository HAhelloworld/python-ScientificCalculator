# scientific_calculator.py

import math

def display_menu():
    print("\nScientific Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square root (√x)")
    print("7. Logarithm (log base 10)")
    print("8. Natural log (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Factorial (x!)")
    print("13. Value of Pi")
    print("14. Value of e")
    print("q. Quit")

def get_number(prompt="Enter number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def scientific_calculator():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == 'q':
            print("Exiting Scientific Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero.")
                else:
                    print(f"Result: {num1 / num2}")
            elif choice == '5':
                print(f"Result: {math.pow(num1, num2)}")

        elif choice == '6':
            num = get_number()
            if num < 0:
                print("Error: Cannot take square root of a negative number.")
            else:
                print(f"Result: {math.sqrt(num)}")

        elif choice == '7':
            num = get_number()
            if num <= 0:
                print("Error: Logarithm undefined for non-positive numbers.")
            else:
                print(f"Result: {math.log10(num)}")

        elif choice == '8':
            num = get_number()
            if num <= 0:
                print("Error: Natural log undefined for non-positive numbers.")
            else:
                print(f"Result: {math.log(num)}")

        elif choice == '9':
            num = get_number("Enter angle in degrees: ")
            print(f"Result: {math.sin(math.radians(num))}")

        elif choice == '10':
            num = get_number("Enter angle in degrees: ")
            print(f"Result: {math.cos(math.radians(num))}")

        elif choice == '11':
            num = get_number("Enter angle in degrees: ")
            print(f"Result: {math.tan(math.radians(num))}")

        elif choice == '12':
            num = get_number()
            if not num.is_integer() or num < 0:
                print("Error: Factorial is defined for non-negative integers only.")
            else:
                print(f"Result: {math.factorial(int(num))}")

        elif choice == '13':
            print(f"Pi = {math.pi}")

        elif choice == '14':
            print(f"e = {math.e}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    scientific_calculator()
