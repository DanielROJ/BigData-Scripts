import sys


def reducer():
    for i in sys.stdin:
        tmp = i.strip().split(',');
        if(tmp[1] == "STANFORD" and tmp[2] == "2015"):
            print(tmp[0]);
            pass

reducer();


