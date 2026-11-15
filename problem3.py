last_names = []
scores = []

with open("scores.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        last_names.append(data[0])
        scores.append(int(data[1]))

def find_highest(names, grades):
    high_var = 0
    high_index = 0

    for i in range(len(grades)):
        if grades[i] > high_var:
            high_var = grades[i]
            high_index = i

    print("Highest Score:")
    print(names[high_index], "-", high_var)

def find_lowest(names, grades):
    low_var = 999
    low_index = 0

    for i in range(len(grades)):
        if grades[i] < low_var:
            low_var = grades[i]
            low_index = i

    print("\nLowest Score:")
    print(names[low_index], "-", low_var)
