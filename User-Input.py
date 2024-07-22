'''Int as input'''

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

z = x*y
print(z)

'''str as input'''

ch = input('Enter your Name: ')
print(ch)

'''To print only one str from word by mentioning the index value'''

ch = input('Enter your name: ')[0]
print(ch)

#or

ch =  input('Enter your name: ')
print(ch[1])

#or

ch = input('Enter a string: ')[:3]
print(ch)

'''Evaluation'''
#It will evaluate the expression like 5+6-7*5/3  and give o/p
cal = eval(input('Enter the values: '))
print(cal)