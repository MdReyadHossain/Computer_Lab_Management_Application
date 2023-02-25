import json
import os

from pc import PC

# with open('TotalLab.json') as file_obj:
#     total_lab = json.load(file_obj)


class Lab:
    def __init__(self, lab_no):
        self.lab_num = lab_no

    def access_lab(self):
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

        if len(data[self.lab_num]) > 0:
            print(f"\nLab{self.lab_num}:")
            for i in data[self.lab_num]:
                print(f"\tPC Number:", i['pc_num'])
                print("\tOperating System:", i['os'])
                print("\tPC Status:", i['status'], end="\n\n")

            # Access PC  --------
            is_valid = False
            while True:
                nth_pc = int(input("Which PC do you want to access(Press 0 to go back): "))
                if nth_pc == 0:
                    break
                for i in data[self.lab_num]:
                    if i['pc_num'] == nth_pc:
                        pcs = PC(nth_pc, self.lab_num)
                        pcs.access_pc()
                        print("\nUpdate this PC?\n1. Set Operating System.")
                        print("2. Update PC status.")
                        print("3. Delete the PC.")
                        print("0. Go Back.")
                        choice = input(f"Enter your choice: ")
                        if choice == '1':
                            pc_os = input(f"Enter Current OS for this PC: ")
                            pcs.update_pc(choice, pc_os)

                        elif choice == '2':
                            pc_stat = input(f"Update status for this PC: ")
                            pcs.update_pc(choice, pc_stat)
                            print("PC information updated!")

                        elif choice == '3':
                            pcs.delete_pc()
                            print(f"PC{nth_pc} has been deleted!")

                        elif choice == '0':
                            self.access_lab()

                        else:
                            print("Invalid choice entered!")
                            self.access_lab()
                        is_valid = True
                        break

                if is_valid:
                    break
                else:
                    print("\nPC does not exist!\n")
                    is_valid = False
        else:
            print("No PC(s) registered in this lab.\n")

    def add_lab(self):
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

        is_valid = True
        while True:
            self.lab_num = input("Enter lab number: ")
            for i in data:
                if i == self.lab_num:
                    print("\nLab already not exist!")
                    is_valid = False
                    break

            if is_valid:
                break
            else:
                is_valid = True

        data.update({
            f"{self.lab_num}": []
        })

        with open(f"./Labs/Lab.json", "w") as file_update:
            json.dump(data, file_update, indent=2)

        print("Lab added!")

    def delete_lab(self):
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

        del data[self.lab_num]

        print(f"Lab {self.lab_num} has been deleted!")

        with open(f"./Labs/Lab.json", "w") as file_update:
            json.dump(data, file_update, indent=2)
