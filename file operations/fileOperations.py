# create and write in file
with open("file1.txt", "w") as f:
    f.write("some random text")

# read the file
with open("file1.txt", "r") as f:
    s = f.read()
print(s)

# append the file with new text
with open("file1.txt", "a") as f:
    f.write("\nappending the text\n")

with open("file1.txt", "r") as f:
    s = f.read()
print(s)