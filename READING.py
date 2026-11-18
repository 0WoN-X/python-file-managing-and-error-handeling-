
filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: You don't have permission to read this file!")