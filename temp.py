import json


with open("./temp.json") as file:
    temp = json.load(file)

while True:
    lab_no = input("Lab no:")
    temp.update({
        f"Lab{lab_no}": []
    })
    choice = input("Exit: ")
    if choice == 'e':
        break

while True:
    pc_no = input("PC no:")
    temp['Lab3'].append({
        "pc_no": pc_no
    })
    choice = input("Exit: ")
    if choice == 'e':
        break

with open("./temp.json", "w") as file_update:
    json.dump(temp, file_update, indent=2)

for i in temp:
    print(i)

print('\n')

for i in temp['Lab1']:
    print("PC number: ", i['pc_no'])
