import os

from rich import print as print

import add_machine
import generate_shelves
import place_machine
import search


def make_qr_dirs():
    os.makedirs(name="qr/location", exist_ok=True)
    os.makedirs(name="qr/machine", exist_ok=True)


def main():

    make_qr_dirs()

    choices = {
        1: "Create Shelves",
        2: "Add Machine(s)",
        3: "Place Machine(s)",
        4: "Locate Machine(s)",
    }
    print(f"What would you like to do?: {choices}")
    choice = int(input("Choose an option: "))
    output = choices[choice]

    if output == "Create Shelves":
        generate_shelves.main()
    if output == "Add Machine(s)":
        add_machine.main()
    if output == "Place Machine(s)":
        place_machine.main()
    if output == "Locate Machine(s)":
        search.choose_search_parameter()


main()
