def calculate_molecular_mass(formula):
  atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "O": 15.999,
    "N": 14.007
  }

element_counts = {"H": 0, "C": 0, "O": 0, "N":0}
current_element = ""
number_buffer = ""

for char in formula:
    if char.isalpha():
      if number_buffer != "":
        count = int(number_buffer)
        element_counts[current_element] += (count - 1)
        number_buffer = ""
      current_element = char
      element_counts[current_element] += 1
    elif char.isdigit():
      number_buffer += char

if number_buffer != ""
  count = int(number_buffer)
  element_counts[current_element] += (count - 1)

total_mass = 0

for element, count in elemenet_counts.items():
  if count > 0:
    total_mass += count * atomic_masses[element]

return total_mass, element_counts

test_molecule = "C60"
final_mass, final_counts = calculate_molecular_mass(test_molecule)

print(f"Analyzing Molecule: {test_molecule}")
print(f"Element Breakdown: {final_counts}")
print(f"Total Molecular Mass: {final_mass}")
