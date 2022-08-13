for item in "Learning Python":
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in {1,2,3,4,5,1,2,3,4}:
    print(item)

for item in (1,2,3,4,5):
    print(item)

for  item in [1,2,3,4,5]:
    for x  in [ 'a','b']:
        print(x, item)

user ={
    "name" : "Jagroop",
    "age": 20,
    "can_swim" : False
}

for items in user.items():
    print(items)

for items in user.values():
    print(items)

for item in user.keys():
    print(item)

for key,value  in user.items():
    print(key, value)