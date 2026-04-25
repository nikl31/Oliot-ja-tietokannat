filename = input("Insert filename to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    print(f"#### {filename} content ####")
    print(content)
    print(f"#### {filename} content ####")

except FileNotFoundError:
    print(f"File '{filename}' not found.")