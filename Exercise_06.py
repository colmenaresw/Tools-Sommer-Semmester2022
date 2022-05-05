"""
Wilfredo Colmenares
Computer Simulation in Science
Sommer Semester 2022
2130541
exercise 6, implementation of room and occupant classes
"""
import re


class Room:
    """
        class implementation of a room
    """
    def __init__(self, building, floor, number) -> None:
        self.building = building
        self.floor = floor
        self.number = number

    def __str__(self) -> str:
        return (f"building-> {self.building} floor -> {self.floor} number->{self.number}")


class Occupant:
    """
        class implementation of an occuppant
    """
    def __init__(self, familyname, givenname, room) -> None:
        self.familyname = familyname
        self.givenname = givenname
        self.room = room

    def __str__(self) -> str:
        return (f"family name-> {self.familyname}\n given name-> {self.givenname}\n {self.room}")
        


#################### MAIN SCRIPT ######################

if __name__ == "__main__":

    # load the file into an array
    with open('fcb_math.txt', "r") as f:
        arr = f.read().splitlines()

    # we create an empty array to save the occupants
    occupants = []

    for o in arr:
        # we obtain the names from the string
        familiy = re.findall("^.+(?=,)", o)
        given = re.findall("(?<=\s).+(?=\s)", o)

        # and the info for the room
        room_s = re.findall("(?<=\s)\w+\..*", o)
        room = re.split("\.", room_s[0])
        room_c = Room(room[0], room[1], room[2])

        # we save the information as an instance of occupant
        occupants.append(Occupant(familiy[0], given[0], room_c))

    # we print the instances
    for occupant in occupants:
        print(occupant)
    