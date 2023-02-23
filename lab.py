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
            for i in data:
                print("\nPC Number:", i['pc_num'])
                print("Operating System:", i['os'])
                print("PC Status:", i['status'], end="\n\n")

            print("Which PC do you want to access: ")
            nth_pc = int(input())
            if 0 < nth_pc <= len(data):
                pcs = PC(nth_pc)

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
