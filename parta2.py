import pandas as pd
import argparse
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------
#create dataframe for plot (code copied and slightly modified from parta1.py)
#-------------------------------------------------------------------------------

#read in desired output file name from commandline
parser = argparse.ArgumentParser()
parser.add_argument('filename1')
parser.add_argument('filename2')
args = parser.parse_args()

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
grouped_covid = covid.groupby(['location', 'month'], as_index = False).agg(
    {'total_cases': ['max'],
     'new_cases': ['sum'],
     'total_deaths' :['max'],
     'new_deaths': ['sum']})
#remove headers from .agg
grouped_covid.columns = grouped_covid.columns.droplevel(1)

#parta1.2

#add fatality rate column
grouped_covid["case_fatality_rate"] = grouped_covid["total_deaths"].div(
    grouped_covid["total_cases"])
#move it to desired column
grouped_covid = grouped_covid[['location','month', 'case_fatality_rate',
                               'total_cases','new_cases',
                               'total_deaths','new_deaths']]

#remove all rows with any NaN values i.e. no case_fatality_rate entry
#this will be done by replacing all NaN values with an empty string
nan_value = float("NaN")
grouped_covid.replace("", nan_value, inplace = True)
#remove rows with empty values
grouped_covid.dropna(subset = ["case_fatality_rate"], inplace = True)

#-------------------------------------------------------------------------------
#create the scatterplot from the data generated above
#-------------------------------------------------------------------------------

#assign each continent to their respective rows
africa = grouped_covid.iloc[10:20, :]
asia = grouped_covid.iloc[89:101, :]
australia = grouped_covid.iloc[101:111, :]
europe = grouped_covid.iloc[549:560, :]
north_america = grouped_covid.iloc[1176:1187, :]
south_america = grouped_covid.iloc[1458:1468, :]

#plot all continents with different colours and labels
plt.scatter(africa.new_cases, africa.case_fatality_rate, color= 'green',
            label="Africa")
plt.scatter(asia.new_cases, asia.case_fatality_rate, color= 'red',
            label="Asia")
plt.scatter(australia.new_cases, australia.case_fatality_rate, color= 'black',
            label="Australia")
plt.scatter(europe.new_cases, europe.case_fatality_rate, color= 'purple',
            label="Europe")
plt.scatter(north_america.new_cases, north_america.case_fatality_rate,
            color= 'orange', label="North America")
plt.scatter(south_america.new_cases, south_america.case_fatality_rate,
            color= 'blue', label="South America")

#label axis
plt.xlabel("New Cases")
plt.ylabel("Case Fatality Rate")
#define viewing limits for plot (based off min and max values from data)
plt.xlim([0, 0.8*10**7])
plt.ylim([0, 0.11])
#preprocessing
plt.grid(True)
plt.legend()
#save the first scatterplot named according to first input name
plt.savefig(args.filename1)

#for the second scatterplot 
#make x-axis scale logarithmic
plt.xscale('log')
#preprocessing
plt.xlim([10, 10**7])
plt.ylim([0, 0.11])
plt.xlabel("New Cases (Logarithmic)")
#save the second scatterplot named according to second input name
plt.savefig(args.filename2)