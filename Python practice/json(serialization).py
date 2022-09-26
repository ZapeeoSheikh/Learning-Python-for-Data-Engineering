# Json decode (Serialization)
import json
person = {"name" : "Rameez", "username" : "ZapeeoSheikh", "fullname" : ["Muhammad", "Rameez"], "rollno" : 90, "isGraduated" : False}

PersonJson = json.dumps(person, indent=4, separators=(': ','= '))

print(PersonJson)

with open('person.json','w') as file:
    json.dump(person, file, indent=4)
