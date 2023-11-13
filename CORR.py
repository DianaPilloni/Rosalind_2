from fastafunction import FASTA
seqs=FASTA('corr.txt')

from Bio.Seq import Seq
corrected=[]
def pointmut(str1,str2):
    mut=0
    for a in range(len(str1)):
        if str1[a]!=str2[a]:
            mut+=1
    return mut
final=[]
mutat=[]

for seq1 in seqs:
    if seqs.count(seq1)>1:
        corrected.append(seq1)
        
    elif Seq(seq1).reverse_complement() in seqs:
        corrected.append(seq1)
        
    else:
        mutat.append(seq1)
        
for seq1 in mutat:
    for seq2 in corrected:
        if pointmut(seq1,seq2)==1 and f'{seq1}->{seq2}\n' not in final:
            final.append(f'{seq1}->{seq2}\n')
                
        elif pointmut(seq1,Seq(seq2).reverse_complement())==1 and f'{seq1}->{Seq(seq2).reverse_complement()}\n' not in final:
            final.append(f'{seq1}->{Seq(seq2).reverse_complement()}\n')
                
with open('solutioncorr.txt','w') as f:
    f.write(''.join(final))