x= ["shubham","aaradhya","rohan","harry"]

y = input("Enter the name :").lower()

b = False
for i in range (4):
    if( x[i] == y ):
        b= True
        print("Yes the name is in the list ")

if( not b):
    print("The name is not in the list ")