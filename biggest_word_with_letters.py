def high(x):
    ls = x.split(' ')
    biggest = 0 
    lar = ''
#     [ let for word in ls for let in word ]
    for val in ls:
        sum = 0
        for let in val:
            sum += ord(let) - 96
        if sum > biggest:
            biggest = sum
            lar = val
    return lar
            
    
            
                