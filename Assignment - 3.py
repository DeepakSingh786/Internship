#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[35]:


#Q1. Write a python program which searches all the product under a particular product from www.amazon.in. The 
#product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
#guitars

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.amazon.in/")


# In[57]:


item = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input') # it will bring cursor to search field
item.send_keys(input("enter your item: "))
time.sleep(3)

search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div')
search.click() #This will click on the search button
time.sleep(3)


# In[ ]:


#Q2. In the above question, now scrape the following details of each product listed in first 3 pages of your search 
#results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
#scrape all the products available under that product name. Details to be scraped are: "Brand 
#Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
#“Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.


# In[ ]:





# In[58]:


product_urls=[]
start=0
end=1
for page in range(start,end): #it's for loop to scrape first 3 pages
    url=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a')
    for i in url[0:10]:
        product_urls.append(i.get_attribute("href"))
    #next_button= driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    #next_button.click()
    #time.sleep(2)


# In[59]:


brand=[]
name=[]
price=[]
e_delivery=[]
available=[]


# In[60]:


for url in product_urls: #it will loop for every guitar in list
    driver.get(url)
    time.sleep(2)
    
    try:
        b=driver.find_element(By.XPATH,'//*[@id="productOverview_feature_div"]/div/table/tbody/tr/td[2]/span')
        brand.append(b.text)
    except: 
        brand.append('-')
        
    try:
        n=driver.find_element(By.XPATH,'//*[@id="title_feature_div"]/div/h1/span')
        name.append(n.text)
    except:
        brand.append('-')
    try:
        p=driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span/span[2]')
        price.append(p.text)
    except:
        brand.append('-')
        
    try:
        d=driver.find_element(By.XPATH,'//*[@id="deliveryBlock_feature_div"]/div/div/div/span/span')
        e_delivery.append(d.text)
    except:
        brand.append('-')
        
    try:
        a=driver.find_element(By.XPATH,'//*[@id="availabilityInsideBuyBox_feature_div"]/div/div/span')
        available.append(a.text)
    except:
        brand.append('-')


# In[42]:


print(len(product_urls),len(brand),len(name),len(price),len(e_delivery),len(available))


# In[62]:


df=pd.DataFrame({'Brand':brand,'Brand_Name':name,'Price':price,'Expected_del':e_delivery,'Availability':available,'URL':product_urls,})
df


# In[63]:


df=pd.DataFrame({'Brand':brand,'Brand_Name':name,'Price':price,'Expected_del':e_delivery,'Availability':available,'URL':product_urls,})
df.to_csv('deepak.csv')


# In[56]:





# In[ ]:


#Q4...Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
#and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
#Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
#“Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
#details is missing then replace it by “- “. Save your results in a dataframe and CSV.


# In[91]:


driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.flipkart.com/")


# In[92]:


item = driver.find_element(By.XPATH,'//*[@class="_2SmNnR"]/input') # it will bring cursor to search field
item.send_keys(input("enter your item: "))
time.sleep(3)

search = driver.find_element(By.XPATH,'//button[@class="_2iLD__"]/*')
search.click() #This will click on the search button
time.sleep(3)


# In[93]:


product_urls=[]
url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    product_urls.append(i.get_attribute("href"))


# In[98]:


print(len(product_urls),len(name),len(price),len(colour),len(brand))


# In[94]:


brand=[]
name=[]
price=[]
colour=[]
ram=[]
storage=[]
primary_c=[]
secondary_c=[]
display=[]
battery=[]

#as discussed via ticket, I have scraped half values for this question


# In[95]:


for url in product_urls: #it will loop for every guitar in list
    driver.get(url)
    time.sleep(2)
    
    try:
        b=driver.find_element(By.XPATH,'//*[@class="aMaAEs"]/*/*/*')
        brand.append(b.text)
    except: 
        brand.append('-')
        
    try:
        n=driver.find_element(By.XPATH,'//table[@class="_14cfVK"]/tbody/tr[3]/td[2]/ul/li')
        name.append(n.text)
    except:
        name.append('-')
    try:
        p=driver.find_element(By.XPATH,'//*[@class="_25b18c"]/div')
        price.append(p.text)
    except:
        price.append('-')
        
    try:
        c=driver.find_element(By.XPATH,'//table[@class="_14cfVK"]/tbody/tr[4]/td[2]/ul/li')
        colour.append(c.text)
    except:
        colour.append('-')


# In[101]:


