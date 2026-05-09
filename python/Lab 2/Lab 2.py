import random
number=0
number = random.randint (5,10) 
my_list = []
while len(my_list) < number: 
    my_list.append(random.randint (1, 100)) 
u= 4
print(my_list[u])
print (my_list)
random.randint(1, 100) 

c = 0

p=0 -1
n=0
w=0
var1 = 0
var2 = 0
q=0
n=0
e=0

while q < number:
    while w < number: 
        var1 = my_list[q]
        var2 = my_list[w]
        e = my_list[q] - my_list[w]    
        if e < -1: 
            w+=1    
        else: 
            p ++ 1
            w +=1         
    p +=0 -1
    my_list.insert(p, q)
    w = 0
    q += 1
"""    
    else:
        p += -1
        w +=0 
        q += 1
if w == number: 
        my_list.insert(p, q)
        w = 0
        q += 1
print (my_list)
"""
print(my_list)