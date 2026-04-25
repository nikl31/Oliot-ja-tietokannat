print("Per Miller's Law, humans can retain ~7 items in short-term memory.")

text = input("Insert memorable string: ")

if len(text) < 7:
    print("This string will be easy to remember.")
else:
    print("This string will be hard to remember.")