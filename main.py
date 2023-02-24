import json
import time
from lab import Lab
from pc import PC

with open('TotalLab.json') as file_obj:
    data = json.load(file_obj)


def lab_access_choice():
    print("*Enter 0 to go back\n->Which lab do you want to access: ")
    # try:
    nth_lab = int(input())
    if 0 < nth_lab <= data['total_lab']:
        labs = Lab(nth_lab)
        pcs = PC(0, nth_lab)
        print("1. Update PC status.")
        print("3. Delete the PC.")
        labs.access_lab()
    elif nth_lab == 0:
        lab_choice()
    else:
        print("No lab found! Try again")
        lab_access_choice()
    # except:
    #     print("Entered wrong choice! Try again")
    #     lab_access_choice()


def delete_lab_choice():
    print("*Enter 0 to go back\n->Which lab do you want to Delete: ")
    try:
        nth_lab = int(input())
        if 0 < nth_lab <= data['total_lab']:
            labs = Lab(nth_lab)
            labs.delete_lab()
        elif nth_lab == 0:
            lab_choice()
        else:
            print("No lab found! Try again")
            lab_access_choice()
    except:
        print("Entered wrong choice! Try again")
        lab_access_choice()


def lab_choice():
    print(f"Total Lab in the institute: {data['total_lab']}")
    print("1. Access a lab.")
    print("2. Add a lab.")
    print("3. Delete a lab.")
    print("4. Quit")

    choice = input(f"Enter your choice: ")
    if choice == '1':
        lab_access_choice()

    elif choice == '2':
        labs = Lab(0)
        labs.add_lab()

    elif choice == '3':
        delete_lab_choice()

    elif choice == '4':
        return 4

    else:
        print("Invalid choice. Please try again.")


def main():
    print("Welcome to Computer Lab Management Application")

    while True:
        valid = lab_choice()
        if valid == 4:
            break

    print("Turning off...")
    time.sleep(1)
    print("Goodbye!")

    # while True:
    #     print("1. Add a new PC")
    #     print("2. Update information of an existing PC")
    #     print("3. Remove an existing PC")
    #     print("4. Display information about all the PCs")
    #     print("5. Display all information of a PC")
    #     print("6. Search for a particular PC and display the information")
    #     print("7. Store all the PC available in the application into a text file")
    #     print("8. Quit")
    #
    #     choice = input(f"Enter your choice: ")


if __name__ == "__main__":
    main()
