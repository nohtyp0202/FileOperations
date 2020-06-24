
# This statement open a file in "w" --> writing mode
file = open("new_file.txt","w")

# Here text is entered into the file. \n adds a new empty line in the file
file.write("first line \n")

# This statement will add second new line into the file
file.write("second line \n")

#Always close an opened file. This statement closes the file and frees up the spaces
file.close()

# This statement confirms closing of the file
print file.closed
