#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[5]:


get_ipython().system('pip install selenium')


# In[3]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[5]:


driver = webdriver.Chrome()#c should be capital letters


# In[187]:


driver.get("https://www.shine.com/") #First get the webpage https://www.shine.com/


# In[173]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
#have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
#jobs data.

designation = driver.find_element(By.CLASS_NAME,"form-control") # it will bring cursor to search field
designation.send_keys('Data Analyst') # it will write data analyst in the search field


# In[174]:


location = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[176]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click() #This will click on the search button


# In[177]:


#Empty lists to store the attributes
job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[178]:


#scrapping job title
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
exp_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[179]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[180]:


import pandas as pd


# In[181]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[195]:


#Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
#have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
#This task will be done in following steps:

#Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field
designation = driver.find_element(By.CLASS_NAME,"form-control") # it will bring cursor to search field
designation.send_keys('Data Scientist') # it will write data analyst in the search field


# In[196]:


location = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore') #This will enter location


# In[198]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click() #This will click on the search button


# In[199]:


#Empty lists to store the attributes
job_title=[]
job_location=[]
company_name=[]


# In[200]:


#scrapping job title
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[201]:


print(len(job_title),len(job_location),len(company_name))


# In[202]:


import pandas as pd

df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name})
df


# In[231]:


#Q3: In this question you have to scrape data using the filters available on the webpage
#You have to use the location and salary filter
driver = webdriver.Chrome()#c should be capital letters


# In[232]:


driver.get("https://www.shine.com/") #First get the webpage https://www.shine.com/


# In[233]:


#Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field
designation = driver.find_element(By.CLASS_NAME,"form-control") # it will bring cursor to search field
designation.send_keys('Data Scientist') # it will write data analyst in the search field


# In[235]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click() #This will click on the search button


# In[243]:


#find absolute xpath of particular filter than write code of it as click on search button.
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[8]/span/label')
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[4]/button[2]')
search.click()


# In[263]:


#find absolute xpath of particular filter than write code of it as click on search button.
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[3]/span/label')
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[4]/button[2]')
search.click()


# In[264]:


#Empty lists to store the attributes
job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[265]:


#scrapping job title
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
exp_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[267]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[268]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[ ]:





# In[24]:


#Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
#6. Brand
#7. ProductDescription
#8. Price
driver = webdriver.Chrome()#c should be capital letters
time.sleep(3)

driver.get("http://www.flipkart.com/") #it will get the webpage
#driver.maximize_window()
time.sleep(3)

item = driver.find_element(By.CLASS_NAME,"Pke_EE") # it will bring cursor to search field
item.send_keys('sunglasses') # it will write data analyst in the search field
time.sleep(3)

search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button')
search.click() #This will click on the search button
time.sleep(3)

#Empty lists to store the attributes
brand_name=[]
prod_tags=[]
price_v=[]
time.sleep(3)

start=0
end=3
for page in range(start,end):
    p_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in p_tags[0:100]:
        prod_tags.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
    if range==3:
        break

    brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags[0:100]:
        brand_name.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
    if range==3:
        break
        
    pr_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in pr_tags[0:100]:
        price_v.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
    if range==3:
        break


# In[ ]:


print(len(brand_name),len(prod_tags),len(price_v))


# In[26]:


df=pd.DataFrame({'Brand':brand_name[0:100],'Product':prod_tags[0:100],'Price':price_v[0:100]})
df


# In[27]:


#Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
#search field.
#You have to scrape 3 attributes of each sneaker:
#1. Brand
#2. ProductDescription
#3. Price

driver = webdriver.Chrome()#c should be capital letters

driver.get("https://www.flipkart.com/")


# In[28]:


import numpy as np
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")


# In[605]:





# In[572]:





# In[29]:


driver = webdriver.Chrome()#c should be capital letters

driver.get("https://www.flipkart.com/")

item = driver.find_element(By.CLASS_NAME,"Pke_EE") # it will bring cursor to search field
#item = driver.find_element_by_class_name('class="_3704LK"')
item.send_keys('sneakers') # it will write data analyst in the search field
time.sleep(3)

search = driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click() #This will click on the search button
time.sleep(3)

#Empty lists to store the attributes
brand_name=[]
prod_tags=[]
price_v=[]
time.sleep(3)

