import numpy as np

val = [2,2,4,5,3]
weight = [3,1,3,4,2]
no_of_items = len(val)
max_weight = 7

arr = np.zeros((no_of_items, max_weight+1))

for i in range(no_of_items):
    for current_weight in range(max_weight+1):
        if current_weight < weight[i]:
            if i==0:
                arr[i,current_weight] = 0
            else:
                arr[i,current_weight] = arr[i-1,current_weight]
        
        else:
            if i==0:
                arr[i,current_weight] = val[i]
            else:
                arr[i,current_weight] = max(val[i] + arr[i-1,current_weight-weight[i]], arr[i-1,current_weight])

# print(val)
# print(weight)
print(arr)

# weights to pick
current_index_row, current_index_col = arr.shape[0]-1, arr.shape[1]-1
current_val = arr[arr.shape[0]-1, arr.shape[1]-1]
while current_val != 0:
    if current_val > arr[current_index_row - 1, current_index_col]:
        print(val[current_index_row], ", ", weight[current_index_row])
        current_index_col -= weight[current_index_row]
        current_index_row -= 1
        # print("updated values: ", val[current_index_row], ", ", weight[current_index_row])
    
    elif current_val == arr[current_index_row - 1, current_index_col]:
        current_index_row -= 1
        current_index_col = current_index_col # no change here
    else:
        break
    current_val = arr[current_index_row, current_index_col]

