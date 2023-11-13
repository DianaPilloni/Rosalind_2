with open ('nwck.txt','r') as file:
    fl=file.readlines()

    
trees=[]
a=0
b=1
t=0

for i in range (int(((len(fl))+1)/3)):
    pop=fl[a].replace('\n','').replace(';','')
    
    elements=fl[b].replace('\n','').split(' ')
    trees.append([pop,elements])
    t+=1
    a+=3
    b+=3


def distance(tree,el1,el2):

    id1=tree.find(el1)
    id2=tree.find(el2)
    d=tree[min(id1,id2):max(id1,id2)]
    ess=[]
    for el in d:
        if el in ['(',')',',']:
            ess.append(el)
    ess=''.join(ess)
    while  '(,)' in ess:
        ess=ess.replace('(,)','')
    if ess.count('(')==len(ess):
        return ess.count('(')
    elif ess.count(')')==len(ess):
        return ess.count(')')
    elif ess.count(',')==len(ess):
        return 2
    else:
        return ess.count('(')+ess.count(')')+2
    
distances=[]
for el in trees:
    id=trees.index(el)
    s=distance(trees[id][0],trees[id][1][0],trees[id][1][1])
    distances.append(str(s))

print(' '.join(distances))
