
import sys
import re

def mapping():
    y = 0 ;
    for i in sys.stdin:
        print(i);
        if(y==1):
            print(i.split(',')[1].strip());
        else:
            y=1;



mapping()