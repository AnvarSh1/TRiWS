#implementation of naive version of Crochemore's longest repetition algoritm
#return result is a string, longest repeat from initial string

import re           #library for regular expressions is imported
def NaiveCr(strn):  #fucntion accepts a string as an input argument

######variables scope:
######    strn - string, passed to function
######    substrn - substring of initial string
######    x, y - iterators
######    l - length of repeat
######    match - matched string       

    l=0   #reset auxiliary variable to zero
    x=0   #reset iterator
    y=0   #reset iterator
    match=''  #reset m
    for y in range(len(strn)):                                            #iterating in range of size of input string
        for x in range(len(strn)):                                        #nested iterating in range of size of input string    
            substrn=strn[y:x]                                             #make substring a size of 0, increasing with each iteration                
            if len(list(re.finditer(substrn,strn)))>1 and len(substrn)>l: #comparsion of substring, until maximum matched size is found
                match=substrn                                             #put maximum matching substring in separate variable
                l=len(substrn)                                            #define length of repeat
    print(match)                                                          #print result
    return ()                                                             #return function


##      optionally, we can get the size of match as l=len(substrn) 
##      and considering possibility of taking values x and y from iterations
##      we can return tandem repeat tuple (i, p, l)     
