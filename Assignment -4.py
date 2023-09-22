#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[3]:


#Q1...Scrape the details of most viewed videos on YouTube from Wikipedia. Url = 
#https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: 
#A) Rank 
#B) Name 
#C) Artist 
#D) Upload date 
#E) Views

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[25]:


rank = []
name = []
artist=[]
u_date=[]
views=[]

r=driver.find_elements(By.XPATH,'//div[@class="mw-parser-output"]/table[2]/tbody/tr/td[1]')
for i in r:
    rank.append(i.text)

n=driver.find_elements(By.XPATH,'//div[@class="mw-parser-output"]/table[2]/tbody/tr/td[2]')
for i in n:
    name.append(i.text)

a=driver.find_elements(By.XPATH,'//div[@class="mw-parser-output"]/table[2]/tbody/tr/td[3]')
for i in a:
    artist.append(i.text)
    
v=driver.find_elements(By.XPATH,'//div[@class="mw-parser-output"]/table[2]/tbody/tr/td[4]')
for i in v:
    views.append(i.text)
    
u=driver.find_elements(By.XPATH,'//div[@class="mw-parser-output"]/table[2]/tbody/tr/td[5]')
for i in u:
    u_date.append(i.text)


# In[26]:


print(len(rank),len(name),len(artist),len(u_date),len(views))


# In[27]:


df=pd.DataFrame({'Rank':rank,'name':name,'Artist':artist,'Upload_date':u_date,'Views':views})
df


# In[17]:


#Q2---Scrape the details team India’s international fixtures from bcci.tv.
#url = https://www.bcci.tv/.
#You need to find following details: 
#A) Match title (I.e. 1 ODI) 
#B) Series 
#C) Place 
#D) Date 
#E) Time 
#Note: - From bcci.tv home page you have reach to the international fixture page through code.


# In[31]:


driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.bcci.tv/")


# In[32]:


int = driver.find_element(By.XPATH,'//li[@class="nav-item"]/a')
int.click() 
time.sleep(3)


# In[33]:


title = []
series = []
place=[]
date=[]
time=[]


# In[34]:


t=driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]')
for i in t:
    title.append(i.text)
    
s=driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in s:
    series.append(i.text)
    
p=driver.find_elements(By.XPATH,'//span[@class="ng-binding"]')
for i in p:
    place.append(i.text)
    
d=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in d:
    date.append(i.text)
    
t=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in t:
    time.append(i.text)


# In[35]:


print(len(title),len(series),len(place),len(date),len(time))


# In[36]:


df=pd.DataFrame({'Title':title,'Series':series,'Place':place,'Date':date,'Time':time})
df


# In[ ]:


#Q3..Scrape the details of State-wise GDP of India from statisticstime.com.
#Url = http://statisticstimes.com/
#You have to find following details: 

#A)Rank 
#B) State 
#C) GSDP(18-19)- at current prices 
#D) GSDP(19-20)- at current prices 
#E) Share(18-19) 
#F) GDP($ billion) 
#Note: - From statisticstimes home page you have to reach to economy page through code. 


# In[69]:


driver = webdriver.Chrome()
driver.get("https://www.statisticstimes.com/")


# In[70]:


eco = driver.find_element(By.XPATH,'//*[@class="navbar"]/div[2]/button')
eco.click()
eco = driver.find_element(By.XPATH,'//*[@class="navbar"]/div[2]/div/a[3]')
eco.click()


# In[71]:


driver.get("https://www.statisticstimes.com/economy/india/indian-states-gdp.php")


# In[76]:


rank = []
state = []
gsdp1920=[]
gsdp1819=[]
share=[]
billion=[]

r=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[1]')
for i in r:
    rank.append(i.text)

s=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[2]')
for i in s:
    state.append(i.text)

gs=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[3]')
for i in gs:
    gsdp1920.append(i.text)
    
dp=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[4]')
for i in dp:
    gsdp1819.append(i.text)
    
