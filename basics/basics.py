#!/usr/bin/python

#even comma works to concat
print "Python is really a great language,", "isn't it?"

# raw_input function is used like cin , instead use str = raw_input() for string input
str = raw_input("enter your input:");

# plus works for concat
print "input received is :"+ str


'''
We have seen  how to print and concat , now we will see file read
'''


'''
--------------------------------------------
File read ... open
'''

# open method to open File

# f  = open(filename, access_mode, buffering)
# buffering =1  1 line is buffered while accessing file
#access mode w -> write, a-> append . if file dosent exists creates new file

f = open("foo.txt", "w")
f.write(str)

#tells the current position of pointer
position = f.tell()

print "tell",position

# take the pointer to beginning of file
position = f.seek(0,0)

print "seek",position

# a better way to open a file is using with statement
with open("foo.txt") as f:
    for line in f:
        print line

# in above statement file.close will automatically be called

with open("foo.txt", "w") as f:
    f.write("hello world")

with open("foo.txt") as f:
    data = f.readlines()

# line is a variable , data is an array of lines, by default split will split on space
for line in data:
    words = line.split()
    print words





f.close()
