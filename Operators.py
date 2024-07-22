'''Operators'''

''' Arithmetic'''
x = 5
y = 2
print(x+y)
print(x-y)
print(y-x)
print(x/y)
print(x*y)
print(x % y)

'''Assignment'''
x, y = 5,6
print(x)
print(y)

x += 2  #here there shouyld not be any space b/w operators
print(x)

x *= 3
print(x)

x -= y + 8
print(x)

'''UNARY OPERATOR'''
n = 5
print(-n)
                  # here we just assigning variable as negative.
n = -n
print(n)

'''Relational Operator'''
a = 4
b = 2
print(a > b)
print(a < b)
print(a == b)      # here == is used to compare two variables
print(a != b)

'''Logical'''

a = 6
n = 7

print(a > n and n < a)
print(a > 2 and n < 11)
print(a > 8 and n < 1)  # 'and' will check if any condition is false it will print that false condition as False
print(a > 8 or n > 2)   # 'or' will check if any condition is true then it will print that true condtion as true

a = True    # Assigning variables logical condition
print(a)
print(not[a])
