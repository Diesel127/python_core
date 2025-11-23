with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "a") as file:
    file.write("\nAppended text")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)