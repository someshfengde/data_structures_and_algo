#%%
def area_of_container(arr):
    # we have to send the most area which will be storing highest number of values 
    if len(arr) == 0 or len(arr) == 1 : 
        return None
    # figuring out the solution 
    maximum = 0 
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            area = min(arr[i] , arr[j + i] ) * (j)
            maximum = max(area,maximum)
    return maximum 

            


area_of_container([1,2,3,4,5,6])
# %%
def area_of_container_effective(a):
    first = 0 
    last = len(a) - 1
    maximum =0 
    while first < last:
        area = min(a[first],a[last]) * (last -first)
        maximum = max(maximum , area)
        if a[first] > a[last] :
            last -= 1 
        elif a[first] < a[last]:
            first += 1
    return maximum

area_of_container_effective([4,8,1,2,3,9])

# %%
