def main():
    try:
        a :int =int(input("Enter a number "))
        print(a)
    except Exception as e:
        print(e)
    finally:
        print("We are inside finally")

main()