df=pd.DataFrame({'Brand':brand,'Brand_Name':name,'Price':price,'Colour':colour,'URL':product_urls,})
df


# In[ ]:





# In[ ]:


#Q3...Write a python program to access the search bar and search button on images.google.com and scrape 10 
#images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 7


# In[102]:


driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://images.google.com/")


# In[107]:


item = driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]') # it will bring cursor to search field
item.send_keys(input("enter your item: "))
time.sleep(3)

search = driver.find_element(By.XPATH,'//button[@class="Tg7LZd"]/div/span/*')
search.click() #This will click on the search button
time.sleep(3)


# In[126]:


img_urls=[]
img_data=[]


# In[ ]:


#for _ in range(20): #means the page will be scrolled 20 times
#driver.execute_script("window.scrollBy(0,1000)")
images=driver.find_element(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for image in images[0:10]:
    source=image.get_attribute('src')#pull the link of images (src for images links)
    if source is not None: #in case nothing written on source above but if the link is there then system will check if the link is valid or not in the for loop below
        if(source[0:4] == 'http'): # it tells if the link is starting 4 letters with http then only append it
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        breakBy.XPATH,
    print("Downloading {0} of {1} images".format(i,10))
    response= requests.get(img_urls[i]) #means getting images one by one
    file = open(r"C:\Users\Shivansh\OneDrive\Images" + str(i)+".jpg","wb") #wb specify that we downloading the image
    file.write(response.content)


# In[211]:


#Q5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.google.co.in/maps/@28.6436846,76.7635778,10z?entry=ttu")


# In[212]:


item = driver.find_element(By.XPATH,'//input[@class="searchboxinput xiQnY"]') # it will bring cursor to search field
item.send_keys(input("enter your item: "))
time.sleep(3)

search = driver.find_element(By.XPATH,'//div[@class="pzfvzf"]')
search.click() #This will click on the search button
time.sleep(3)


# In[238]:


import re
try:
    url_string=driver.current_url
    print("URL Extracted: ",url_string)
    lat_lng=re.findall(r'@(.*)data',url_string)
    print("lat_lng extracted: ",lat_lng)
except:
    url_string='url not found'


# In[229]:


#Q7...Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
#“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”


# In[280]:


driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.forbes.com/billionaires/")


# In[272]:


rank=[]
name=[]
net_w=[]
age=[]
country=[]
source=[]
indus=[]

r=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[1]')
for i in r:
    rank.append(i.text)
    
n=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[2]')
for i in n:
    name.append(i.text)
    
w=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[3]')
for i in w:
    net_w.append(i.text)
    
a=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[4]')
for i in a:
    age.append(i.text)
    
c=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[5]')
for i in c:
    country.append(i.text)
    
s=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[6]')
for i in s:
    source.append(i.text)
    
i=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[7]')
for i in i:
    indus.append(i.text)

next_button= driver.find_element(By.XPATH,'//span[@class="Pagination_bubbleArrow__WFrX4 Pagination_paginationBtnNext__IOwqm"]/svg')
next_button.click()


# In[270]:


print(len(indus),len(name),len(net_w),len(age),len(country),len(source),len(rank))


# In[273]:


df=pd.DataFrame({'Rank':rank,'Name':name,'Net_worth':net_w,'Age':age,'Country':country,'Source':source,'Industry':indus,})
df


# In[ ]:


#Q9...Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
“London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
reviews, privates from price, dorms from price, facilities and property description. 


# In[289]:


driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.hostelworld.com/")


# In[ ]:





# In[294]:


item = driver.find_element(By.XPATH,'//button[@class="item-content"]') # it will bring cursor to search field
item.send_keys('London')
time.sleep(3)


# In[299]:


search = driver.find_element(By.XPATH,'//button[@class="btn-content medium-button icon-only"]/div/*')
search.click() #This will click on the search button
time.sleep(3)


# In[ ]:


hostel=[]
distance=[]
rating=[]
total_r=[]
country=[]
source=[]
indus=[]

h=driver.find_elements(By.XPATH,'//div[@class="property-name"]/span')
for i in h:
    hostel.append(i.text)
    
d=driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
for i in d:
    distance.append(i.text)
    
r=driver.find_elements(By.XPATH,'//span[@class="number"]')
for i in r:
    rating.append(i.text)
    
rev=driver.find_elements(By.XPATH,'//span[@class="left-margin"]')
for i in rev:
    total_r.append(i.text)

