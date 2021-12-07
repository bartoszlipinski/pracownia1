import json

student = {
    'name': 'John',
    'surname': 'Doe',
    'age': 17,
    'fieldOfStudy': 'Computer Science',
    'vaccinated': True,
}

with open('student.json', "w") as f:
    f.write(json.dumps(student))