import sys


def reducer():
    mem = "";
    block = True;
    count = 0;
    arrDy = [];
    for i in sys.stdin:

        tmp = i.strip().split(',');
        condado = tmp[0].strip()
        city = tmp[1].strip();

        if (block == False):

            if (condado == mem):
                try:
                    arrDy.remove(city);
                    arrDy.append(city);
                except:
                    arrDy.append(city);
                    count += 1
            else:
                print('{},{}'.format(count,1));
                mem = condado;
                count = 1
                arrDy.clear();

        else:
            mem = condado;
            block = False;
            count += 1;


reducer();
