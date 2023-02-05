hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
otRate = r * 0.5
wage = h * r
otWage = otRate * (h - 40.0)
wageTotal = otWage + wage


if h <= 40.0:
    # print('Standard Pay:', wage)
    print(wage)
else:
    # print('Standard Pay:', wage)
    # print('Overtime Pay:', otWage)
    # print('Total Pay:', wageTotal)
    print(wageTotal)