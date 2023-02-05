hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
    otRate = r * 0.5
    wage = h * r
    otWage = otRate * (h - 40.0)
    wageTotal = otWage + wage

    if h <= 40.0:
        # print('Standard Pay:', wage)
        print(wage)
    else: 
        h > 40.0
        # print('Standard Pay:', wage)
        # print('Overtime Pay:', otWage)
        # print('Total Pay:', wageTotal)
        print(wageTotal)
except:
    print('Error. Please enter numeric input.')