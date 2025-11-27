import sys

# If user provides weight and height via command line
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    weight = 70.0     # default weight in kg
    height = 1.75     # default height in meters
    print("No input given — using default values:")

# Calculate BMI
bmi = weight / (height * height)

# Print results
print("\n--- BMI Calculation ---")
print("Script Name:", script_name)
print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI:", bmi)