# DIRECTORIES
# OS library has many functions that helps in accessing and working with directories
import os

# to getcwd() --> get Current Working Directory
print os.getcwd()

print os.getcwdu()

# To os.chdir() --> to change directory by giving the path as a string
os.chdir("/Users/gururao/Desktop/Sahana/Notes")

with (open("NewFile.txt","w")) as f:
    f.write("Hello")

print os.getcwd()

os.chdir("/Users/gururao/Desktop/Sahana/Python/2020Proj")
print os.getcwd()