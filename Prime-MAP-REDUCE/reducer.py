

import sys


## Daniel Rojas - Univerdiad Sergio Arboleda

def reduce():
	rel = "";
	temp = "";
	count = 0;
	for i in sys.stdin:

		if(count == 0):
			temp= i;
		pass

		if(temp == i):
			count+=1;

		else:
			rel += temp.strip()+","+str(count)+" ";
			count = 1;
			temp = i;
	[print(x) for x in rel.split(" ")]


reduce();



