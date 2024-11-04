#Author: MReduzino

'''
Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
Where T= Air Temperature (ºF) V= Wind Speed (mph)
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

air_temperature = float(input("What is the temperature? "))
F_or_C = input("Fahrenheit or Celsius (F/C)? ")
wind_speed = 5

if F_or_C.lower() == "c":
    air_temperature = celsius_to_fahrenheit(air_temperature)
    
while wind_speed <= 60:
    windchill = calculate_wind_chill(air_temperature, wind_speed)
    print(f"At temperature {air_temperature}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")
    wind_speed += 5