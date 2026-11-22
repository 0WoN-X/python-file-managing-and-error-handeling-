
filename = input("Enter filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError as e:
    error_message = f"Error: {e}"

    with open("error_log.txt", "a") as log_file:
        log_file.write(error_message + "\n")

    print("File not found!")
    print("The error has been saved in error_log.txt")
