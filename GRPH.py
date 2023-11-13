from fastafunction import FASTAwr
from Bio import Seq

fasta=FASTAwr('FASTAgrph.txt')
seq=fasta[0]
rosalind=fasta[1]
c=0
pairs=[]
for a in range(0,len(seq)):
    first=seq[a] #taking the first sequence
    tf=f'{first[len(first)-3]}{first[len(first)-2]}{first[len(first)-1]}' #storing the last 3 bases
    for b in range(0,len(seq)):
        second=seq[b] #taking second sequence
        ps=f'{second[0]}{second[1]}{second[2]}' #storing the first 3 bases
        if first!=second: #check they are different
            if tf==ps: #check if they are equal
                pair=[rosalind[a],rosalind[b]] #creating the pair with the codes of the strings
                pairs.append(pair)

with open('solutiongrph.txt','w') as file: #open the solution file
    file.truncate()
    for el in pairs: 
        file.write(' '.join(el)) #append every pair
        file.write(f'\n')

