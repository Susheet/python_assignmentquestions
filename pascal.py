def pascalSpot(row,col):
    if(col == 1): return 1
    if(col==row):return 1
    upleft = pascalSpot(row-1,col-1)
    upright = pascalSpot(row-1,col)
    return upleft+upright

for r in range(1,10):
    for c in range(1,r+1):
        print(pascalSpot(r,c),end=" ")
    print("")