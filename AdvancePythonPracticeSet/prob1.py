try:
    with open("file1.txt","r") as f:
        print(f.read())
except FileExistsError:
    print("File Not found")
except FileNotFoundError:
    print("File not exists")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("file2.txt","r") as f:
        print(f.read())
except FileExistsError:
    print("File Not found")
except FileNotFoundError:
    print("File not exists")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("file3.txt","r") as f:
        print(f.read())
except FileExistsError:
    print("File Not found")
except FileNotFoundError:
    print("File not exists")
except Exception as e:
    print(f"An error occurred: {e}")

