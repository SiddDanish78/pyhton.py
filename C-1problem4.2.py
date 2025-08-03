#question - write a python program to print the contents of a directory using the os module.
# search online for the function which does that
import os

# select the directory whose content you want to list

directory = "C:\DRIVER"

#use the os module to list the directory content 

content = os.listdir(directory)

#print the content of the directory 

print(content)
