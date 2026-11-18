
try:
    text = input("Enter some text: ")

    with open("user_data.txt", "w") as file:
        file.write(text)

    print("Text saved successfully!")

except IOError:
    print("Error: An input/output error occurred while writing to the file.")
