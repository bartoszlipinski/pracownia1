import json

with open('students.json')as f:
    data = json.loads(f.read())
    limited = []
    for row in data:
        limited.append({'id': row['id'], 'name': row['name'], 'surname': row['surname']})

    with open('limited.json', 'w') as f2:
        f2.write(json.dumps(limited))