student={"name":"Anu","age":20,"grade":"A"}
print(student)
#Common dictionary operations
#Access value by key,dict[key]
print(student["name"])
#Get value safely, .get()
print(student.get("age"))
#Add/Update
student["age"]=21    #update
student["city"]="Delhi"    #add new
print(student)
#Remove element
student.pop("age")
print(student)
#Remove last inserted item, .popitem()
student.popitem()
print(student)
#Delete key or whole dictionary, del
del student["grade"]    #delete specific key
print(student)  
del student       #delete entire dictionary 
#Clear all, .clear()
student.clear()
print(student)
#View all keys
print(student.keys())
#View all value
print(student.values())
#View all items
print(student.items())