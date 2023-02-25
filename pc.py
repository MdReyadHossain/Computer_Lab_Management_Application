import json


class PC:
    def __init__(self, pc_no, lab_no):
        self.lab_num = lab_no
        self.pc_num = pc_no
        self.pc_os = None
        self.pc_status = None

    def add_pc(self):
        is_lab = False
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

        try:
            while True:
                self.pc_num = int(input("Enter PC number: "))
                for i in data[self.lab_num]:
                    if i['pc_num'] == self.pc_num:
                        is_lab = True

                if not is_lab:
                    break
                elif is_lab:
                    print("PC already exist!")
                    is_lab = False

            self.pc_os = input("Enter installed OS: ")
            self.pc_status = input("Enter status: ")
        except:
            print("Invalid Input!")
            self.add_pc()

        data[self.lab_num].append({
            "pc_num": self.pc_num,
            "os": self.pc_os,
            "status": self.pc_status
        })

        with open(f"./Labs/Lab.json", "w") as file_update:
            json.dump(data, file_update, indent=2)

    def access_pc(self):
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

            for i in data[self.lab_num]:
                if i['pc_num'] == self.pc_num:
                    print("Selected PC:")
                    print("\tPC Number:", i['pc_num'])
                    print("\tOperating System:", i['os'])
                    print("\tPC Status:", i['status'], end="\n\n")

    def update_pc(self, choice, pc_key):
        self.pc_os = pc_key
        self.pc_status = pc_key

        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

            for i in data[self.lab_num]:
                if i['pc_num'] == self.pc_num:
                    if choice == '1':
                        i['os'] = self.pc_os
                        with open(f"./Labs/Lab.json", "w") as file_update:
                            json.dump(data, file_update, indent=2)

                    elif choice == '2':
                        i['status'] = self.pc_status
                        with open(f"./Labs/Lab.json", "w") as file_update:
                            json.dump(data, file_update, indent=2)

    def delete_pc(self):
        with open(f"./Labs/Lab.json") as file:
            data = json.load(file)

        for num, i in enumerate(data[self.lab_num]):
            if i['pc_num'] == self.pc_num:
                data[self.lab_num].pop(num)
                break

        with open(f"./Labs/Lab.json", "w") as file_update:
            json.dump(data, file_update, indent=2)
