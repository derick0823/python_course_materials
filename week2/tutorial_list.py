###  創建新的list
fruits = [
    "apple",   # index 0
    "banana",  # index 1
    "cherry",  # index 2
    "durian",  # index 3
]
# print(fruits)

# # ### 讀取list第n個資料 
# print(fruits[1]) 
# # banana

# ### 修改list第n個資料 
# fruits[1] = "grape"
# print(fruits)
# ['apple', 'grape', 'cherry', 'durian']

# ### 刪除list第n個資料 
# del fruits[2]
# print(fruits)
# ['apple', 'grape', 'durian']

# ### 2D list
# row_frist_matrix = [
#     [ 13, 25, 7 ],
#     [ 91, 2, 44 ] # index 1
# ] 

# print(row_frist_matrix[1]) # 取出第一層的LIST
# print(row_frist_matrix[1][1]) # 從第二層的LIST取出ELEMENT

# col_frist_matrix = [
#     [13, 91], #idx 0
#     [25, 2], #idx 1
#     [7, 44] #idx 2
# ] 

# print(col_frist_matrix[1][1])
print(fruits)
# fruits.append("grape")
# print(fruits)
# my_favoriate = fruits.pop()
# print(my_favoriate)

fruits.insert(2,"grape")

print(fruits)

