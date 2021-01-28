#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This Program Optimizizes Users Portfolio using Efficient Frontier


# In[2]:


# https://en.wikipedia.org/wiki/Portfolio_optimization


# In[3]:


pip install pandas-datareader


# In[4]:


from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[5]:


# Get the stock symbols
assets = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']


# In[6]:


# Assign weight to stocks
weights = np.array([0.2,0.2,0.2,0.2,0.2])


# In[7]:


# Get the stocks start date
stockStartDate = '2013-01-01' #First full year for FB :D


# In[8]:


# Get the stocks end date
today = datetime.today().strftime('%Y-%m-%d')


# In[9]:


today


# In[10]:


# Create a dataframe to store the adjusted close price of the stocks

df = pd.DataFrame()

# Store the adjusted close price of the stock into the df

for stock in assets:
    df[stock] = web.DataReader(stock, data_source = 'yahoo', start=stockStartDate, end = today)['Adj Close']


# In[11]:


# Show the first five rows of the dataframe
df.head()


# In[12]:


#Visually show the stock/portfolio
title = 'Portfolio Adjusted Close Price-Past'

# Get the stocks
my_stocks = df

# Create and plot the graph

for symbol in my_stocks.columns.values:
    plt.plot(my_stocks[symbol], label = symbol)

plt.title(title)
plt.xlabel('Date', fontsize = 20)
plt.ylabel('Adjusted Price in USD ($)', fontsize = 20)
plt.legend(my_stocks.columns.values, loc = 'upper right')
plt.show()


# In[13]:


# Show the daily simple return
returns = df.pct_change()   # /(price(i+1)/price(i))-1
returns[1:]


# In[14]:


# Creat and show the annualized covariance matrix
cov_matrix_annual = returns.cov() * 252
cov_matrix_annual


# In[15]:


# Calculate the portfolio variance
port_variance = np.dot(weights,cov_matrix_annual)
port_variance


# In[16]:


port_variance = np.dot(weights.T, port_variance)
port_variance


# In[17]:


# Calculate the portfolio volatility aka standart deviaton

port_volatility = np.sqrt(port_variance)
port_volatility


# In[18]:


# Calculate the annual portfolio return
portfolioSimpleAnnualReturn = np.sum(returns.mean() * weights) * 252
portfolioSimpleAnnualReturn


# In[19]:


# Show the expected annual return, volatility
percent_var = str( round(port_variance,2) * 100) + '%'
percent_vola = str(round(port_volatility,2)*100) + '%'
percent_return  = str(round(portfolioSimpleAnnualReturn,2)* 100) + '%'


# In[20]:


print('Expected annual return:' , percent_return)
print('Annual volatility /risk:', percent_vola)
print('Annual variance:', percent_var)


# In[21]:


pip install cvxpy


# In[22]:


pip install PyPortfolioOpt


# In[23]:


from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


# In[ ]:




