# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:17:51 2019

@author: hmusugu
"""

import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 



df = pd.read_excel("Realogy_Harmonization v2.xlsx", sheet_name = 'Sheet1')

#Data Munging 
x = df2.iloc[:,1:2].values.astype(str)
x = x.flatten()
z = x.tolist()

z[0]='Unknown'

from string import digits 
def remove(list): 
    remove_digits = str.maketrans('', '', digits) 
    list = [i.translate(remove_digits) for i in list] 
    return list
z=remove(z)

#Impute missing terms
for i1 in range(len(z)):
    if z[i1]=='nan':
        z[i1]= 'Unknown'
        

for i1 in range(len(z)):
    if z[i1]=='NAN':
        print('T')




def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

    
#Longest substring
for i3 in range(3):
    tracker = []
    for i2 in range(len(z)-1):    
        if(levenshtein_ratio_and_distance(z[i2],z[i2+1], ratio_calc = True )>0.66):
            match = SequenceMatcher(None, z[i2], z[i2+1]).find_longest_match(0, len(z[i2]), 0, len(z[i2+1]))
            final = z[i2][match.a: match.a + match.size]  
            z[i2]= final
            z[i2+1] = final
            tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))
        else:
            tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))
   
#It took 4 min 55.18 sec to run through all the 125k rows.
            
#fuzzywuzzy method
for i3 in range(3):
    #tracker = []
    for i2 in range(len(z)-1):    
        if(fuzz.ratio(z[i2],z[i2+1] )>80):
            match = SequenceMatcher(None, z[i2], z[i2+1]).find_longest_match(0, len(z[i2]), 0, len(z[i2+1]))
            final = z[i2][match.a: match.a + match.size]  
            z[i2]= final
            z[i2+1] = final
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))
        #else:
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))


#fuzzywuzzy method 2
for i3 in range(3):
    #tracker = []
    for i2 in range(len(z)-1):    
        if(fuzz.token_set_ratio(z[i2],z[i2+1] )>89):
            match = SequenceMatcher(None, z[i2], z[i2+1]).find_longest_match(0, len(z[i2]), 0, len(z[i2+1]))
            final = z[i2][match.a: match.a + match.size]  
            z[i2]= final
            z[i2+1] = final
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))
        #else:
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))


#fuzzywuzzy method 2
for i3 in range(3):
    #tracker = []
    for i2 in range(len(z)-1):    
        if(fuzz.token_set_ratio(z[i2],z[i2+1] )>90):
            #match = SequenceMatcher(None, z[i2], z[i2+1]).find_longest_match(0, len(z[i2]), 0, len(z[i2+1]))
            #final = z[i2][match.a: match.a + match.size]  
            z[i2+1]= z[i2]
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))
        #else:
            #tracker.append(levenshtein_ratio_and_distance(z[i2],z[i2+1]))



#Saving to csv


df1 = pd.DataFrame(z)

df1.to_csv("CBS_output.csv")


levenshtein_ratio_and_distance('sad','SAD', ratio_calc = True )

df2 = z

df.to_csv("Harmonized_CBM.csv")


df['Harmonised_Supplier_Name'] = pd.DataFrame(z)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    









       