start=0
end=3
for page in range(start,end):
    p_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in p_tags[0:100]:
        prod_tags.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
        
    pr_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in pr_tags[0:100]:
        price_v.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
    if range==3:
        break
    
    brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags[0:100]:
        brand_name.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)
    if range==3:
        break


# In[30]:


print(len(prod_tags),len(price_v),len(brand_name))


# In[31]:


df=pd.DataFrame({'Brand':brand_name[0:100],'Product':prod_tags[0:100],'Price':price_v[0:100]})
df


# In[ ]:


#Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
#set CPU Type filter to “Intel Core i7” as shown in the below image:


# In[139]:


driver = webdriver.Chrome()#c should be capital letters

driver.get("https://www.amazon.in/")


# In[142]:


item = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input') # it will bring cursor to search field
#item = driver.find_element_by_class_name('class="_3704LK"')
item.send_keys('Laptop') # it will write data analyst in the search field
time.sleep(3)

search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div')
search.click() #This will click on the search button
time.sleep(3)


# In[37]:


lap_title=[]
lap_rating=[]
lap_price=[]

#find absolute xpath of particular filter than write code of it as click on search button.
search = driver.find_element(By.XPATH,'//li[@id="p_n_feature_thirteen_browse-bin/12598163031"]//i')
#search = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[11]/li/span/a/span')
search.click()


# In[144]:


#scrapping job title
lap_title=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in lap_title[0:100]:
    title=i.text
    lap_title.append(title)
    
lap_rating=driver.find_elements(By.XPATH,'//span[@class="a-size-base puis-normal-weight-text"]')
for i in lap_rating[0:100]:
    rating=i.text
    lap_rating.append(rating)
    
lap_price=driver.find_elements(By.XPATH,'//span[@class="a-price"]')
for i in lap_price[0:100]:
    price=i.text
    lap_price.append(price)


# In[145]:


print(len(lap_title),len(lap_rating),len(lap_price))


# In[146]:


df.drop(df.index[0:24])


# In[147]:


df=pd.DataFrame({'Title':lap_title[0:34],'Price':lap_price[0:34],'Rating':lap_rating[0:34]})
df


# In[231]:


#Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
#The above task will be done in following steps:
#1. First get the webpagehttps://www.azquotes.com/
#2. Click on TopQuotes
#3. Than scrap a) Quote b) Author c) Type Of Quote

driver = webdriver.Chrome()#c should be capital letters

driver.get("https://www.azquotes.com/top_quotes.html/")


# In[232]:


#find absolute xpath of particular filter than write code of it as click on search button.
quote=[]
author=[]
qtype=[]


# In[275]:


#scrapping job title
start=0
end=1
for page in range(start,end):
    q=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/p/a[2]')
    for i in q:
        quote.append(i.text)
    a=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in a:
        author.append(i.text)
    t=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in t:
        qtype.append(i.text)
    next_button= driver.find_element(By.XPATH,'//div[@class="tags"]/a')
    next_button.click()


# In[276]:


print(len(quote),len(author),len(qtype))


# In[277]:


df=pd.DataFrame({'Quote':quote[0:1000],'Author':author[0:1000],'Quote_Type':qtype[0:1000]})
df


# In[281]:


#Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
#Car name and Price) from https://www.motor1.com/
#This task will be done in following steps:
#1. First get the webpage https://www.motor1.com/
#2. Then You have to type in the search bar ’50 most expensive cars’
#3. Then click on 50 most expensive carsin the world..
#4. Then scrap the mentioned data and make the datafram

driver = webdriver.Chrome()#c should be capital letters

driver.get("https://www.motor1.com/")


# In[286]:


item = driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input') # it will bring cursor to search field
item.send_keys('50 most expensive cars') # it will write data analyst in the search field
time.sleep(3)

search = driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click() #This will click on the search button
time.sleep(3)


# In[287]:


search = driver.find_element(By.XPATH,'/html/body/div[10]/div[10]/div[2]/div[2]/a[2]')
search.click() #This will click on the search button
time.sleep(3)


# In[288]:


carn=[]
price=[]


# In[378]:


#scrapping job title
car=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car:
    carn.append(i.text)
    
p=driver.find_elements(By.TAG_NAME,'strong')
for i in p:
    price.append(i.text)


# In[ ]:


print(len(carn),len(price))


# In[379]:


df=pd.DataFrame({'Car_Name':car[0:50],'Price':price[0:50]})
df


# In[ ]:





# In[ ]:





# In[ ]:




