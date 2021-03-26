#import libraries
import pandas as pd
import argparse

#read in desired output file name from commandline
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

#------------------------------------------------------------------------------
#parta1.1 Creating the dataframe
#------------------------------------------------------------------------------

#read in desired columns from csv file
covid = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1')
covid = covid.loc[:,['location','date','total_cases','new_cases','total_deaths',
                     'new_deaths']]

#convert dates from 2020 to months
covid['date'] = pd.to_datetime(covid['date'])
#take data from 2020 only
covid=covid[(covid['date'].dt.year == 2020)]
covid['date'] = covid["date"].dt.strftime("%m")
covid.rename(columns = {"date": "month"}, inplace = True)

#group by location and month
grouped_covid = covid.groupby(['location', 'month'], as_index = False).agg({
    'total_cases': ['max'], 'new_cases': ['sum'], 'total_deaths' :['max'],
    'new_deaths': ['sum']})
#remove headers from .agg
grouped_covid.columns = grouped_covid.columns.droplevel(1)

#------------------------------------------------------------------------------
#parta1.2 Adding fatality rate column
#------------------------------------------------------------------------------

#add fatality rate column
grouped_covid["case_fatality_rate"] = grouped_covid["total_deaths"].div(
    grouped_covid["total_cases"])
#move it to desired column
grouped_covid = grouped_covid[['location','month', 'case_fatality_rate',
                               'total_cases','new_cases', 'total_deaths',
                               'new_deaths']]

#remove all rows with any NaN values i.e. no case_fatality_rate entry
#this will be done by replacing all NaN values with an empty string
nan_value = float("NaN")
grouped_covid.replace("", nan_value, inplace = True)
#remove rows with empty values
grouped_covid.dropna(subset = ["case_fatality_rate"], inplace = True)

#export as CSV
grouped_covid.to_csv(args.filename, index = False)

#print the first 5 rows of datastructure
print(grouped_covid.head(5))
