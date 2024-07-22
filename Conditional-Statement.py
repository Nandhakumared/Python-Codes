'''Conditional Statements'''

'''IF Statement'''
# x = int(input("Enter number: "))
# if x == 10:      # Here if x is equal to 10 then it will print the print stmt inside if.
#     print("Expected Result")
# print("Enter correct value")

'''IF ELSE Statement'''
# x = int(input("enter number: "))
# y = int(input("Enter number: "))
# if x > y:
#     print("True")
# else:
#     print("False")

'''NESTED IF ELSE Statement'''
# x = int(input("Enter number: "))
# y = int(input("Enter number: "))
# z = x + y
# if z % 2 == 0:           # here if this stmt is true thn only nested if else stmt work. t
#     print("Z is Even")   # i.e if the stmt is true, thn it performs nested if condition.
#     if z > 5:            # If condition is false it got to else stmt.
#         print("z is greater  than 5")
#     else:
#         print("z is less than 6")
# else:             # if in this else stmt if we have nested if else condition thn it will perform nested if else in else condition
#     print("Z is odd")
#     if z > 5:
#         print("z is greater  than 5")
#     else:
#         print("z is less than 6")

'''IF ELIF ELSE Statement'''
# Here the i/p will be checked with each condition 1 by 1 in sequence. If any one of the condition is true,
# thn it will skip remaining conditions. i.e if two condition are same with diff o/p thn it will take 1st occurence and
# skip remaining occurence which has same condition. It just execute the first occurence.
x = int(input("Enter number: "))

if x == 1:
    print("Sunday")
    if x == 1:    # just implimented nested if else
        print("Have a wonderful Sunday")
elif x == 2:
    print("Monday")
elif x == 3:
    print("Tuesday")
elif x == 4:
    print("Wednesday")
elif x == 5:
    print("Thursday")
elif x == 6:
    print("Friday")
elif x == 7:
    print("Saturday")
elif x == 7:
    print("it will not print")
else:
    print("It's not a weekday")