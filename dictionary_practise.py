obj = {"name":"Ram","RollNo":12,
        "marks":[{"Maths":50,
        "English":49,
        "scie":79}],
        "teacher":{"Maths":"mr rama",
                "english":"ms komal"
        }
    }
# print (obj)
# print (maths teacher name and marks)
# print (teacher)
# print (name and rollno)
# print (marks)
# print (max and min marks)

# ----------------------------
# print marks 
obj1=obj["marks"]
i=0 
while i<len(obj1):
        print (obj1[i]["Maths"])
        print (obj1[i]["English"])
        print (obj1[i]["scie"])
        i=i+1

#------------------------------
#print maths teacher name
obj2=obj["teacher"]
print (obj2["Maths"])

#--------------------
# print teacher 
teacher1=obj["teacher"]
i=0
while i<len(teacher1):
        print (teacher1["Maths"])
        print (teacher1["english"])
        i=i+1

#------------------
# print (name and roll no)
print (obj["name"])
print (obj["RollNo"])

#-----------------
# print marks
obj2=obj["marks"]
i=0
while i<len(obj2):
        print (obj2[i]["Maths"])
        print (obj2[i]["English"])
        print (obj2[i]["scie"])
        i=i+1

#--------------------
# print max and min marks
a={"neha":12,"aman":10,"saral":67,"rakesh":45}
b=a.values()
print (b)
b.sort()
print (b)
length=len(b)-1
index=length-1 
while length>index:
        print (b[length])
        length=length-1

# print min marks
a={"neha":12,"aman":10,"saral":67,"rakesh":45}
b=a.values()
b.sort(reverse=True)
print (b)
length=len(b)-1 
index=length-1
while length>index:
        print (b[length])
        length=length-1
