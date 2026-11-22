with open("sample.txt","w") as f:
    f.write("My name is aaradhya garg")

with open("sample.txt") as f:
    x =f.read()
    print(x)