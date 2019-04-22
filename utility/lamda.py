def run(ld, arg):
    ld(arg)

run(lambda x: print(x + 1), 1)

def func(p, *args, **kwargs):
    print(p,args,kwargs)

func(1, 2,3,1,4, b=1,c=2)

import copy

l1 = [1,2,[3,4]]
l2 = l1
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)
l1.append(3)
l1[2].append(3)

print('l1: ', l1)
print('l2: ', l2)
print('l3: ', l3)
print('l4: ', l4)