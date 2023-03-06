original_list = [
    [13,25,7],
    [91,2,44]
]

result = []
for first_list in original_list:
    # 做一個新的list
    result_element_list = []
    
    for num in first_list:
        # 取出所有num後乘以2再放回新的list
        result_element_list.append(num*2)
    
    # 組合出新的2D矩陣
    result.append(result_element_list)

print(result)