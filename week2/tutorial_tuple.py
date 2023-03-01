###  創建新的tuple
fruits = (
    "apple",   # index 0
    "banana",  # index 1
    "cherry",  # index 2
    "durian",  # index 3
)

print(fruits)

### 讀取tuple第n個資料 
print(fruits[1]) 
# banana

# ### 修改tuple第n個資料 
# fruits[1] = "grape"
# # ERROR : tuple是不可修改的容器

# ### 刪除list第n個資料 
# del fruits[2]
# # ERROR : tuple內的物件也不可以刪除

fruits.append('x')