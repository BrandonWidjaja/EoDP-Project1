# COMP20008 2021 Semester 1 Assignment 1

Name: Brandon Widjaja
Student ID: 1187107

# Project descriptions:

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
Finds all document IDs in the .txt files in the "cricket" folder. Document IDs consist of 4 upper-case chars, a "-", 3 integers and optionally another upper-case char.
Document IDs that are found are stored in the output csv along with their corresponding filenames.
Program is called by: python partb1.py <FILENAME>