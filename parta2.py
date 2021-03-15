import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

covid = pd.read_csv('owid-covid-data-2020-monthly.csv',encoding = 'ISO-8859-1')
covid = covid.loc[:,['location','date','total_cases','new_cases','total_deaths','new_deaths']]
x = covid_graph.new_cases
y = covid_graph.case_fatality_rate
plt.scatter(x,y)
plt.savefig('test.png')