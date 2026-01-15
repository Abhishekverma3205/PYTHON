#take a temperature input from user and print whether its hot, warm or cold
temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 35:
    print("It's hot.")
elif temperature < 21:
    print("It's cold .")

else:
    print("It's warm.")
