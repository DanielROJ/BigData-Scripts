import urllib.request
from bs4 import  BeautifulSoup;
import json;

contents = urllib.request.urlopen("https://www.eltiempo.com/").read().decode();

soup = BeautifulSoup(contents,'html.parser');
titular = soup.find("div",class_= "article-details informacion");
subTitulares = soup.find_all("div",class_= "article-details");

for x in subTitulares:
    print(x);

