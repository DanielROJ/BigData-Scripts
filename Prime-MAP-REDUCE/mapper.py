import sys


## Daniel Rojas - Universidad Sergio Arobelda.

def mapper():
   li = "";
   for j in sys.stdin:
        li += j.lower().strip();
   [print(x) for x in li.split(" ")]


   
 		



mapper();
