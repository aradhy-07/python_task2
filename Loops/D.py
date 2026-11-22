n = input("Enter a word : ").lower()
x = 0 
for i in range(0,len(n)):
    if( n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u'):
        x =x+1

print(f"Total vowels are : {x}")