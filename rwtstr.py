#function "ReadWeightString" transforms given unformated weighted sequence into usable format
#example and template of string: a;b;a;b;[(a,0.5),(b,0.5)] - position 5 is uncertain

def ReadWeightString(path):                     #function accepts path to file as a string for its argument

#return result is a list of lists of tuples where:
        #main list is a string x itself
        #inner lists are position x[i] of the string x
        #tuples inside inside inner lists are pairs ("letter", occurence)

#tuples are immutable compared to list, which makes using them for each pair safe

###### variables scope:
######     path - path to file containing sequence, passed in a form of string
######     f - file
######     x - list, created from file
######     xp - final list of list of tuples
######     i, j - iterators
######     x1 - helping string for  separat solid string into letters and occurences

    f=open(path)                                #read file
    x=f.read().split(";")                       #and save it to a list splitting by delimiter, ";" in this case 
    xp=[]                                       #empty future list
    for i in x:                                 #start iterating through lists in list
        if len(i)!=1:                           #check if current position is uncertain, as certain position will have only one letter
            x1=''                               #reset helping for each loop string
            for j in i:                         #iterate through uncertain position as string
                if j.isalpha():                 #check if any symbols in string are letters
                    j="'"+j+"'"                 #if yes, put inside quotes to disringuish from rest of the string
                    x1=x1+j                     #save it to the helping string as strings are immutable in python
                else:                           #if not a letter
                    x1=x1+j                     #save the rest of the string to the helping string
            x1=eval(x1)                         #build-in eval() function allows to evaluate a string as an expression
            xp.append(x1)                       #add resulting list of tuples to final list
        else:                                   #if position is certain
            i="[('"+i+"',1)]"                   #add occurence of 1 for existing letter, add list and tuple syntax
            i=eval(i)                           #evaluate string as list of tuples
            xp.append(i)                        #add to final list


#######optional code, get exact value from position
##    for i in xp:              #iterate through lists in list
##        for j in i:           #iterate through tuples in list
##            if (j[1]==0.6):   #check for value needed in all tuples
##                print(j[0])   #j[0] is the first element of each tuple, in our case it is letter
##                print(j[1])   #j[1] is the second element of each tuple, in our case it is occurence

    return(xp)                                  #function returns a list of lists of tuples
