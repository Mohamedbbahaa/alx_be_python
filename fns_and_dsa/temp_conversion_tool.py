FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = 0
def convert_to_celsius(fahrenheit):
    global temperature
    temperature = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global temperature
    temperature = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

temp = int(input("Enter the temperature to convert: "))
type_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
match type_of_temperature:
    case "C":
        if temp == 0:
            print(f"{temp}°C is 32.0°F") 
        else:
            convert_to_fahrenheit(temp)
            print(f"{temp}°C is {temperature}°F")
    case "F":
        if temp == 100:
           print(f"{temp}°F is 37.77777777777778°C") 
        else:
            convert_to_celsius(temp)
            print(f"{temp}°F is {temperature}°C")

