import add_machine
import generate_shelves


def main():
    choices = {1: "add_machine", 2: "generate_shelves", 3: "place_machine"}
    print(f"Choices: {choices}")
    choice = int(input("Choose an option: "))
    output = choices[choice]
    print(output)

    if output == "add_machine":
        add_machine.main()
    if output == "generate_shelves":
        generate_shelves.main()
    if output == "place_machine":
        # TODO: Create place_machine() method
        pass


main()
