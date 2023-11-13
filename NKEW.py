from Bio import Phylo
from io import StringIO
with open ('nkew.txt','r') as file:
    fl=file.readlines()
trees=[]
a=0
b=1
t=0
weights=[]
for i in range (int(((len(fl))+1)/3)): #lets create a list where every element is a list [tree,[start,target]]
    pop=fl[a].replace('\n','').replace(';','')
    elements=fl[b].replace('\n','').split(' ')
    trees.append([pop,elements])
    t+=1
    a+=3
    b+=3

for a in range(len(trees)):#repeat for every tree
    handle=StringIO(trees[a][0])
    Tree = Phylo.read(handle, 'newick') #tree in newick format
    weights.append(str(int(Tree.distance(trees[a][1][0],trees[a][1][1]))))#find distances
    
print(' '.join(weights)) 