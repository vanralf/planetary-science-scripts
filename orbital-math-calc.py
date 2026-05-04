# Script for calculating Period (P) and AU (a) using Kepler's Third Law
# P^2 = a^3

# Psuedo-code
# User Query -> Solve P or a
# If P, then calculate Orbital Period
# If a, then calculate AU Distance
# P = (a^3)^1/2
# a = (P^2)^1/3

# Prompt user
choice = input("Press P to calculate Period. Press a to calculate Distance")

# Calculate Period given AU (a)
if choice == 'P'
  a_str = input("Enter distance (a) in Astronomical Units (AU)")
  a = float(a_str)
  P = (a ** 3) ** 0.5
  print("The Orbital Period is {P} Earth years.")

# Calculate AU given Period
elif choice == 'a'
  p_str = input("Enter period (P) in years")
  p = float(p_str)
  a = (P ** 2) ** (1/3)
  print("The Distance is {a} AU")

else:
  print("Invalid choice. Run the script to try again")
