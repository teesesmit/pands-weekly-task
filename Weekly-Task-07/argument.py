#Write a program that reads in a text file 
#https://www.freecodecamp.org/news/file-handling-in-python/
#and outputs the number of e's it contains. 
#The program should take the filename from an argument on the command line. 

#Need to create a text file, with some of first paragraph of moby-dick? 
#read it into the the program
#outputs the number of e's it contains

#https://stackoverflow.com/questions/70175221/cant-open-file-in-the-same-directory
from pathlib import Path

FILENAME = Path(__file__).parent / "Moby_dick.txt"

# Open the file and read its contents - lecture
with open(FILENAME, 'r') as f:
    # Read the entire content of the file
    text = f.read()

# Print the content of the file to verify it's being read correctly
print("Contents of the file:")
print(text)

# Count the number of occurrences of the letter 'e' in the text
#https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
count_of_e = text.count('e')

# Print the number of occurrences of 'e' in the text
print("Number of 'e's in the text:", count_of_e)




