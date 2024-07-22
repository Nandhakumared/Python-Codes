'''Bitwise Operator'''

'''Compliment'''
a = ~13      # Take binary value of 13 and reverse it.
print(a)     # And take outputs binary value, reverse it then add reversed outputs binary value with 1.
             # Now Compare both reversed values.


'''Bitwise AND(&), OR(|), XOR(^)'''
# Here it will do AND & OR operation using binary values of a and b and gives output.
# The output will be diff i.e based on the binary value we got.
# Eg: if binary value 'a' is 00001101 and binary value fo 'b' is 11001101 => out will be 11001101
#  00001101
#  11001101
#  11001101       => here we used AND. similarly for OR and XOR

a = 12
b = 13
print(a & b)
print(a|b)
print(a^b)

'''LEFT(<<) and RIGHT Shift(>>)'''
# Here it take binary value of 'a'
# For Left shift it will add two zero (or no.of value as we give) at end of binary value and convert it to calculate the decimal values.
#For Right shift it will add two zeros(or no.of value as we give) at begining of binary value and last two number will be removed and  convert it to calculate the decimal values.

a = 10
print(a<<2)
print(a>>2)
