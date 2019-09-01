import sys


def reducer():
    total = 0;
    count = 0;
    for i in sys.stdin:
        total += int(i);
        count+=1;
    print(total/count);

reducer();


