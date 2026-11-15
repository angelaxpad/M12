last_names = [
    "Garcia",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Perez",
    "Sanchez",
    "Ramirez",
    "Torres"
]

scores = [90, 85, 78, 92, 88, 95, 80, 87, 91, 84]

def display_names(names, grades):
    print("Last Names and Scores:")
    for i in range(len(names)):
        print(names[i], "-", grades[i])

def display_reverse(names, grades):
    print("\nLast Names and Scores in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i], "-", grades[i])
