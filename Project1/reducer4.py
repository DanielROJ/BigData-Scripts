import sys


def reducer():
    for i in sys.stdin:
        tmp = i.strip().split(',');
        if(tmp[1] == "STAMFORD" and tmp[2] == "2015"):
            print(int(tmp[0]));
            pass

reducer();


