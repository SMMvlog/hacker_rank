from functools import reduce

question = '''Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers. Then print the respective minimum and
maximum values as a single line of
two space-separated
long integers. Example

The minimum sum is  and the maximum sum is . The function prints

16 24'''

def miniMaxSum(arr):
    try:
        min_num = reduce(lambda x,y:x+y,arr)-max(arr)
        max_num = reduce(lambda x,y:x+y,arr)-min(arr)
        return print(min_num,max_num)
    except Exception as ex:
        return print(False)
    
miniMaxSum([1,3,5,7,9])