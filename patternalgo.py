#this code uses two previously deployed modules
#to input, process and find longest tandem repetitions in extended factors


import time                         #importing times module
start=time.time()
                  #initiating measurement



import rwtstr as rw                 #module for weighted string reading and formatting
import naivestrcr as naiv           #module for Crochemore's algorithm naive implementation

######variable scope:
######    x - weighted sequence, read from file
######    z, zz, zzc - threshold markers
######    i, j , k - iterators
######    cl[] - list of colours corresponding to each position in x, stores as strings
######    extfct[] - list of extended factors
######    mul - optional multiplicator
######    exts, exts1 - auxiliary strings


x=rw.ReadWeightString("mystr2")      #passing file path as a string, additional files "mystr2" (with different alphabet) and "mystr3"(with larger input) are available

z=4                                 #given z
zz=1/z                              #cumulative weight threshold 1/z, separate variable for easier use
zzc=1-zz                            #1-1/z threshold for colouring stage, separate variable for easier use


############filtering
for i in x:               #iterate through lists in list
    for j in i:           #iterate through tuples in list
        if (j[1]<zz):     #check for letters with low occurence probability
            i.remove(j)   #remove tuple from list


############colouring
cl=[]                                            #reset list for colours          
for i in x:                                      #iterate through lists in list
    for j in i:                                  #iterate through list of tuples
        if (j[1]==1):                            #if occurence is equal to 1 (single letter)
            cl.append("W")                       #add letter "W" to the list of colours
        elif (any(1>j[1]>zzc for j in i)):       #otherwise, if there is any occurence that is lower than 1 but higher that threshold on current position
            cl.append("G")                       #add letter "G" to the list of colours
            break                                #stop executing loop further, to avoid possible duplicates
        elif (all(j[1]<=zzc for j in i)):        #if all letter on current position have occurence that is lower than threshold
            cl.append("B")                       #add letter "B" to the list of colours
            break                                #stop executing loop furter, to avoid duplicates
        else:                                    #empty syntax pass
            pass                                 #empty syntax pass

############generation of extended factors
extfct=[]                                   #list of extended factors
#mul=1                                      #optional use of multiplicator to check threshold of factors, otherwise extending from-to "B" position
for i in range (len(cl)):                   #initiating universal iterator for two separate lists
    if cl[i]=="B":                          #if at some index in colours list we get "B"

        exts=""                             #reset auxilialry string
        for j in x[::i]:                    #iterate through the string till black position
            for k in j:                     #iterate through each (letter+occurence) tuple
                if k[1]>zz:                 #if occurence is higher than threshold
                    #mul=mul*k[1]           ######optinal multiplication
                    exts=exts+k[0]          #add letter to auxiliary string
                    break                   #do not iterate till next black positions
                    #this is "safety" loop, as not necessarily first position will be black.                
        if len(exts)>1:                     #if length of resulting string is more than one letter (first position is not black)
            extfct.append(exts)             #append string to list
        
        
        exts=""                             #reset auxilialry string
        for j in x[i:]:                     #iterate through the string starting from black position
            for k in j:                     #iterate through each (letter+occurence) tuple
                if k[1]>zz:                 #if occurence is higher than threshold
                    #mul=mul*k[1]           ######optinal multiplication
                    exts=exts+k[0]          #add letter to auxiliary string
                    break                   #do not iterate for duplicates
        extfct.append(exts)                 #append string to list
        exts1=""                            #reset another auxiliary string for "empty string" factor
        for j in x[i]:                      #iterate for each letter with on current position
            exts1=(j[0]+exts)               #add letter to each factor
            extfct.append(exts1)            #add factor to list



#print(extfct)                              #optional, print list of extended factors

for i in extfct:                            #iterate through list of extended factors
    naiv.NaiveCr(i)                         #pass each string to repetition finder



print(time.time()-start)                    #print run time


    

