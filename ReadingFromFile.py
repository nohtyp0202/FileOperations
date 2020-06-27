
# Reading from  a file

# Creates a file and writes data into the file
with (open("FileReading.txt","w")) as fi:
    fi.write("First line \n") # as \n is in the end a new line is initiated
    fi.write("second line \n")
    fi.write("third line \n")
    fi.write("end of document \n")

print fi.closed # to confirm if the file is closed


with (open("FileReading.txt","r")) as re:
   print re.read(4) # read first four characters
   print re.read(6) # read NEXT six characters
   print re.read() # if no parameter is passed then it will read till end of the document

print re.closed # As with..as is used files are always closed in the end


# tell() --> tells the position of the cursor in the file

with (open("FileReading.txt", "r")) as telfil:
    print telfil.tell() # tells the current position of the cursor in the file


# seek() --> seek(<parameter_int_intended position of cursor>) method takes the cursor to the specified position

with (open("FileReading.txt","r")) as refil:
    refil.seek(20) # Cursor is now pointing to the 20th character in the file
    print refil.read(15) # starting from 20th character it will read NEXT 15 character
    print refil.tell() # tells the new position of the cursor ( 20 + 15 = 35 )