FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


while True:
    temperature = int(input("Enter the temperature to convert:"))
    specify = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if specify == 'C':
        print(convert_to_fahrenheit(temperature))
        break
    elif specify == 'F':
        print(convert_to_celsius(temperature))
        break
    else:
        print("invalid input")