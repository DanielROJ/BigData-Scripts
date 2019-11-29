import urllib.request
from bs4 import  BeautifulSoup;
import re;
import json;
import sys
import os.path
sys.path.insert(0, "./src")

valor = 1998;

patronART2 = re.compile('team-home \w');
patronART3 = re.compile('team-away \w');

patronART4 = re.compile('\w graph-circle-number-value__home-team');
patronART5 = re.compile('\w graph-circle-number-value__away-team');
def scraPing2(url):
    contents = urllib.request.urlopen("https://www.uefa.com/{}".format(url)).read().decode();
    soup = BeautifulSoup(contents, 'html.parser');
    PH = soup.find('div',class_= patronART4);
    PW = soup.find('div',class_= patronART5);
    if(PH!=None and PW!=None):
        dic2=[
             PH.string.strip(),
             PW.string.strip()
        ]
        return dic2;
    else:
        return [];


for x in range(1,21):
    valor = valor +1;
    contents = urllib.request.urlopen("https://www.uefa.com/uefachampionsleague/season={}/matches/".format(valor)).read().decode();
    soup = BeautifulSoup(contents,'html.parser');

    listaArticulos = [];
    dic={};


    listaArticulos = soup.find_all("div",attrs={"class":'match-row_match'});

    for x in listaArticulos:

        TeamHome = x.find('div',class_= patronART2).find('span',class_='fitty-fit');
        TeamAway = x.find('div',class_= patronART3).find('span',class_='fitty-fit');
        scoreHome = x.find('span', class_= 'js-team--home-score');
        scoreAway = x.find('span', class_= 'js-team--away-score');
        winner = "";
        if(len(TeamHome.parent.parent.parent.get('class')) == 3):
            winner= TeamHome.string;
        else:
            winner= TeamAway.string;
        url=  x.parent.parent.find('a',class_= 'match-row_link').get('href');
        rel =scraPing2(url);# {'PossesionHome':"",'PossesionAway':"" };
        PH = "";
        PW = "";
        if(len(rel)!=0 and len(rel) >=2):
            PH = rel[0];
            PW = rel[1];

        dic ={
            'season':valor,
            'TeamHome':TeamHome.string.strip(),
            'TeamAway':TeamAway.string.strip(),
            'scoreHome':scoreHome.string.strip(),
            'scoreAway': scoreAway.string.strip(),
            'winner': winner.strip(),
            'urlMatch':url,
            'PossesionHome': PH,
            'PossesionAway':PW
        }

        #print(dic)




## Verificar si haciendo otro archivo con diferentes campos como realiza la funcion de los campos.
## Verificar El notebook de probabilidad para evaluacion de la regresion lineal