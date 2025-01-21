try:
    a = int(input("Enter an input: "))
    print("You entered:", a)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error Found")
except Exception as e:
    print("An error occurred:", e)

print("Thank You")