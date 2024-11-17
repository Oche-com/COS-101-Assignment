# Display the menu
print("COS101 Assignment")
print("Mathematics Formula Calculator")
print("Name of Functions")
print("Choose one of the following options and then provide the values:")
print("A: Calculate Compound Interest (CI = principal * 1 + rate/100*n*time)")
print("B: Calculate Celsius to Fahrenheit (fahrenheit = celsius * 9/5 + 32)")
print("C: Calculate Simple Interest (SI = principal * rate * time) / 100)")
print("D: Calculate Area Of a Circle (Pi.r.2 = 3.142* radius * 2)")
print("E: Calculate Fahrenheit to Celsius (C = fahrenheit - 32) * 5/9)")
# Get the user's choice
choice = input("Enter the formular you want to use and then select it (A, B, C, D, E): ").strip().upper()
# Perform the appropriate calculation based on the user's choice
if choice == "A":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))
    n = float(input("Enter the number of times interest is compounded per year: "))
    amount = principal * (1 + rate/(100*n))**(n*time)
    compound_interest = amount - principal
    print("The compound interest is:", compound_interest)
elif choice == "B":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == "C":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))
    simple_interest = (principal * rate * time) / 100
    print("The simple interest is:", simple_interest)
elif choice == "D":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.142* radius * 2
    print("The area of the circle is:", area)
elif choice == "E":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid choice. Please select A, B, C, D, or E.")