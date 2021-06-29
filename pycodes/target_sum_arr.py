#%%
# my solution 
def get_target_sum(arr,target):
    a = 0 
    if len(arr) <= 1 : 
        return None 
    
    for val in range(len(arr)):
        for bval in range(len(arr)- a):
            if target == arr[a] + arr[a + bval]: 
                return [a,a + bval]
        a = a + 1 
    return 'value_not_found'

get_target_sum([1,4,5,6,7],5)

#%%
# Andrei's solution


def andrei( arr, target):
    for val in range(len(arr)): 
        # print(val)
        value_to_find = target - arr[val] 
        for bval in range(len(arr) - val):
            cval = val + bval 
            if value_to_find == arr[cval]:
                return [val,cval]
                
    return 'value_not_found'

andrei(arr = [1,4,5,6,7],target = 800)


# %%

# %%
