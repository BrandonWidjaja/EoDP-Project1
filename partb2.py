#------------------------------------------------------------------------------
#Partb1.py; Brandon Widjaja 1187107
#------------------------------------------------------------------------------

# Part B Task 2
import re
import os
import sys

#read in folder name and txt file name from stdin
file= sys.argv[1][-7:]
folder= sys.argv[1][:-7]

#open the specified txt
with open(folder+'/'+ file) as file:
    textfile = file.read()

#preprocess txt file
def preprocess(txt):
    #remove non-alhpabetic characters
    txt = re.sub(r'[^a-zA-Z\s]','', txt)
    #replace tabs and newlines with whitespace
    txt = re.sub(r'[\n\t]',' ', txt)
    #ensure no consecutive whitespaces
    txt = re.sub(' +', ' ', txt)
    #convert all to lowercase
    txt = txt.lower()
    return txt

#guard the print function to stop it from being called 
#when function is imported
if __name__ == "__main__":
    print(preprocess(textfile))