l=[3,513,53,535]
index=0
for item in l:
    print(f"The item number at index {index} is {item}")
    index+=1

print("\n\n")
for index,item in enumerate(l):
    print(f"{index},{item}")
