def find_indexes(arr, min_value, max_value):
    indexes = []   
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:   
            indexes.append(i)   

    return indexes
 
input_list = input().split(', ')  
array = [int(num) for num in input_list]  
min_value = int(input())   
max_value = int(input())   

result = find_indexes(array, min_value, max_value)

 
output = ', '.join(f"{i}({array[i]})" for i in result)
print(output)
