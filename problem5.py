player_names = []
averages = []

with open("players.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        player_names.append(data[0])
        averages.append(float(data[1]))

def display_players(names, batting):
    print("Player Names and Batting Averages:")
    for i in range(len(names)):
        print(names[i], "-", batting[i])

def search_player(names, batting, last_name):
    found = False

    for i in range(len(names)):
        name_parts = names[i].split()

        if name_parts[-1].lower() == last_name.lower():
            print("Player Found:")
            print(names[i], "-", batting[i])
            found = True

    if found == False:
        print("Name not found")

display_players(player_names, averages)

while True:
    search_name = input("\nEnter a last name (or quit to exit): ")

    if search_name.lower() == "quit":
        break

    search_player(player_names, averages, search_name)
