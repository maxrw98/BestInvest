#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime,date
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from dateutil.relativedelta import relativedelta


# In[2]:


style.use('ggplot')


# In[3]:


today = datetime.today().strftime('%Y-%m-%d')
a_day_ago = datetime.today() - relativedelta(days=+1)
a_week_ago = datetime.today() - relativedelta(weeks=+1)
a_month_ago = datetime.today() - relativedelta(months=+1)
half_year_ago = datetime.today() - relativedelta(months=+6)
a_year_ago  = datetime.today() - relativedelta(years=+1)
five_years_ago  = datetime.today() - relativedelta(years=+5)


# In[4]:


assets = ['TSLA', 'KO', 'AAPL', 'BNTX','MRNA','NFLX','AMZN','ADSK','MDLZ','GOOGL']


# In[5]:


# Assign weight to stocks
weights = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])


# In[6]:


df_a_day_ago = pd.DataFrame()
df_a_week_ago = pd.DataFrame()
df_a_month_ago = pd.DataFrame()
df_half_year_ago = pd.DataFrame()
df_a_year_ago = pd.DataFrame()
df_five_years_ago = pd.DataFrame()


# In[7]:


import calendar
my_date = date.today()

if calendar.day_name[my_date.weekday()] == 'Saturday' or 'Sunday':
    a_day_ago = datetime.today() - relativedelta(days=+2)


# In[8]:


for stock in assets:
    df_a_day_ago[stock] = web.DataReader(stock, data_source = 'yahoo', start=a_day_ago, end = today)['Adj Close']
    df_a_week_ago[stock] = web.DataReader(stock, data_source = 'yahoo', start=a_week_ago, end = today)['Adj Close']
    df_a_month_ago[stock] = web.DataReader(stock, data_source = 'yahoo', start=a_month_ago, end = today)['Adj Close']
    df_half_year_ago[stock] = web.DataReader(stock, data_source = 'yahoo', start=half_year_ago, end = today)['Adj Close']
    df_a_year_ago[stock] = web.DataReader(stock, data_source = 'yahoo', start=a_year_ago, end = today)['Adj Close']
    df_five_years_ago = web.DataReader(stock, data_source = 'yahoo', start=five_years_ago , end = today)['Adj Close']


# In[9]:


df = pd.DataFrame(
    {'dfs':[df_a_day_ago, df_a_week_ago, df_a_month_ago, df_half_year_ago, df_a_year_ago, df_five_years_ago]
    },
    index = ['1 day ago','1 week ago','1 month ago','half year ago','1 year ago', '5 years ago'],)


# In[10]:


# Show the daily simple return
returns = df_a_year_ago.pct_change()   # /(price(i+1)/price(i))-1
returns


# In[11]:


df_a_year_ago.describe()


# In[12]:


# Creat and show the annualized covariance matrix
cov_matrix_annual = returns.cov() * 252   # /(price(i+1)/price(i))-1
cov_matrix_annual


# In[13]:


# Calculate the portfolio variance
port_variance = np.dot(weights.T, np.dot(weights,cov_matrix_annual))
port_variance


# In[14]:


# Calculate the portfolio volatility aka standart deviaton

port_volatility = np.sqrt(port_variance)
port_volatility


# In[15]:


# Calculate the annual portfolio return
portfolioSimpleAnnualReturn = np.sum(returns.mean() * weights) * 252
portfolioSimpleAnnualReturn


# In[16]:


# Show the expected annual return, volatility
percent_var = str( round(port_variance,2) * 100) + '%'
percent_vola = str(round(port_volatility,2)*100) + '%'
percent_return  = str(round(portfolioSimpleAnnualReturn,2)* 100) + '%'


# In[17]:


print('Expected annual return:' , percent_return)
print('Annual volatility /risk:', percent_vola)
print('Annual variance:', percent_var)


# In[18]:


from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


# In[19]:


#Portfolio Optimization

#Calculate the expected Returns and the annualised sample covariance matrix of asset returns
mu = expected_returns.mean_historical_return(df_a_year_ago)
S = risk_models.sample_cov(df_a_year_ago)

#Optimize for max sharpe ratio - it measures the performance of an investment compared to investments such as bonds or treasury bills
ef = EfficientFrontier(mu,S)
weights = ef.max_sharpe()

cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose = True)


# In[20]:


from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices


# In[21]:


latest_prices = get_latest_prices(df_a_year_ago)
weights = cleaned_weights
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value = 10000)

allocation, leftover = da.lp_portfolio()
print('Discrete allocation:', allocation)
print('Funds remaining: ${:.2f}'.format(leftover))


# In[22]:


#pip install cvxpy


# In[23]:


#pip install cvxopt


# In[24]:


#Time
#schedule.every().day.at("15:30").do()
#schedule.every().day.at("22:00"do.()

#while True:
    #schedule.run_pending()
    #time.sleep(1)


# In[ ]:




