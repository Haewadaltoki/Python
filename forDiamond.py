i,k =0,0

i=0
for i in range(i,10):
    if i < 5:
        k = 0
        for k in range(0,4-i):
            print('  ',end = '')
        k=0
        for k in range(0,i*2+1):
            print('\u2665',end='')
            k+=1
    else :
        k=0
        for k in range(0,i-4):
            print('  ',end='')
            k+=1
        k=0
        for k in range(0,(9-i)*2-1):
            print('\u2665',end='')
            k+=1
    print()
