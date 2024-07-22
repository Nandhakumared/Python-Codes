'''Swap numbers'''

a = 7
b = 8

#Using 3rd variable temp;
temp = a
a = b
b = temp
print(a)
print(b)

# without using 3rd variable temp: # here it will take extra bits
a = 2
b = 5

a = a + b
b = a - b
a = a - b
print(a)
print(b)

# using XOR operator  :  This XOR wil not use extra bits
a = 16
b = 10

a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)

# single line method
a,b = 5,6
a,b = b,a
print(a)
print(b)
print(a,b)
