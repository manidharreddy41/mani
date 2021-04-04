#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
from scipy import stats


# In[2]:


df_choice = pd.read_csv(r'E:\\5502\\multipleChoiceResponses.csv')
question_names = df_choice.iloc[0]
df_choice = df_choice.drop(0, axis=0)

df_choice = df_choice[df_choice['Q9'].notnull()]
df_choice = df_choice[df_choice['Q9'] != 'I do not wish to disclose my approximate yearly compensation']


# In[16]:


#male
df_male=df_choice[df_choice['Q1']=='Male']
print(df_male.shape[0])
newstr=[x.replace("-"," ") for x in df_male['Q9']]
salary_male=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_male.sal_high.fillna(value=salary_male.sal_low, inplace=True)

salary_male["sal_low"]=pd.to_numeric(salary_male["sal_low"])
salary_male.loc[salary_male["sal_low"]<300000, "sal_low"] = salary_male["sal_low"]*1000


salary_male["sal_high"]=pd.to_numeric(salary_male["sal_high"])

salary_male['avg_male'] = salary_male[['sal_low', 'sal_high']].mean(axis=1)

print(st.median(salary_male['avg_male']))


# In[17]:


# Female
df_female=df_choice[df_choice['Q1']=='Female']
print(df_female.shape[0])
newstr=[x.replace("-"," ") for x in df_female['Q9']]
salary_female=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_female.sal_high.fillna(value=salary_female.sal_low, inplace=True)

salary_female["sal_low"]=pd.to_numeric(salary_female["sal_low"])

salary_female.loc[salary_female["sal_low"]<300000, "sal_low"] = salary_female["sal_low"]*1000

salary_female["sal_high"]=pd.to_numeric(salary_female["sal_high"])

salary_female['avg_female'] = salary_female[['sal_low', 'sal_high']].mean(axis=1)
salary_female.to_excel("out.xlsx")
print(st.median(salary_female['avg_female']))


# In[19]:


#Question2 histogram

plt.style.use('ggplot')
plt.ticklabel_format(useOffset=False, style='plain')
plt.hist(salary_male['avg_male'], alpha=0.5, label='Male')
plt.hist(salary_female['avg_female'], alpha=0.5, label='Female')
plt.legend(loc='upper right')
plt.show()


# In[20]:


#Sample distribution
male_sam=df_male.sample(n=250,replace="False")
female_sam=df_female.sample(n=250,replace="False")
samp_pp = pd.concat([male_sam, female_sam])


# In[22]:


# Salary Histogram for the Sample

plt.style.use('ggplot')
plt.hist(samp_pp['Q9'])
plt.xticks(rotation=-90)
plt.title("Salary Histogram", fontsize=15)
plt.show()


# In[24]:


# Median for the Sample
# Male

newstr=[x.replace("-"," ") for x in male_sam['Q9']]
salary_male=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_male.sal_high.fillna(value=salary_male.sal_low, inplace=True)

salary_male["sal_low"]=pd.to_numeric(salary_male["sal_low"])
salary_male.loc[salary_male["sal_low"]<300000, "sal_low"] = salary_male["sal_low"]*1000
salary_male["sal_high"]=pd.to_numeric(salary_male["sal_high"])

salary_male['avg_male'] = salary_male[['sal_low', 'sal_high']].mean(axis=1)

print(st.median(salary_male['avg_male']))


# In[25]:


# Female

newstr=[x.replace("-"," ") for x in female_sam['Q9']]
salary_female=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_female.sal_high.fillna(value=salary_female.sal_low, inplace=True)

salary_female["sal_low"]=pd.to_numeric(salary_female["sal_low"])
salary_female.loc[salary_female["sal_low"]<300000, "sal_low"] = salary_female["sal_low"]*1000

salary_female["sal_high"]=pd.to_numeric(salary_female["sal_high"])

salary_female['avg_female'] = salary_female[['sal_low', 'sal_high']].mean(axis=1)

