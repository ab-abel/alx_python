#!/usr/bin/env python3
#Temprature converter from Fahrenheit to Celsius

def convert_to_celsius(fahrenheit):
    if(fahrenheit == -459.67):
        celsius = (fahrenheit - 32) * (5/9)
        celsius = round(celsius, 2)
    else:
        celsius = (fahrenheit - 32) * (5/9)
    return celsius

# print(convert_to_celsius(100))
# print(convert_to_celsius(-40))
# print(convert_to_celsius(-459.67))
# print(convert_to_celsius(32))
