#Write a program that reads in a text file 
#and outputs the number of e's it contains. 
#The program should take the filename from an argument on the command line. 

#Need to create a text file, with some of first paragraph of moby-dick? 
#read it into the the program
#outputs the number of e's it contains
#arguments?? 

FILENAME = "Moby_dick.txt"

# Open the file and read its contents
with open(FILENAME, 'r') as f:
    # Read the entire content of the file
    text = f.read()

# Print the content of the file to verify it's being read correctly
print("Contents of the file:")
print(text)

# Count the number of occurrences of the letter 'e' in the text
e_count = text.count('e')

# Print the number of occurrences of 'e' in the text
print("Number of 'e's in the text:", e_count)




