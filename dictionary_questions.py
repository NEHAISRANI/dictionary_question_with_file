obj = {"name":"Ram","RollNo":12,
    "marks":[{"Maths1":50,
            "English1":49,
            "scie1":79,
            "teacher":{
                "Maths":"mr rama",
                "English":"ms komal",
                "scie":45
                }
            }, 
            {
            "names1":{
                "Math":78,
                "Englishs":123,
                "science":34} 
            }    
        ] 
}
obj1=obj["marks"] 
print (obj)
i=0
print (obj1[i]["Maths1"])
print (obj1[i]["English1"])
print (obj1[i]["scie1"])
print (obj1[i]["teacher"]["Maths"])
print (obj1[i]["teacher"]["English"])
print (obj1[i]["teacher"]["scie"])
print (obj["name"])
print (type(obj))

