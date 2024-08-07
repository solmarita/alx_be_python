FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

while True:

    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if isnumeric(temp):
        if unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
            break

        if unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
            break
    else:
        print("Invalid temperature. Please enter a numeric value.")

