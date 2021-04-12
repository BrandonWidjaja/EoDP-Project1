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
from sklearn.feature_extraction.text import TfidfTransformer
import math
from numpy import dot
from numpy.linalg import norm

#------------------------------------------------------------------------------
#most of the code is similar to partb4.py, but instead we will output
#the cosine similarities of the documents
#------------------------------------------------------------------------------

porter = PorterStemmer()
#stores the term frequencies for each document
term_counts = []
#stores the document IDs of the files with matching keywords
doc_IDs = []
#tracks if at least one file was found
found = 0
#iterate all files ending with '.txt' in the 'cricket' directory
for filename in os.listdir('cricket'):
    #set 'include' to 1 on each loop in the directory. this variable will 
    #be used to keep track of whether or not all words are in the document
    include = 1
        
    if filename.endswith(".txt"):
        #frequency of each keyword in the file
        word_freq = []
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
                #append the frequency of the word to word_freq
                word_freq.append(len(re.findall(r"\b" + re.escape(argstem) + r"\b", stemmed, 
                                re.IGNORECASE)))
                continue
        
        #append the frequency of the keywords and the document ID if all words included
        if include:
            term_counts.append(word_freq)
            doc_IDs.append(df.loc[df['Filename'] == filename, 'documentID'].item())
            found = 1
        else:
            continue
        file.close()
if found==1:   
    #tf-idf calculation
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(term_counts)

    doc_tfidf = tfidf.toarray()
    q_unit = []

    for arg in sys.argv[1:6]:
        q_unit.append(1/(math.sqrt(len(sys.argv)-1)))

    #cosine similarity calculation    
    def cosine_sim(v1, v2):
        return dot(v1, v2)/(norm(v1)*norm(v2))

    #list of all cosine similarities
    sims = [round(cosine_sim(q_unit, doc_tfidf[d_id]), 4) for d_id in range(doc_tfidf.shape[0])]

    #dictionary withe document IDs and their scores
    d = {'documentID': doc_IDs, 'score': sims}
    #convert to dataframe
    results = pd.DataFrame(d)
    #sort by score
    results.sort_values(by=['score'], inplace=True, ascending=False)
    #output the document IDs and their scores
    print(results.to_string(index=False))
else:
    print("No matching documents found")