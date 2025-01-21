n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    for i, value in enumerate(table, start=1):
        f.write(f"{n} * {i} = {value}\n")
    f.write("\n")