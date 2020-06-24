# By using with..as statement we do not have to explicitly close the file in the end
with (open("New1.txt","w")) as file:
    for i in range(1,6): # this statement is to iterate the printing for 5 times in the file
        file.write("Hello\n")

# This confirms if the file has been closed
print file.closed