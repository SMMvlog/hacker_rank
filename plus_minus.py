def puls_minus(n,arr):
    try:
        plus = 0
        minus = 0
        zero = 0
        for num in arr:
            if num > 0:
                plus +=1
            elif num < 0:
                minus +=1
            else:
                zero +=1
        print(round(plus/n,6))        
        print(round(minus/n,6))        
        print(round(zero/n,6))        
    except Exception as ex:
        return "something went wrong"
    
puls_minus(5,[1,1,0,-1,-1])