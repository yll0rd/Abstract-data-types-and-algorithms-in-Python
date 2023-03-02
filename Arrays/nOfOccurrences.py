from arrayADT import Array

theCounters = Array(127)
theCounters.clear( 0 )

# Open the text file for reading and extract each line from the file
# and iterate over each character in the line.
with open ("aTextFile.txt", "r") as File: 
    for line in File:
        for letter in line:
            code = ord(letter)  
            value = theCounters.getItem(code)
            value += 1
            theCounters.setItem(code,value)

# Print the results. The uppercase letters have ASCII values in the
# range 65..90 and the lowercase letters are in the range 97..122.
for i in range(26):
    print( "%c - %4d    %c - %4d" % \
    (chr(65+i), theCounters.getItem(65+i), chr(97+i), theCounters.getItem(97+i)) )