# a = 1.5
# b = 1
# print(int(a))
# print(complex(b))
# print(float(b))
# print(type(b))

# c = 5
# d = c
# print(d)
#
# c = 6
# print(d)
# print(c)
# range(5)
# print(list(range(5))) #This will print number from 0 to 4
#
# print(list(range(1,6,2))) #this will print only odd numbers i.e 1 is starting index value, 6 is to spcify place and 2 is difference b/w values
# print(list(range(2,6,2))) #this will display even values

'''To print keys and values alone'''
name = {1: 'Nandhu', 2: 'Ashok', 3: 'Avinash'}
print(name.keys())
print(name.values())
print(name.copy())
print(name.get(2)) # this get and below are same
print(name[3])