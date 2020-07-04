def max_sum_subarray(arr):
    
    current_sum = arr[0] # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]     # `max_sum` denotes the maximum value of `current_sum` ever
    
    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)
        
        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)   
    
    return max_sum


# FLAGGED