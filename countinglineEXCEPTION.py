filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        count = 0

        for line in file:
            count += 1

    print("Number of lines:", count)

except FileNotFoundError:
    print("Error: File not found!")