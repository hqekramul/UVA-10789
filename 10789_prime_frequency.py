t = int(input())
n = 0

def isprime(n):
    for i in range(2, int(num ** .5) + 1):
        if n % i == 0:
            return 0
    return 1


while n < t:
    str = list(input())
    sset = set(str)
    str1 = list(sset)
    str2 = []
    
    while str1 != []:
        num = str.count(str1[0])
        if num > 1:
            if isprime(num):
                str2.append(str1[0])
        str1.remove(str1[0])
        sset = set(str1)
    
    str2.sort()
    if str2 == []:
        print ("Case %d:" %(n +1), "empty")
    else:
        print ("Case %d:" %(n + 1), ''.join(str2))
        
    n += 1
        


