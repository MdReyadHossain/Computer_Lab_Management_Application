import json


class PC:
    def __init__(self, pc_no, lab_no):
        self.lab_num = lab_no
        self.pc_num = pc_no
        self.pc_os = None
        self.pc_status = None

    def add_pc(self):
        is_lab = False
        with open(f"./Labs/Lab{self.lab_num}.json") as file:
            data = json.load(file)

        try:
            while True:
                self.pc_num = int(input("Enter PC number: "))
                for i in data:
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

        data.append({
            "pc_num": self.pc_num,
            "os": self.pc_os,
            "status": self.pc_status
        })

        with open(f"./Labs/Lab{self.lab_num}.json", "w") as file_update:
            json.dump(data, file_update)

    def access_pc(self):
        with open(f"./Labs/Lab{self.lab_num}.json") as file:
            data = json.load(file)
            for i in data:
                if i['pc_num'] == self.pc_num:
                    print("\nPC Number:", i['pc_num'])
                    print("Operating System:", i['os'])
                    print("PC Status:", i['status'], end="\n\n")

    def update_pc(self, choice, pc_key):
        self.pc_os = pc_key
        self.pc_status = pc_key

        with open(f"./Labs/Lab{self.lab_num}.json") as file:
            data = json.load(file)

            for i in data:
                if i['pc_num'] == self.pc_num:
                    if choice == '1':
                        i['os'] = self.pc_os
                        with open(f"./Labs/Lab{self.lab_num}.json", "w") as file_update:
                            json.dump(data, file_update)

                    elif choice == '2':
                        i['status'] = self.pc_status
                        with open(f"./Labs/Lab{self.lab_num}.json", "w") as file_update:
                            json.dump(data, file_update)

    def delete_pc(self):
        with open(f"./Labs/Lab{self.lab_num}.json") as file:
            data = json.load(file)

        for num, i in enumerate(data):
            if i['pc_num'] == self.pc_num:
                data.pop(num)
                break

        with open(f"./Labs/Lab{self.lab_num}.json", "w") as file_update:
            json.dump(data, file_update)
