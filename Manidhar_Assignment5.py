#!/usr/bin/env python
# coding: utf-8

# In[71]:


#Question 1.2
import pandas as pd
import numpy as np
from matplotlib import pyplot
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_csv('E:\\5502\\criminals.csv')
df=df[['State','Year','Murder Rate']]
State_Alaska=df[df['State']=='Alaska']
State_Alaska=pd.DataFrame(State_Alaska[['Year','Murder Rate']])
State_Alaska=State_Alaska.rename(columns={'Murder Rate':'Murder rate in Alaska'})
State_Texas=df[df['State']=='Texas']
State_Texas=pd.DataFrame(State_Texas[['Murder Rate']]).reset_index()
State_Alaska['Murder rate in Texas']=State_Texas['Murder Rate']
pyplot.plot(State_Alaska['Year'],State_Alaska['Murder rate in Alaska'],label='Alaska',color='blue')
pyplot.plot(State_Alaska['Year'],State_Alaska['Murder rate in Texas'],label='Texas',color='black')
pyplot.legend()


# In[72]:


#Question 1.3
input_data=pd.read_csv('E:\\5502\\criminals.csv')
input_data=input_data[['State','Year','Murder Rate']]
def most_murderous(year):
    group=input_data.groupby('Year')
    getdata=group.get_group(year)
    top_five=getdata.sort_values('Murder Rate',ascending=False).head(5).reset_index()[['State','Murder Rate']]
    a=np.array(top_five['State'])
    print(a[::-1])
    pyplot.barh(top_five['State'],top_five['Murder Rate'], color='red')
most_murderous(1996)


# In[73]:


#Question 1.4
input_data=pd.read_csv('E:\\5502\\criminals.csv')
input_data=input_data[['State','Year','Population','Murder Rate']]
Texas_murder_rate=input_data[(input_data['State']=='Texas') & (input_data['Year']==1988)].reset_index()[['Population','Murder Rate']]
Texas_murders=((Texas_murder_rate['Population']*Texas_murder_rate['Murder Rate'])/100000).tolist()
Texas_murder_rate_1989=input_data[(input_data['State']=='Texas') & (input_data['Year']==1975)].reset_index()[['Population','Murder Rate']]
Texas_murders_1989=((Texas_murder_rate_1989['Population']*Texas_murder_rate_1989['Murder Rate'])/100000).tolist()
Texas_change=Texas_murders[0]-Texas_murders_1989[0]
Texas_change=np.round(Texas_change)
print(f" People murdered:{Texas_change}")


# In[74]:


#Question2.1
df=pd.read_csv('E:\\5502\\criminals.csv')
df=df[['State','Year','Murder Rate']]
changes_by_state=[]
num_changes=[]
def two_year_changes (values, n):
    val=[]
    val2=[]
    a=np.array(values)[n:] - np.array(values)[:-n]
    b=np.array(values)[n:]
    c=np.array(values)[:-n]
    for temp in range(len(b)):
        if b[temp]>c[temp]:
            val.append(True)
        if b[temp]<c[temp]:
            val2.append(False)
        else:
            continue
    changes_by_state.append(len(val)-len(val2))
for state_one in df['State'].unique():
       years=df[df['State']==state_one]['Year'].tolist()
       rates=df[df['State']==state_one]['Murder Rate'].tolist()
       two_year_changes(rates,2)
print(changes_by_state)
print()
print()


# In[75]:


#Question 2.2
df=pd.DataFrame(input_data['State'].unique())
df.columns = ['State']
df['Murder Rate two_year_changes']=pd.DataFrame(changes_by_state)
print(df)
print()


# In[76]:


#Question 2.3
Positive_values=[]
Negative_values=[]
for minus in changes_by_state:
    if '-' in str(minus):
        Negative_values.append(minus)
    else:
        Positive_values.append(minus)
total_changes=len(Positive_values)-len(Negative_values)
print(f"Total Changes : {total_changes}")
print()


# In[77]:


#Question 2.4
num_changes=[]
for state in input_data['State'].unique():
    g=input_data[input_data['State']==state]
    year=g['Year']
    num_changes.append(len(np.array(year)[2:]-np.array(year)[:-2]))
print(f'num_changes : {sum(num_changes)}')
print()


# In[78]:


#Question 2.6
import random
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_csv('E:\\5502\\criminals.csv')
df=df[['State','Year','Murder Rate']]
changes_by_state =[]
final_random_samples=[]
for sample in range(500):
    def final_diff(change):
        Negative_values=[]
        Positive_values=[]
        for minus in change:
            if '-' in str(minus):
                Negative_values.append(minus)
        
            else:
                Positive_values.append(minus)
    
        total_changes=len(Positive_values)-len(Negative_values)
        final_random_samples.append(total_changes+5)
    def two_year_changes (values, n):
        val=[]
        val2=[]
        a=np.array(values)[n:] - np.array(values)[:-n]
        b=np.array(values)[n:]
        c=np.array(values)[:-n]
        for temp in range(len(b)):
            if b[temp]>c[temp]:
                val.append(True)
            if b[temp]<c[temp]:
                val2.append(False)
            else:
                continue
        changes_by_state.append(len(val)-len(val2))
    

    for state_one in input_data['State'].unique():
       
           rates=df[df['State']==state_one]['Murder Rate'].tolist()
           two_year_changes(rates,4)
    random_value=random.randrange(10,50)
    final_diff(changes_by_state[:random_value])


