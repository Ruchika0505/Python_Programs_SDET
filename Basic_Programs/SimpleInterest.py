principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))
simple_interest=(principal * rate * time) / 100
print("Simple Interest {} ".format( simple_interest))