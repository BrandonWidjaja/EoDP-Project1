#import libraries
import pandas as pd
import argparse

#read in desired columns from csv file
covid = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1')
covid=covid.loc[:,['location','date','total_cases','new_cases','total_deaths','new_deaths']]

#convert dates columns to months
covid['date']= pd.to_datetime(covid['date'])
covid['date'] = covid["date"].dt.strftime("%m")
covid.rename(columns = {"date": "month"}, inplace = True)

print(covid)