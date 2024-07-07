CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


while True:
    temperature = int(input("Enter the temperature to convert:"))
    specify = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if specify == 'C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        break
    elif specify == 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        break
    else:
        print("Invalid temperature. Please enter a numeric value.")