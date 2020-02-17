obj={"availableCourses":[{"id":14,
                        "name":"GIT101 - Learning GIT",
                        "type":"js",
                        "logo":"https://tcrn.ch/2Kd0xvh",
                        "shortDescription":"Learning Basics of using GIT",
                        "sequenceNum":7},
                        {"id":15,
                        "name":"Introduction to HTML",
                        "type":"html",
                        "logo":"https://bit.ly/2FufxWZ",
                        "shortDescription":"Learn how to use HTML to build simple web pages :)",
                        "sequenceNum":11},
                        {"id":16,
                        "name":"Introduction to CSS",
                        "type":"html",
                        "logo":"https://bit.ly/2BfcwWh",
                        "shortDescription":"Learn how to use CSS to add styles to simple web pages :)",
                        "sequenceNum":13} 
                        ]} 

# # 1.Find all availableCourses courses?
# # 2.find all id from availableCourses courses?
# # 3.take userinput from user accoring to print details of the id?
# # 4.print all name from courses?
# # 5.print name according to userinput which will be gaven by user?


obj1=obj["availableCourses"]
i=0
while i<len(obj1):
    print("id",obj1[i]["id"])
    print("name",obj1[i]["name"])
    print("type",obj1[i]["type"])
    print("logo",obj1[i]["logo"])
    print("shortDescription",obj1[i]["shortDescription"])
    print("sequenceNum",obj1[i]["sequenceNum"])
    i=i+1

obj1=obj["availableCourses"]
i=0
while i<len(obj1):
    print ("id",obj1[i]["id"])
    i=i+1


obj1=obj["availableCourses"]
i=0
while i<len(obj1):
    print("name",obj1[i]["name"])
    i=i+1
obj1=obj["availableCourses"]
for i in obj1:
        user=input("enter your id  \n")
        if user==i["id"]:
                print (i)



obj1=obj["availableCourses"]
for i in obj1:
        print (i["name"] )

obj1=obj["availableCourses"]
i=0
while i<len(obj1):
        user=input("enter your number \n")
        if obj1[i]["id"]==user:
                print (obj1[i])
        i=i+1  
