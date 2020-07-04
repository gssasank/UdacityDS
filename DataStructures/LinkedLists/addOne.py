def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    
    """
    num = 0
    blip = []
    for i in range(len(arr)):
        
        num += arr[i]*(10**(len(arr) -i -1))
    num += 1
    res = [int(x) for x in str(num)] 

    
    
    
    return res

print(add_one([1,2,3]))