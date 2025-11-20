import sys

if len(sys.argv) != 5:
    print("Usage: python name.py <name> <id> <salary>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
id = sys.argv[2]
salary =sys.argv[3]
exp =sys.argv[4]

print("Script Name:", script_name)
print("Employee Name:", name)
print("Employee Id:", id)
print("Employee salary",salary)
print("Employee Experience:", exp)