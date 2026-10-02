def main():
    print("Welcome to the calculator!")
    while True:
        print("Please choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        operation = input("Enter the number of the operation you want to perform: ").strip()
        while operation not in ['1', '2', '3', '4', '5']:
            print("Invalid input. Please enter a number between 1 and 5.")
            operation = input("Enter the number of the operation you want to perform: ").strip()

        if operation == '5':
            print("Goodbye!")
            break

        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        if operation == '1':
            print(f"Result: {first_number + second_number}")
        elif operation == '2':
            print(f"Result: {first_number - second_number}")
        elif operation == '3':
            print(f"Result: {first_number * second_number}")
        elif operation == '4':
            if second_number == 0:
                print("Error: cannot divide by zero.")
            else:
                print(f"Result: {first_number / second_number}")


if __name__ == "__main__":
    main()