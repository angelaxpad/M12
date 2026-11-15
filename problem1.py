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

def display_names(names):
    print("Last Names:")
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    print("\nLast Names in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])
