myFile = 'D:\\test\\data.txt'
f = open(myFile, 'w') # Make a new file in output mode
f.write('Hello\n') # Write strings of bytes to it
f.write('world\n') # Returns number of bytes written in Python 3.0
f.close()

x = 0
for line in open(myFile):
    print line

