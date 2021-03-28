#------------------------------------------------------------------------------
#Partb1.py; Brandon Widjaja 1187107
#------------------------------------------------------------------------------

## Part B Task 1
#import libraries
import re
import pandas as pd
import os
import argparse

#read in desired output file name from commandline
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

#create dataframe to store filenames and doc IDs
df = pd.DataFrame(columns = ['Filename', 'documentID'])

#the pattern to search for. assume that all sentences start with an uppercase, 
#this helps identify whether or not we should include the optional final character
pattern = r'[A-Z]{4}\-\d{3}[A-Z]{0,1}(?![a-z])'

#search every file ending with ".txt" in the "cricket" folder
for filename in os.listdir('cricket'):
    if filename.endswith(".txt"):
        #read in each text doc
        with open('cricket'+'/'+ filename) as file:
            textfile = file.read()
        #search the file for the pattern and append the files name as well as ID
        if re.search(pattern, textfile):
            docid= re.search(pattern, textfile)
            df.loc[len(df.index)] = [filename, docid.group(0)] 
        file.close()
        continue
    else:
        continue

#sort dataframe by filename and save as required CSV
df.sort_values(by=['Filename'], inplace=True)
df.to_csv(args.filename, index = False)
