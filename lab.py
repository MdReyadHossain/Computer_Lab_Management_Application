import json


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

        else:
            print("No PC(s) registered in this lab.\n")

