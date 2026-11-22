x = "i am a student of lnmiit and my computer science and engineering"
appeared = [" "]
for i in x :
    if(i not in appeared):
        y = x.count(i)
        print(f"{i} appears {y} times")
        appeared.append(i)
else:
    print("Thanks")