def numMax(num1,num2,num3):
    fNum1 = float(num1)
    fNum2 = float(num2)
    fNum3 = float(num3)

    max3 = max(fNum1,fNum2,fNum3)
    return max3


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
num3 = input('Enter third number: ')

try:
    max = numMax(num1,num2,num3)
    print(max)
except:
    print('Please enter a numeric value.')