import json


class PC:
    def __init__(self, number, os, status):
        self.number = number
        self.os = os
        self.status = status


class Lab:
    def __init__(self):
        self.pcs = []

    def add_pc(self, pc):
        self.pcs.append(pc)

    def update_pc(self, number, os, status):
        for pc in self.pcs:
            if pc.number == number:
                pc.os = os
                pc.status = status

    def remove_pc(self, number):
        for pc in self.pcs:
            if pc.number == number:
                self.pcs.remove(pc)

    def display_all_pcs(self):
        for pc in self.pcs:
            print(f"PC number: {pc.number}, OS: {pc.os}, Status: {pc.status}")

    def display_pc(self, number):
        for pc in self.pcs:
            if pc.number == number:
                print(f"PC number: {pc.number}, OS: {pc.os}, Status: {pc.status}")

    def search_pc(self, number):
        found = False
        for pc in self.pcs:
            if pc.number == number:
                print(f"PC number: {pc.number}, OS: {pc.os}, Status: {pc.status}")
                found = True
        if not found:
            print("PC not found. Do you want to add it?")
            choice = input("Enter Y to add, N to cancel: ")
            if choice.lower() == "y":
                os = input("Enter OS: ")
                status = input("Enter status: ")
                self.add_pc(PC(number, os, status))

    def check_duplicate_pc(self, number):
        for pc in self.pcs:
            if pc.number == number:
                print("This PC number already exists.")
                choice = input("Enter M to modify, R to remove, N to cancel: ")
                if choice.lower() == "m":
                    os = input("Enter new OS: ")
                    status = input("Enter new status: ")
                    self.update_pc(number, os, status)
                elif choice.lower() == "r":
                    self.remove_pc(number)
                else:
                    return
                break
            else:
                print("PC Is Unique.")
                break

    def store_pcs(self, filename):
        with open(filename, "w") as f:
            json.dump([pc.__dict__ for pc in self.pcs], f)

    def load_pcs(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.pcs = [PC(**pc) for pc in data]

# Example usage
lab = Lab()
print("1. Add PC\n2. Display All PC\n3. Search PC\n4. Check Duplicate\n5. Store\n6. Quit")

while True:
    check = input("Enter an option: ")
    print("User selected option", check)
    if check == '1':
        lab.add_pc(PC(1, "Windows", "Available"))
        lab.add_pc(PC(2, "Linux", "In use"))
        lab.add_pc(PC(3, "Linux", "Unavailable"))
    elif check == '2':
        lab.display_all_pcs()
    elif check == '3':
        lab.search_pc(3)
    elif check == '4':
        lab.check_duplicate_pc(4)
    elif check == '5':
        lab.store_pcs("pcs.json")
        lab.load_pcs("pcs.json")
    else:
        quit()