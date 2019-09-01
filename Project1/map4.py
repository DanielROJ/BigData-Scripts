
import sys
import re

def mapping():
    y = 0 ;
    for i in sys.stdin:
        if(y==1):
            tmp = i.split(',');
            print("{},{},{}".format(tmp[1].strip(), tmp[6].strip(),tmp[2].strip().split('-')[0]))
        else:
            y=1;

mapping();