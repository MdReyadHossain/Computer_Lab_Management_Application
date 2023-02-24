import json
import time
from lab import Lab
from pc import PC

with open('TotalLab.json') as file_obj:
    data = json.load(file_obj)


def lab_access_choice():
    print("\n*Enter 0 to go back\n->Which lab do you want to access: ")
    try:
        nth_lab = int(input())
        if 0 < nth_lab <= data['total_lab']:
            labs = Lab(nth_lab)
            pcs = PC(0, nth_lab)
            print("1. Add a PC to this lab.")
            print("2. Access this lab.")
            choice = input("Enter your choice: ")
            if choice == '1':
                pcs.add_pc()
                print("\nPC Added Successfully!\n")

            elif choice == '2':
                labs.access_lab()

            else:
                print("Invalid Input!")
                lab_access_choice()

        elif nth_lab == 0:
            lab_choice()
        else:
            print("No lab found! Try again")
            lab_access_choice()
    except:
        print("Entered wrong choice! Try again")
        lab_access_choice()


def delete_lab_choice():
    print("\n*Enter 0 to go back\n->Which lab do you want to Delete: ")
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
    print(f"\nTotal Lab in the institute: {data['total_lab']}")
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
    print("\n-----Welcome to Computer Lab Management Application-----\n")

    while True:
        valid = lab_choice()
        if valid == 4:
            break

    print("Turning off...")
    time.sleep(1)
    print("Goodbye!")


if __name__ == "__main__":
    main()
