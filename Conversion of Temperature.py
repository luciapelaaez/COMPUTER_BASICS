print ("I'm going to convert a temperature in degrees Celsius to degrees Fahrenheit.")
celsius = float(input ("Please give me a temperature in degrees Celsius."))
print ("The temperature you gave me is:", celsius)
def conversion(celsius):
    resultado = celsius*9/5+32
    return resultado

print ("The temperature that you gave me in degrees Celsius, in degrees Fahrenheit is:", conversion (celsius))

