import json

with open('eur.json') as f:
    data = json.loads(f.read())
    print(f'Date         Buying Rate   Selling Rate')
    print('=======================================')
    for row in data['rates']:
        if len(str(row['bid'])) == 6:
            print(f'{row["effectiveDate"]}   {row["bid"]}        {row["ask"]}')
        else:
            print(f'{row["effectiveDate"]}   {row["bid"]}         {row["ask"]}')