sh=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[5]')
for i in sh:
    share.append(i.text)
    
b=driver.find_elements(By.XPATH,'//div[@id="header"]/div[2]/div[5]/div/div/table/tbody/tr/td[6]')
for i in b:
    billion.append(i.text)


# In[77]:


print(len(rank),len(state),len(gsdp1920),len(gsdp1819),len(share),len(billion))


# In[78]:


df=pd.DataFrame({'Rank':rank,'State':state,'GSDP 19-20 at current Price':gsdp1920,'GSDP 18-19 at current Price':gsdp1819,'Share':share,'GDP Billion $':billion})
df


# In[ ]:


#Q4..Scrape the details of trending repositories on Github.com
#Url = https://github.com/
#You have to find the following details: 
#A) Repository title 
#B) Repository description 
#C) Contributors count 
#D) Language used
#Note: - From the home page you have to click on the trending option from Explore menu through code. 


# In[2]:


driver = webdriver.Chrome()
driver.get("https://github.com/")


# In[3]:


exp = driver.find_element(By.XPATH,'//div[@class="header-menu-wrapper d-flex flex-column flex-self-end flex-lg-row flex-justify-between flex-auto p-3 p-lg-0 rounded rounded-lg-0 mt-3 mt-lg-0"]/nav/ul/li[3]/button')
exp.click()
exp = driver.find_element(By.XPATH,'//ul[@class="d-lg-flex list-style-none"]/li[3]/div/div[3]/ul/li[2]/a')
exp.click()


# In[13]:


title = []
desc = []
ccount=[]
lang=[]

try: 
    t=driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]/a')
    for i in t:
        title.append(i.text)

    d=driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
    for i in d:
        desc.append(i.text)

    c=driver.find_elements(By.XPATH,'//span[@class="d-inline-block mr-3"]')
    for i in c:
        ccount.append(i.text)
    
    l=driver.find_elements(By.XPATH,'//div[@class="f6 color-fg-muted mt-2"]/span/span[2]')
    for i in l:
        lang.append(i.text)
except:
        title.append('-')
        desc.append('-')
        ccount.append('-')
        lang.append('-')


# In[16]:


print(len(title),len(desc),len(ccount),len(lang))


# In[18]:


df=pd.DataFrame({'Title':title[0:23],'Description':desc[0:23],'Contributor':ccount[0:23],'Language':lang[0:23]})
df


# In[ ]:


#Q5...Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/
You have to find the following details: 
A) Song name 
B) Artist name 
C) Last week rank 
D) Peak rank 
E) Weeks on board 
Note: - From the home page you have to click on the charts option then hot 100-page link through code.


# In[4]:


driver = webdriver.Chrome()
driver.get("https://www.billboard.com/")


# In[5]:


exp = driver.find_element(By.XPATH,'//div[@class="main-menu-container js-hide-when-sticky"]/div/div/div[2]/div[2]/div/div/nav/ul/li/a[1]')
exp.click()
exp = driver.find_element(By.XPATH,'//div[@class="u-flex-grow-0 lrv-u-text-align-center"]/span/a')
exp.click()


# In[11]:


song = []
artist = []
lwr=[]
pr=[]
wob=[]

s=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li/h3')
for i in s:
    song.append(i.text)

a=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]/span')
for i in a:
    artist.append(i.text)

lw=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[4]/span')
for i in lw:
    lwr.append(i.text)
    
p=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[5]/span')
for i in p:
    pr.append(i.text)
    
wo=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[6]/span')
for i in wo:
    wob.append(i.text)


# In[12]:


print(len(song),len(artist),len(lwr),len(pr),len(wob))


# In[13]:


df=pd.DataFrame({'Song_Name':song,'Artist':artist,'Last_Week_Rank':lwr,'Peak_Rank':pr,'Week_on_Board':wob})
df


# In[ ]:


#Q6..Scrape the details of Highest selling novels. 
compare 
A) Book name 
B) Author name 
C) Volumes sold 
D) Publisher 
E) Genre 
link - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare


