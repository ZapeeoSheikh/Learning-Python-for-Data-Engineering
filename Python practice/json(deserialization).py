import json

person = {"name" : "Rameez", "username" : "ZapeeoSheikh", "fullname" : ["Muhammad", "Rameez"], "rollno" : 90, "isGraduated" : False}

PersonEncode = json.dumps(person, indent=4)
print(PersonEncode)

# open into another file ( json encode )
# with open('openedfile.json', 'w') as file:
#     json.dump(person, file)

# lets deocode it in the other file
personn = json.loads(PersonEncode)


with open('person.json', 'r') as file:
   personnn = json.load(file)
   print(personnn)
