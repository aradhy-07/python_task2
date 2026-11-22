with open("data.txt") as file:
        content = file.read()
        if not content:
            print("The file is empty.")
        else:
            print(content)
