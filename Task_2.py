# Write and Append Data to a File

# Takes user input and writes it to a file named output.txt.
file=open('output.txt','r+')
a=input('\nEnter text to write to the file: ')
writing_file = file.write(a+'\n')
file.close()
print('Data successfully written to output.txt.')


# Appends additional data to the same file.
file=open('output.txt','a')
b=input('\nEnter additional text to append: ')
appending_file = file.write(b+'\n')
file.close()
print('Data successfully appended.')


# Reads and displays the final content of the file.
file=open('output.txt','r')
reading_file=file.read()
print('\nFinal content of output.txt:')
print(reading_file)
file.close()
