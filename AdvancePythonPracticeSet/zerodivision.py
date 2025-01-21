try:
    a: int = int(input("Enter a number: "))
    b: int = int(input("Enter another number: "))  # Fixed the missing parenthesis
    print(a / b)
except ZeroDivisionError as e:
    print("Infinite")
except Exception as e:
    print(e)
