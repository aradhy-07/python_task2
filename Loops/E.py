
for i in range(1,101):
    x = False
    for j in range (2,i):
        if( i % j == 0 ):
            x = True
            break
    if not x:
        print(i,end= ", ")