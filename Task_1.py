# Read a File and Handle Errors
try:                                      # If file exist.
    file=open('sample.txt','r')
    reading_file = file.readline()
    reading_file2 = file.readline()
    print('Reading file content: \nLine 1: '+reading_file+'Line 2: '+reading_file2)
    file.close()
except:                                   # If file do not exist.
    print("Error: The file 'sample.txt' was not found")