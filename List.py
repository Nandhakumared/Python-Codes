'''List '''
# LIST:
#     In list we can able to chnage the values.
#     List in mutable. if needed we can add values in between.
#     [] is used here.
#     In list we can multiple values.



name = ["ashok", "karnesh", "aravindh", "avinash", "aakash"]
place = [11, 2, 43, 64, 25]

ninjas = [name, place]
place [1] = 5                     # here we replace the value 2 to 5
place.append(6)
place.insert(6,7)
name.append("nandhu")
print(ninjas)
print(max(place))
print(min(place))
print(name[0:1])
place.sort()
print(place)

del place[3:]
print(place)

print(type(place))

