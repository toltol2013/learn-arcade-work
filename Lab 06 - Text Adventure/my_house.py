class Room:


    def __init__(self, name, descr, north, east, south, west, go_up, go_dpwn):

        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = go_up
        self.down = go_dpwn

def main():


    room_list = []
    names = ["Hall", "Bathroom", "Living room", "Bedroom", "Library", "Kitchen", "bedroom2", "bathroom2", "bedroom3"]
    descriptions = ["You are in the Hall. At your right you have a shoe cabinet to put your shoes inside. There is also a little window. There are doors to the north and to the east.",
        "You are in the Bathroom. at your left you have a toilet and in front of you a shower. There are doors to the east and to the west.",
        "you are in the Living room. In front of you you have a sofa and at you right a TV. There are doors to the west and to the north.",
        "You are in the Bedroom. In front of you there is a big bed and on your right there is a wardrobe. There are doors om the south and on the west.",
        "You are in the Library. There are a lot of books and there is a table with some chairs. There are doors on the east and on the west.",
        "You are in the kitchen. There si a big table with some chairs. There is also a fridge and a cooker. There are doors to the sout and to the east.",
        "You are in the second bedroom. In front of you there is a bed and an armchair. At your left you have a window with curtains. There is a door to the east.",
        "You are in the second bathroom. in front of you there is a little window without curtains, there is a toilet and a bath. There is also a shower. There are doors to the east and to the west.",
        "You are in the third bedroom. It's a really big room. At your right there is a big shelf. In front of you there is a really big bed and at your right a big window with yellow curtains. There is a door at the west."
    ]

    norths = [5, None, 3, None, None, None, None, None, None]
    easts = [1, 2, None, None, 3, 4, None, None, None]
    souths = [None, None, None, 2, None, 0, None, None, None]
    wests = [None, 0, 1, 4, 5, None, None, None, None]
    ups = [6, None, None, None, None, None, None, None, None]
    downs = [None, None, None, None, None, None, 0, None, None]

    for i in range(len(names)):

        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print(room_list[current_room].description)
        answer = input("What do you want to do? Enter n for north, e for east, s for south, w for west, u for up, d for down, q to quit:")

        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == "n":
            new_room = room_list[current_room].north

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "e":
            new_room = room_list[current_room].east

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "s":
            new_room = room_list[current_room].south

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "w":
            new_room = room_list[current_room].west

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "u":
            new_room = room_list[current_room].up

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "d":
            new_room = room_list[current_room].down

            if new_room is None:
                print("Sorry, you can't go that way")

            else:
                current_room = new_room

        elif move == "q":
            print("Goodbye. I hope you liked exploring the house.")
            done = True

        else:
            print("Sorry, I did not understand your answer")


main()