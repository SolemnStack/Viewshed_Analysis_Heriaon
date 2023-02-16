# This code is reading a set of HTML files and extracting a numeric value from them, then writing that value to an ASCII file in a specific format.

# The code starts by defining two variables for the number of columns and files to be read, and using them to calculate the number of rows.
# It then creates a header string containing information about the ASCII file format, and writes that header to an ASCII file using the with open statement and the 'w' mode.
# Then, the script enters a while loop that iterates through each file, reading it and using a regular expression to extract a specific string ("Mean") and its value,
# which is then converted to a float number. It then performs a mathematical operation on that value and writes the result to the ASCII file, with a specific format.
# If the current file number is not a multiple of the number of columns, it writes the value followed by a space, otherwise it writes the value followed by a new line.

# Filepaths to reports need to be set before running

import re

# Number of columns = 70, as grid of simulation was 70m
numberOfCols = 70
# Number of files = 1120, as that is the amount of reports produced per Pinax/camera 
numberOfFiles = 1120
numberOfRows = numberOfFiles / numberOfCols
header = "NCOLS " +str(numberOfCols)+ "\nNROWS " +str(numberOfRows)+ "\nXLLCORNER 0 \nYLLCORNER 0  \nCELLSIZE 10 \nNODATA_VALUE -9999\n"
with open(r'writeToASC.asc', 'w') as f:
    f.write(header)

currentFileNumber = 0
while numberOfFiles > 0:
    numberOfFiles -= 1
    currentFileNumber += 1
    currentFile = r'report' + str(currentFileNumber) + '.html'

    with open(currentFile, 'r') as f:
        lines = f.read()

    items = re.findall("Mean.*$", lines, re.MULTILINE)
    for x in items:
        print(x)
    extractedNumber = items
    print(extractedNumber)
    print(extractedNumber[0])

    found = re.findall(r'\b\d+\b', extractedNumber[0])
    print(found)
    mean = int(found[0]) / 255
    print(mean)
    mean = int(mean*100)

    with open(r'writeToASC.asc', 'a') as f:
        if currentFileNumber % 70 != 0:
            f.write(str(mean) + " ")
        else:
            f.write(str(mean) + "\n")