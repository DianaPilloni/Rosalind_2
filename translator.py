import re
with open(r'C:\Users\diana\OneDrive\Desktop\uniroma1\II year\pocsi\Homework to submit\codon_table2.txt','r') as l:
    
    #we have opened the file, now we want to create a list like this [('codon','aa'),('codon','aa')...]
    #first we split the list in this way, obtaining ['codon\taa','codon\taa'...]
    f=l.read().split('\n') 

    #we create a blank list
    u=[]
    for elements in f:
        #now we can split each element
        s=elements.split('\t')
        u.append(s) #this will be our final list
    
    #we create a blank dictionary and we insert every codon as the key for its amino acid
    codon_dict={}

    for elements in u:
        if elements[0]!= '': 
            #this must be done because we will have a blank space in the end of the list (idk why honestly)
            codon_dict[elements[0]]=elements[1]