print(st.median(salary_female['avg_female']))


# In[26]:


# Question3.1 & 3.3

yf, xf=np.histogram(st.median(salary_female['avg_female']), bins=1)
ym, xm=np.histogram(st.median(salary_male['avg_male']), bins=1)

plt.scatter(xf[-1],xf[-2])
plt.scatter(xm[-1],xm[-2])
plt.xticks(np.arange(10000, 50000, 5000))
plt.yticks(np.arange(10000, 50000, 5000))
plt.show()


# In[33]:


#Question3.4 test statistic
avg_male_mean=salary_male['avg_male'].mean()
avg_female_mean=salary_female['avg_female'].mean()
overall_gend=avg_male_mean-avg_female_mean
print("test statistic",overall_gend)

avg_overall_hist=salary_male['avg_male']-salary_female['avg_female']
plt.hist(avg_overall_hist,bins='auto',alpha=0.5,label='Mean Salaries')
plt.scatter(overall_gend,0,color='red',s=50,label='Test statistic of the histogram')
plt.show()


# In[12]:


# Bootstrap of 5000 samples
male_sam=df_male.sample(n=2500,replace="True")
female_sam=df_fmale.sample(n=2500,replace="True")


# In[34]:


# Question3.6 Male

newstr=[x.replace("-"," ") for x in male_sam['Q9']]
salary_male=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_male.sal_high.fillna(value=salary_male.sal_low, inplace=True)

salary_male["sal_low"]=pd.to_numeric(salary_male["sal_low"])
salary_male.loc[salary_male["sal_low"]<300000, "sal_low"] = salary_male["sal_low"]*1000
salary_male["sal_high"]=pd.to_numeric(salary_male["sal_high"])

salary_male['avg_male'] = salary_male[['sal_low', 'sal_high']].mean(axis=1)


# In[35]:


# Female

newstr=[x.replace("-"," ") for x in female_sam['Q9']]
salary_female=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
salary_female.sal_high.fillna(value=salary_female.sal_low, inplace=True)

salary_female["sal_low"]=pd.to_numeric(salary_female["sal_low"])
salary_female.loc[salary_female["sal_low"]<300000, "sal_low"] = salary_female["sal_low"]*1000

salary_female["sal_high"]=pd.to_numeric(salary_female["sal_high"])

salary_female['avg_female'] = salary_female[['sal_low', 'sal_high']].mean(axis=1)

avg_overall_boot=salary_male['avg_male']-salary_female['avg_female']
plt.hist(avg_overall_boot,bins='auto',alpha=0.5,label='BootStrap for 5000 samples')
plt.show()


# In[47]:


# Question3.7 P value and confidence interval
rand_pop=pd.DataFrame()
rand_pop['gender']=df_choice['Q1']
rand_pop['sal']=df_choice['Q9']
newstr=[x.replace("-"," ") for x in rand_pop['sal']]
p_c_d=pd.DataFrame([x.replace(",","").replace("+","").split() for x in newstr],columns=['sal_low',"sal_high"])
p_c_d.sal_high.fillna(value=p_c_d.sal_low, inplace=True)

p_c_d["sal_low"]=pd.to_numeric(p_c_d["sal_low"])
p_c_d.loc[p_c_d["sal_low"]<300000, "sal_low"] = p_c_d["sal_low"]*1000
p_c_d["sal_high"]=pd.to_numeric(p_c_d["sal_high"])
for i in range(250):
    p_c_d['mix_labels']=np.random.permutation(rand_pop['gender'])

p_c_d['avg_over'] = p_c_d[['sal_low', 'sal_high']].mean(axis=1)
p_c_d_m=p_c_d[p_c_d['mix_labels']=='Male']['avg_over']
p_c_d_f=p_c_d[p_c_d['mix_labels']=='Female']['avg_over']


pvalue=stats.ttest_ind(a=p_c_d_m,b=p_c_d_f,equal_var=False)
print(pvalue.pvalue)


# In[ ]:




