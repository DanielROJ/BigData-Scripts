import urllib.request
from bs4 import  BeautifulSoup;
import re;
import json;

valor = 1998;

patronART2 = re.compile('team-home \w');
patronART3 = re.compile('team-away \w');
for x in range(1,2):
    valor = valor +1 ;
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

        dic ={
            'season':valor,
            'TeamHome':TeamHome.string.strip(),
            'TeamAway':TeamAway.string.strip(),
            'scoreHome':scoreHome.string.strip(),
            'scoreAway': scoreAway.string.strip(),
            'winner': winner.strip()
        }

        print(dic)

## Verificar si haciendo otro archivo con diferentes campos como realiza la funcion de los campos.