# %%
# to find the most optimal solution 
# we can use the lookup iwth the hash map it's having the complexity to find is O(1)

# breaking out the 2 for loops into 1 for loop
# analyze what the for loop is doing 
#   1.st calculate the numer to find 
#    


def effi(arr,target):
    key_values = {}
    for val in range(len(arr)):
       
        if arr[val] in key_values.keys():
            print(key_values[arr[val]],val)
            return key_values[arr[val]],val
        else:
            key_values[target - arr[val]] = val

    
effi(arr = [1,3,7,9,2],target = 11)

# HASH MAP : look up of O(1) time   
# %%
    