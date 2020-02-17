import json
with open("users.json") as file_txt:
    file=json.load(file_txt)
    print(file)


with open('data.json', 'w') as outfile:
    json.dump(file,outfile)

