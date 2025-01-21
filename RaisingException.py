a:int=(int(input("Enter 1st number : ")))
b:int=(int(input("Enter 2nd number : ")))

#here program will not crash if error or exception is found
#try:
#    print(a/b)
#except ZeroDivisionError:
#    print("The number cannot be divided by 0")
#except Exception as e:
#    print(e)

if(b==0):
    raise ZeroDivisionError("The number Cannot be divisible by Zero")
else:
    print(f"The division of a/b is {a/b}")

#here this will stop the program immediately
