def row_sum_odd_numbers(n):
    firstnum = 1
    Sum = i = 0
    count = 0
    
    for x in range(1,n):
        count += x
        
    while i < count:
        firstnum += 2
        i+=1     
    Sum = sum([x for x in range(firstnum,firstnum + n * 2 , 2)])
    return Sum
    