# In[80]:


#question 2.7
pyplot.hist(final_random_samples,alpha=0.50,edgecolor='black',color='yellow', linewidth=1.5)


# In[81]:


#Question 3.3
df=pd.read_csv('E:\\5502\\criminals.csv')
df=df[['State','Year','Population','Murder Rate']]
input_data=df[(df['State']!='Alaska') & (df['State']!='Texas') & (df['State']!='Wisconsin') & (df['State']!='Michigan') & (df['State']!='California')&(df['State']!='Minnesota')].reset_index()
input_data=input_data.rename(columns={"Murder Rate": 'death_penalty_murder_rates'})
print(input_data)
states=input_data['State'].unique()
count=0
count1=0
input_data_year_1971=input_data[input_data['Year']==1971]['death_penalty_murder_rates'].reset_index()['death_penalty_murder_rates']
input_data_year_1973=input_data[input_data['Year']==1973]['death_penalty_murder_rates'].reset_index()['death_penalty_murder_rates']
input_data3=pd.DataFrame(states)
input_data3.columns=['State']


# In[82]:


#Question 3.4
input_data3['Diff']=input_data_year_1973-input_data_year_1971
for a in input_data3['Diff']:
    if '-' in str(a):
        count+=1
    else:
        count1+=1
changes_72 =count1-count
print(f"Test Statistic 1971 to 1973:{changes_72}")


# In[83]:


#Question 3.5
get_ipython().run_line_magic('matplotlib', 'inline')
test_values=[]
for samples in range(5000):
    def simulation(Values):
        count=0
        count1=0
        for a in input_data3['Diff'][:Values]:
            if '-' in str(a):
                count+=1
            else:
                count1+=1
        changes_72 =count1-count
        test_values.append(changes_72)
    random_value=random.randrange(4,50)
    simulation(random_value)


# In[84]:


#Question 3.6
test_values=np.array(test_values)
empirical_P=np.count_nonzero(test_values >= changes_72 ) / samples
print(f'P-Value is : {empirical_P}')
pyplot.hist(test_values,bins=20,alpha=0.5,edgecolor='red',color='yellow',linewidth=1.2)


# In[85]:


#question 4.1
get_ipython().system('pip install datascience')
import random
from matplotlib import pyplot
import datascience as ds
from datascience import Table

test_values=[]
uniform = Table().with_columns("Change", ds.make_array('Increase', 'Decrease'),"Chance", ds.make_array(0.5,0.5))
test_statistics=uniform.sample_from_distribution('Chance', 100)

def run_test(size):
    test_values.append(uniform.sample_from_distribution('Chance',100).column(2).item(0)-uniform.sample_from_distribution('Chance', 100).column(2).item(1))
          
for sample_test in range(5000):
    run_test(44)  
test_values1=np.array(test_values)
empirical_P=np.count_nonzero(test_values1>=22) / sample_test
print(f"P-Value :{empirical_P}")


# In[86]:


#Question 5.1
df=pd.read_csv('E:\\5502\\criminals.csv')
mean_difference=[]
mean_difference_six_states=[]
df=df[['State','Year','Population','Murder Rate']]
input_data1=df[(df['State']!='Alaska') & (df['State']!='Texas') & (df['State']!='Hawaii') & (df['State']!='Iowa') & (df['State']!='New Jersey')&(df['State']!='Minnesota')].reset_index()
data_frame=input_data1['Year'].unique()
d=input_data1.groupby('Year')
for year in data_frame:
    group=d.get_group(year)
    mean_difference.append(group['Murder Rate'].mean())
input_data7=df[(df['State']=='Alaska') | (df['State']=='Texas') | (df['State']=='Hawaii') | (df['State']=='Iowa') | (df['State']=='New Jersey')|(df['State']=='Minnesota')].reset_index()
d2=input_data7.groupby('Year')
for year_no in data_frame:
    group1=d2.get_group(year_no)
    mean_difference_six_states.append(group1['Murder Rate'].mean())
average_murder_rates=pd.DataFrame(data_frame)
average_murder_rates.columns=['Year']
average_murder_rates['Death penalty states']=mean_difference
average_murder_rates['No death penalty states']=mean_difference_six_states
print(average_murder_rates)


# In[87]:


#Question 5.2
pyplot.plot(average_murder_rates['Year'],average_murder_rates['No death penalty states'],label='No death penalty states',color='black')
pyplot.plot(average_murder_rates['Year'],average_murder_rates['Death penalty states'],label='Death penalty states',color='red')
pyplot.legend()


# In[ ]:




