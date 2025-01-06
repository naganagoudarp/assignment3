#wap to take input of list containg n eliments and print average of all the eliment
n=input('enter eliments of list=')
l=n.split(',')
v=[]
for x in l:
    g=int(x)
    v.append(g)
l=len(v)
s=sum(v)
print('AVERAGE OF LIST ELIMENTS',s/l)