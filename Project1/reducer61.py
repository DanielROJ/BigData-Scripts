
import sys


def reducer():
    dynamic = 0;
    cost = 1;
    mem = 0;
    fr = True;
    for i in sys.stdin:
        arr = i.strip().split(',');
        dynamic = int(arr[0]);

        if(fr == False):
            if(mem == dynamic):
                cost += int(arr[1]);
            else:
                print(cost,mem);
                mem = dynamic;
                cost =1;
        else:
            mem = dynamic;
            fr = False


reducer();

