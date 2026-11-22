
x = [] 
for i in range(5):
    y =int(input("Enter marks : "))
    x.append(y)

a = sum(x)
b= a/5
print(f"Sum of all marks : {a}")
print(f"Average of marks : {b}")

q = 0
for i in range(5):
    if(x[i]>q):
        q = x[i] 

print(f"Highest marks is : {q}")
r = q 
for i in range(5):
    if(x[i]<r):
        r = x[i] 
print(f"Lowest marks is : {r}")