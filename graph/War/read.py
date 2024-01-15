path = '/home/rumin/Documents/Code/Web/graph/War/numbers.txt'
with open (path,'r') as fread:
    num = fread.read().splitlines()
    a = num[0]
    b = num[1]
    c = num[2]
    print(a,b,c)

