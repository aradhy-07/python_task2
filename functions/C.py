list_ = []

for i in range(5):
    x = int(input("Enter marks :"))
    list_.append(x)

def average(marks_list):
    return sum(marks_list) / len(marks_list)

print(average(list_))
