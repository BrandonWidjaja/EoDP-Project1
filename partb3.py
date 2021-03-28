#------------------------------------------------------------------------------
#Partb3.py; Brandon Widjaja 1187107
#------------------------------------------------------------------------------

## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os
from partb2 import preprocess
from partb1 import df

if len(sys.argv)>1:
    #iterate all files ending with '.txt' in the 'cricket' directory
    for filename in os.listdir('cricket'):
        #set 'include' to 1 on each loop in the directory. this variable will 
        #be used to keep track of whether or not all words are in the document
        include = 1
        
        if filename.endswith(".txt"):
            #read in the file
            with open('cricket'+'/'+ filename) as file:
                textfile = file.read()
            #apply preprocessing
            filepreproc = preprocess(textfile)
            #check that each word is included the document
            for arg in sys.argv[1:6]:
                #only include if word isnt part of another. also we assume 
                #the input word can include uppercase so we will ignore the case
                if not re.search(r"\b" + re.escape(arg) + r"\b", filepreproc, 
                                 re.IGNORECASE):
                    #if any word isnt found, set include to 0
                    include= 0
                else:
                    continue
            #print the ID if all words included
            if include:
                print(df.loc[df['Filename'] == filename, 'documentID'].item())
                
            else:
                continue
            file.close()