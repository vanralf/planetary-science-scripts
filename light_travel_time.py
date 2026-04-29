#Calculates the time it takes light to travel a certain distance
SPEED_OF_LIGHT = 299792.458

def light_travel_time(distance_km):
  return distance_km / SPEED_OF_LIGHT

distance = float(input("Enter distance in kilometers: "))
time_traveled = light_travel_time(distance)
print(f"Light takes {time_traveled} to travel {distance} kilometers")