# In[21]:


driver = webdriver.Chrome()
driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[22]:


title = []
author = []
volume=[]
publisher=[]
genre=[]


# In[23]:


t=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[2]')
for i in t:
    title.append(i.text)

a=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[3]')
for i in a:
    author.append(i.text)

v=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[4]')
for i in v:
    volume.append(i.text)
    
p=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[5]')
for i in p:
    publisher.append(i.text)
    
g=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[6]')
for i in g:
    genre.append(i.text)


# In[24]:


print(len(title),len(author),len(volume),len(publisher),len(genre))


# In[25]:


df=pd.DataFrame({'Title':title,'Author':author,'Volume Sold':volume,'Publisher':publisher,'Genre':genre})
df


# In[ ]:


#@7..Scrape the details most watched tv series of all time from imdb.com. 
Url = https://www.imdb.com/list/ls095964455/ You 
have to find the following details: 
A) Name 
B) Year span 
C) Genre 
D) Run time 
E) Ratings 
F) Votes


# In[27]:


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/list/ls095964455/")


# In[38]:


name = []
year = []
genre=[]
runtime=[]
ratings=[]
votes=[]

n=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3/a')
for i in n:
    name.append(i.text)

y=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3/span[2]')
for i in y:
    year.append(i.text)

g=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p/span[5]')
for i in g:
    genre.append(i.text)
    
r=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p/span[3]')
for i in r:
    runtime.append(i.text)
    
rat=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/div/div/span[2]')
for i in rat:
    ratings.append(i.text)
    
v=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p[4]/span[2]')
for i in v:
    votes.append(i.text)


# In[39]:


print(len(name),len(year),len(genre),len(runtime),len(ratings),len(votes))


# In[40]:


df=pd.DataFrame({'Name':name,'Year':year,'Genre':genre,'Runtime':runtime,'Ratings':ratings,'Votes':votes})
df


# In[33]:


#Q8..Details of Datasets from UCI machine learning repositories. 
Url = https://archive.ics.uci.edu/
You have to find the following details: 
A) Dataset name 
B) Data type 
C) Task 
D) Attribute type 
E) No of instances 
F) No of attribute G) Year 
Note: - from the home page you have to go to the Show All Dataset page through code.


# In[49]:


driver = webdriver.Chrome()
driver.get("https://archive.ics.uci.edu/")


# In[50]:


dataset = driver.find_element(By.XPATH,'//div[@class="flex flex-wrap justify-center gap-5"]/a[1]')
dataset.click()
time.sleep(3)
dataset = driver.find_element(By.XPATH,'//label[@class="btn-primary btn-sm btn flex gap-2 rounded-full"]/div[2]')
dataset.click()


# In[52]:


name = []
type = []
task=[]
attribute=[]
instances=[]
nattributes=[]
year=[]


# In[53]:


n=driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/h2/a')
for i in n:
    name.append(i.text)

t=driver.find_elements(By.XPATH,'//div[@class="grid grid-cols-8 overflow-x-auto"]/table/tbody/tr/td[2]')
for i in t:
    type.append(i.text)

tas=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]/span')
for i in tas:
    task.append(i.text)
    
a=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]/span')
for i in a:
    attribute.append(i.text)
    
i=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]/span')
for i in i:
    instances.append(i.text)
    
na=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]/span')
for i in na:
    nattributes.append(i.text)
    
y=driver.find_elements(By.XPATH,'//div[@class="grid grid-cols-8 overflow-x-auto"]/table/tbody/tr/td[3]')
for i in y:
    year.append(i.text)


# In[54]:


print(len(name),len(type),len(task),len(attribute),len(instances),len(nattributes),len(year))


# In[55]:


df=pd.DataFrame({'Dataset Name':name,'Dataset Type':type,'Task':task,'Attribute':attribute,'No of Instances':instances,'No of Attributes':nattributes,'Year':year})
df

