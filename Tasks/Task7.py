from Convolution.ConvTest import ConvTest
from helper_functions import *



def convolve(x1,y1,x2,y2) :

   len1 = len(y1)
   len2 = len(y2)
   convolved = np.zeros(len1 + len2 - 1)
   newmin=int(min(x1)+min(x2))
   newmax=int(max(x1)+max(x2))
   new_indices=list(range(newmin,newmax+1))
   for i in range(len1):
        for j in range(len2):
             convolved[i + j] += y1[i] * y2[j]
    
   ConvTest(new_indices,convolved)
             
   return convolved,new_indices


