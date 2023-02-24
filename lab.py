import json
import os

from pc import PC

with open('TotalLab.json') as file_obj:
    total_lab = json.load(file_obj)


class Lab:
    def __init__(self, lab_no):
        self.lab_num = lab_no

    def access_lab(self):
        with open(f"./Labs/Lab{self.lab_num}.json") as file:
            data = json.load(file)

        if len(data) > 0:
            print(f"\nLab{self.lab_num}:")
            for i in data:
                print(f"\tPC Number:", i['pc_num'])
                print("\tOperating System:", i['os'])
                print("\tPC Status:", i['status'], end="\n\n")

        # Access PC  --------
            nth_pc = int(input("Which PC do you want to access(Press 0 to go back): "))
            if 0 < nth_pc <= len(data):
                pcs = PC(nth_pc, self.lab_num)
                pcs.access_pc()
                print("\nUpdate this PC?\n1. Set Operating System.")
                print("2. Update PC status.")
                print("3. Delete the PC.")
                print("0. Go Back.")
                choice = input(f"Enter your choice: ")
                if choice == '1':
                    pc_os = input(f"Update OS for this PC: ")
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

            elif nth_pc == 0:
                pass

            else:
                print("Invalid PC number entered!")
                self.access_lab()
        else:
            print("No PC(s) registered in this lab.\n")

    def add_lab(self):
        data = []
        lab_name = f"Lab{total_lab['total_lab']+1}.json"
        with open(f"./Labs/{lab_name}", 'x') as file:
            json.dump(data, file)

        total_lab['total_lab'] = total_lab['total_lab']+1
        with open('TotalLab.json', 'w') as file:
            json.dump(total_lab, file)

        print("Lab added!")

    def delete_lab(self):
        filename = f"./Labs/Lab{self.lab_num}.json"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"\nLab{self.lab_num} has been deleted!")

        else:
            print("No lab found\n")

        total_lab['total_lab'] = total_lab['total_lab'] - 1
        with open('TotalLab.json', 'w') as file:
            json.dump(total_lab, file)
