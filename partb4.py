#------------------------------------------------------------------------------
#Partb4.py; Brandon Widjaja 1187107
#------------------------------------------------------------------------------

## Part B Task 4
import re
import pandas as pd
import os
import sys
from nltk import PorterStemmer
from partb2 import preprocess
from partb1 import df

#------------------------------------------------------------------------------
#most of the code is similar to partb3.py, but instead we will stem all words 
#in each .txt file and also stem the args from stdin
#------------------------------------------------------------------------------

porter = PorterStemmer()

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
        #create an emtpy list that will be filled with the stemmed words
        stemtxt = []
        #stem each word and store in stemtxt
        for word in filepreproc.split():
            stemtxt.append(porter.stem(word))
        #convert stemtxt into string, each word seperated by whitespace
        stemmed = ' '.join(stemtxt)
        
        #check that each word is included the document
        for arg in sys.argv[1:6]:
            argstem = porter.stem(arg)
            
            #only include if word isnt part of another. also we assume 
            #the input word can include uppercase so we will ignore the case
            if not re.search(r"\b" + re.escape(argstem) + r"\b", stemmed, 
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