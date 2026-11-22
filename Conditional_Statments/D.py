x = int(input("Enter First number :"))
y = int(input("Enter Seconf number : "))

print('''What do want to do :
1.ADD
2.SUBTRACTION
3.MULTIPLY
4.DIVIDE
''')
p = input("Enter what do want :").lower()
p.lower()
if(p == "add" ):
    print("Add : ",x+y)
if(p == "subtraction" ):
    print("Subtraction  : ",x-y)
if(p == "multiplication" ):
    print(" Multiplication : ",x*y)
if(p == "divide" and y !=0):
    print("Division : ",x/y)

