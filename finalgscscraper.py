# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:15:41 2022

@author: massh
"""

#==============IMPORTS==============#
from bs4 import BeautifulSoup
import requests
import io
import csv
from csv import writer
import pandas
#===================================#

print("===============================================================")
print("This script is designed to scrape gsc and output a txt file")
keywords = input("Enter keywords: ")
print("showing results for: "+ keywords, end='\n'*3)
print("processing")
print("===============================================================")

file= open("gsc_"+keywords+".csv","w")
writer= csv.writer(file)

header= ['Article title','Abstract','Links']
writer.writerow(header)


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#https://webscraping.com/blog/User-agents/

url = ("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="+keywords+"&btnG=")
n=0
with io.open("gsc_"+keywords+".txt","w",encoding= 'utf-8') as f:
    for page in url:
        n= n+1
        url = ("https://scholar.google.com/scholar?start="+str(n)+"0&q="+keywords+"&hl=en&as_sdt=0,5")
        #print(url)
        response = requests.get(url)
        soup= BeautifulSoup(response.content,'lxml')
        if(n==100) :
            break
        for item in soup.select('[data-lid]'):
             articletitle= (item.select('h3')[0].get_text())
             articletitle.encode('utf8')
             #print(articletitle)
             
             f.write(articletitle)
            
             abstract= (item.select('.gs_rs')[0].get_text())
             abstract.encode('utf8')
             
             f.write(abstract)
             
             links= (item.select('a')[0]['href'])
             links.encode('utf8')
            
             articletitle= (item.select('h3')[0].get_text())
             #print(articletitle)
             abstract= (item.select('.gs_rs')[0].get_text())
             links= (item.select('a')[0]['href']) 
                     
             writer.writerow([articletitle.encode('utf8'),abstract.encode('utf8'),links.encode('utf8')])
             #print(item.select('h3')[0].get_text(), end='\n')
             #print(item.select('.gs_rs')[0].get_text(), end='\n')
             #print(item.select('a')[0]['href'], end='\n'*2)   
             #f.write(links)
             
print("END OF SCRAPING")                   

di = dict()
path = ("gsc_"+keywords+".txt")
with  open(path, encoding ="utf_8") as f:
    for lin in f:
         lin = lin.rstrip()
         wds = lin.split()
         #print(wds)
         for w in wds:
             if w in di:
                 di[w] = di[w] + 1
             else:
                 di[w] = 1
#print(di) 
#sortedbyvalue = {k: v for k,v in sorted(di.items(),key=lambda v: v[1], reverse= True)}
#print(sortedbyvalue)

             
    
print("===============================================================")
print("================= done! now check the file ====================")
print("===============================================================")
#if nothing prints to console, consider using a vpn :)
