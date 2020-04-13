# -*- coding: utf-8 -*-
"""
Spyder Editor
pandas_skeleton
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger


covid_df = pd.read_csv('***')
print(covid_df.***)


covid_df.***()

#
# Which column names have missing values?
# ***
#
#

covid_df.***(inplace=True)
covid_df.***()

stats = covid_df.***()

cor = covid_df.***()

above_10_deaths = covid_df[covid_df['***'] > ***].head(10)

covid_df.plot(kind='scatter',x ='***', y='***', title="Cases by County Population") 

           