users = {
    'id' : 1,
    'name' : 'Leanne Graham',
    'username' : 'Bret',
    'email' : 'Sincere@april.biz',
    'address' : {
        'street' : 'Kulas Light',
        'suite' : "Apt. 556",
        'city' : "Gwenborough",
        'zipcode' : "92998-3874",
            'geo' : {
                'lang' : '-37.3159',
                'long' : '81.1496'
            }
            }
}

print(users)
print(users['name'])
print(users['address']['street'])
print(users['address']['geo'])
print(users['address']['geo']['lang'])
print(users['address']['geo']['long'])


print(users)
print(type(users))
print('\nUbah Dict ke json')
import json
result = json.dumps(users)
print(type(result))
print(result)

# menulis ke file hasil dump json, beda antara json.dumps dengan json.dump -> tanpa s
with open('result.json', 'w') as file:
    json.dump(users, file)
