import urllib.request
from bs4 import  BeautifulSoup;
import re;
import json;

contents = urllib.request.urlopen("https://www.eltiempo.com/").read().decode();

soup = BeautifulSoup(contents,'html.parser');
listaArticulos = [];

jsonLista = [];
dic = {};


patronART = re.compile('\w[0-9]');
patronART2 = re.compile('category page-link \w');
listaArticulos = soup.find_all("article",attrs={"dtm-name":patronART});

for art in listaArticulos:
    info_Categoria =art.find('a', class_=patronART2);
    info_titulo =  art.find('a', class_='title page-link');
    info_fecha = art.find('span', class_ = 'published-at');
    if(info_Categoria != None and info_titulo!= None):
        dic = {
        #'Fecha': info_fecha.string,
        'Url_categoria': info_Categoria.get('href'),
        'Categoria': info_Categoria.string,
        'Url_Noticia': info_titulo.get('href'),
        'Titulo':info_titulo.string,
        };
        print(dic)






