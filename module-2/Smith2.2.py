# This function converts Fahrenheit to Celsius.
def fahrentheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Store a temperature in Fahrenheit.
temperature_f = 68

# Call the function and store the converted temperature.
temperature_c = fahrentheit_to_celsius(temperature_f)

# Display the result.
print("Temperature in Celsius:", temperature_c)