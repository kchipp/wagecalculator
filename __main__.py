def calculateWagesEarned():
    wages = input("Please enter hourly wage")
    try:
        wages=float(wages)
        return wages
    except:
        print ("Please enter a number")
    
def calculateHoursWorked():
    hours = input("Please enter number of hours worked")
    try:
        hours=float(hours)
        return hours
    except:
        print ("Please enter a number")
        
def calculateRegularWeeklyPay(wages, hours):
    if hours <=40:
        pay = wages * hours
    else:
        pay = calculateOvertimePay
    return pay
    
def calculateOvertimePay():
    if hours >40:
        overtimeRate = wages * 1.5
        overtimeAmount = (hours-40) * overtimeRate
        hours = 40
        pay = wages * hours + overtimeAmount
    return pay
    
def main():
    wages = calculateWagesEarned()
    hours = calculateHoursWorked()
    pay = calculateRegularWeeklyPay(wages, hours)
    print pay
    
if __name__ == "__main__":
    main()