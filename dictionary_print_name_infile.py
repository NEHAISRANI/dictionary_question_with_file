# import json
# with open("dictionary_print_name_infile.json","r") as file_txt:
#     file=file_txt.read()
#     print (type(file))
#     b=json.loads(file)
#     print (type(b))
#     print (b)
#     c=b["availableCourses"]
#     print (c)
#     i=0
#     while i<len(c):
#         print (c[i]["id"])
#         print (c[i]["name"])
#         print (c[i]["type"])
#         print (c[i]["logo"])
#         print (c[i]["sequenceNum"])
#         i=i+1



# without read function
# import json
# with open("dictionary_print_name_infile.txt") as file_txt:
#     file=json.load(file_txt)
#     print (type(file))
#     b=file["availableCourses"]
#     i=0
#     while i<len(b):
#         print b[i]["id"]
#         print b[i]["name"]
#         print b[i]["type"]
#         print b[i]["logo"]
#         print b[i]["sequenceNum"]
#         i=i+1
