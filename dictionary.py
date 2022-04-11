#!/usr/bin/python3

## Game of Life
## author:  Hannah Rittich, Holger Arndt
## version: 18.03.2022
## framework for sheet 1, exercise 4
# edit: Wilfredo Colmenares Code: 2130541

import json, time

def main():

    dictionary = load_dictionary()  # where the dictionary will be stored
    dictionary.get()

    # Implement here 

    while True:
        # main loop of the program
        user_i = input("look up (1), List(2), New Entry (3), Delete Entry(4), Exit(0)\n")

        if user_i == "1":
            look_up(dictionary)
        elif user_i == "2":
            list_(dictionary)
        elif user_i == "3":
            new_entry(dictionary)
        elif user_i == "4":
            delete_entry(dictionary)
        elif user_i == "0":
            print("Good Bye!")
            break
    
    save_dictionary(dictionary)

def load_dictionary():
    """Loads a dictionary from file and returns it."""

    try:
        with open('words.json', 'r') as fp:
            dictionary = json.load(fp)
    except:
        print('WARNING: No dictionary found.')
        dictionary = {}

    return dictionary

def save_dictionary(dictionary):
    """Saves a dictionary to a file."""

    with open('words.json', 'w') as fp:
        json.dump(dictionary, fp, indent = 2, sort_keys = True)




#### Functions for the program ####

def look_up(dict_):
    """
        Function to look up words into the dictionary
    """
    in_ = input("What is the word?:")
    try:
        out_ = dict_[in_]
        print("--> " + out_)
    except:
        print("Word not found!")
    return 0
        
def list_(dict_):
    """
        Function to print all the words in the dictionary
    """
    print(dict_)

def new_entry(dict_):
    """
        function to input entries into the dictionary
        dictionary is passed by reference
    """
    in_en = input("What is the word?:\n")
    in_de = input("What is the translation?:\n")
    dict_[in_en] = in_de
    
def delete_entry(dict_):
    """
        function to delete words from the dictionary
    """
    in_ = input("What word do you want to delete?\n")
    try:
        del dict_[in_]
    except:
        print("word not found!")




if __name__ == '__main__':
    main()
