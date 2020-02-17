import json
with open("users.json") as file_txt:
    file=json.load(file_txt)
    print (type(file))
    users1=file["users"]
index=0
while index<len(users1):
    print("users first name",users1[index]["firstName"])
    print("users last name",users1[index]["lastName"])
    print("users address",users1[index]["details"]["City"])
    print("users age",str(users1[index]["details"]["age"]))
    print("users mobile no",str(users1[index]["details"]["mobileNo"]))
    index=index+1