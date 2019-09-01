
import sys
import re

def mapping():
    y = 0 ;
    for i in sys.stdin:
        if(y==1):
            tmp = i.split(',');
            print("{},{}".format(tmp[8].strip(), tmp[6].strip()));
        else:
            y=1;

mapping()