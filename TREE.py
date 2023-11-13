def tree(data):
    with open (data,'r') as file:
        read=file.readlines()
    read=''.join(read)
    read=read.split('\n')
    n=read[0]
    read.remove(n)
    read.remove('')
    nodes=[]
    for el in read:
        nodes.append(el.split(' '))
    edges=int(n)-len(nodes)-1
    return edges
print(tree('graph.txt'))
