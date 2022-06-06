# COMP20008 2021 Semester 1 Assignment 1

Name: Brandon Widjaja
Student ID: 1187107

# Project descriptions:

Part 1: Wrote python scripts to read and process a CSV containing the locations, month, case fatality rate, total cases, new cases, total deaths, and new deaths for covid-19 in 2020. 

Part 2: Wrote python scripts to preprocess and extract information from a large collection of text files. Wrote a script to implement a search tool which returns the document IDs for each text file which included the specified words. This search script also implements a Porter Stemmer allowing the search to also include related inexact word matches. Also wrote a separate script which returns the cosine similarities of each document matching the keywords.


parta1.py
This program reads the input csv "owid-covid-data.csv" and outputs a csv containing the locations, month, case fatality rate, 
total cases, new cases, total deaths and new deaths for covid-19 in 2020, all aggregated monthly and sorted by location and month.
Program is called by: python parta1.py <FILENAME>

parta2.py
This program uses similar code as parta1.py but instead outputs two scatter plots of the case fatality rate against new cases per month for each continent.
Scatter plot "b" presents the data with the new cases in a log scale.
Program is called by: python parta2.py <FILENAME1> <FILENAME2>
    
owid-covid-2020-visual-analysis.pdf
An analysis of the scatter plots created in parta2.py
    
partb1.py
Finds all document IDs in the .txt files in the "cricket" folder. Document IDs consist of 4 upper-case chars, a "-", 
3 integers and optionally another upper-case char.
Document IDs that are found are stored in the output csv along with their corresponding filenames.
Program is called by: python partb1.py <FILENAME>
    
partb2.py
Preprocesses the specified document to make searching easier, removing all non-alphabetic characters, 
converting all spacing characters to single whitespaces and convert all characters to lower case.
Requires partb1.py to be in the same directory.
Program is called by: python partb2.py <DIRECTORY/FILENAME>
    
partb3.py
Input between 1-5 words and searches through all .txt files in the cricket folder and returns the document ID of the files that contain all the input words.
Requires partb1.py and partb2.py to be in the same directory.
Program is called by: python partb3.py <keyword1> <keyword2> <keyword3> <keyword4> <keyword5>
    
partb4.py
Same as partb3.py, however this program uses the Porter Stemmer so that the search function can also search for related inexact matches.
Requires partb1.py and partb2.py to be in the same directory.
Program is called by: python partb3.py <keyword1> <keyword2> <keyword3> <keyword4> <keyword5>
    
partb5.py
Returns the cosine similarities of each document matching the keywords, sorted by their score.
Requires partb1.py and partb2.py to be in the same directory.
Program is called by: python partb3.py <keyword1> <keyword2> <keyword3> <keyword4> <keyword5>
