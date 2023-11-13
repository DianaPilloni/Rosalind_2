from fastafunction import FASTA

fasta=FASTA('FASTAlong.txt')

lenght=len(fasta[0])
for i in range(lenght):
    for s1 in fasta:
        for s2 in fasta:
            if s1!=s2:
                for j in range(len(s1)):
                    if s1[:j]==s2[-j:] and j>=int(lenght//2)-1:
                        fasta.append(s2+s1[j:])
                        if s1 in fasta:
                            fasta.remove(s1)
                        if s2  in fasta:
                            fasta.remove(s2)
print(''.join(fasta))

                   

        
