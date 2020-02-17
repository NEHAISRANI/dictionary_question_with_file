#with read function

# import json
# with open("dict.txt","r") as file_txt:
#     file=file_txt.read()
#     print type(file)
#     c=json.loads(file)
#     print type(c) 
#     b=c["users"]
#     print c 
# i=0
# while i<len(b):
#     print b[i]["firstName"]
#     print b[i]["lastName"]
#     print b[i]["details"]["age"]
#     print b[i]["details"]["mobileNo"]
#     print b[i]["details"]["City"] 
#     i=i+1 


#--------------------
#without read function

import json
with open("dict.json") as file_txt:
    file=json.load(file_txt)
    print type(file)
b=file["users"]
print b
# i=0
# while i<len(b):
#     print b[i]["firstName"]
#     print b[i]["lastName"]
#     print b[i]["details"]["age"]
#     print b[i]["details"]["mobileNo"]
#     print b[i]["details"]["City"] 
#     i=i+1 

for i in b:
    print i["firstName"]
    print i["lastName"]
    print i["details"]["age"]
    print i["details"]["mobileNo"]
    print i["details"]["City"] 