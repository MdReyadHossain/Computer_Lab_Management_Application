import json
import time
from lab import Lab
from pc import PC


def lab_access_choice():
    is_valid = False
    try:
        while True:
            with open('./Labs/Lab.json') as file_obj:
                data = json.load(file_obj)
            nth_lab = (input("\n<-Enter 0 to go back.\nWhich lab do you want to access: "))
            if nth_lab == "0":
                lab_choice()
            for i in data:
                if i == nth_lab:
                    labs = Lab(nth_lab)
                    pcs = PC(0, nth_lab)
                    print("1. Add a PC to this lab.")
                    print("2. Access this lab.")
                    choice = input("Enter your choice: ")

                    # --------- Adding a PC ---------
                    if choice == '1':
                        pcs.add_pc()
                        print("\nPC Added Successfully!\n")

                    # --------- Access a Lab ---------
                    elif choice == '2':
                        labs.access_lab()

                    else:
                        print("Invalid Input!")
                        lab_access_choice()
                    is_valid = True
                    break

            if is_valid:
                break
            else:
                print("\nLab does not exist!\n")
                is_valid = False
    except:
        print("Entered wrong choice! Try again")
        lab_access_choice()


def delete_lab_choice():
    is_valid = False
    try:
        while True:
            with open('./Labs/Lab.json') as file_obj:
                data = json.load(file_obj)
            nth_lab = (input("\n<-Enter 0 to go back.\nWhich lab do you want to DELETE: "))
            for i in data:
                if i == nth_lab:
                    labs = Lab(nth_lab)
                    labs.delete_lab()
                    is_valid = True
                    break
            if is_valid:
                break
            else:
                print("\nLab does not exist!\n")
                is_valid = False
    except:
        print("Entered wrong choice! Try again")
        lab_access_choice()


def lab_choice():
    with open('./Labs/Lab.json') as file_obj:
        data = json.load(file_obj)
    print(f"Total Lab in the institute: {len(data)}\n")

    if len(data) > 0:
        print("Existing Labs:\n\t-> ", end="")
        for i in data:
            print(f"Lab-{i} | ", end="")
    else:
        print("No lab registered yet.")

    print("\n")
    print("\n1. Access a lab.")
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
