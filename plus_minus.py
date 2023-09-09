Question = '''Given an array of integers, calculate the ratios of its elements that are positive, negative,
and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to  are acceptable.
Example
There are  elements, two positive, two negative and one zero. Their ratios are ,
and .Results are printed as: 0.400000
0.400000
0.200000'''


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