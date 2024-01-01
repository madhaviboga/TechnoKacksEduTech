def convert_temp(temp, unit):
 if unit == "F":
   return (temp - 32) * 5/9
 elif unit == "C":
   return temp * 9/5 + 32
 else:
   raise ValueError("Invalid unit: {}".format(unit))

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (F or C): ").upper()

new_temp = convert_temp(temp, unit)
new_unit = "C" if unit == "F" else "F"

print(f"{temp} degrees {unit} is equal to {new_temp:.1f} degrees {new_unit}")

