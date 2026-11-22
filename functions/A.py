x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
z = int(input("Enter a number : "))

def max_(  a , b ,c ):
    if( a >= b and a >= c ):
        m = a 
    if( b >= a and b >= c ):
        m = b
    if( c >= a and c >= b ):
        # print(f"Maximum number is : {x}")
        m = c
    print(f"Maximum number is {m}")

max_(x,y,z)