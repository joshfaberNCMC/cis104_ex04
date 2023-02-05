def computePay(hrs,rate):
    try:
        h = float(hrs)
        r = float(rate)
        otRate = r * 0.5
        wage = h * r
        otWage = otRate * (h - 40.0)
        wageTotal = otWage + wage

        if h <= 40.0:
            return wage
            # print('Returning normal pay')
        else:
            return wageTotal
            # print('Returning overtime pay')
    except:
        return 'Error. Please enter numeric input.'


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

pay = computePay(hrs,rate)
print ('Pay',pay)