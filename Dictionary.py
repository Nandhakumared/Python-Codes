# Dict:
#      it has set of unique keys. i.e key should be unique and same value can be given for many keys
#      We use {} for dictionary
#      It is combination of key and values
#      Below in d, 1 is a key and that contains value in it.

d = {1: 'Nandhu', 2: 'Ashok', 3: 'Avinash'}

print(d.__len__())
print(d[1])
# d[4]  #this line will print error
print(d.get(4))  # this will print as none since there is no value or key 4
print(d.get(2))
print(d.get(4, 'Not found'))

name = {1: 'Nandhu', 2: 'Ashok', 3: 'Avinash'}
print(name.keys())  # this will print only keys from dictionary
print(name.values()) # this will print only values from dictionary
# USing Dictionar in LIST
#  To combine list, use dict(zip(var1, var2))

name = ['Ashok', 'Karnesh', 'Aasash', 'Avinash']
area = ['East', 'West', 'North', 'South']
data = dict(zip(name, area))
print(data)
print(data['Ashok'])     # we can pick particular value from data

# Add additional values
data['Nandhu'] = 'Middle'

print(data)

# To delete value

del data['Nandhu']
print(data)

# Using list and dictionary inside Dictionary

item = {'Dog':'large', 'Cat':'small', 'Rat': ['Small', 'Big'], 'Hippo': {'Land':'slow', 'Water':'speed'}, 'Bird':('Tree', 'Forest')}

print(item)
print(item['Dog'])
print(item['Rat'])
print(item['Rat'][1])
print(item['Bird'])
print(item['Bird'][0])
print(item['Hippo']['Land'])
