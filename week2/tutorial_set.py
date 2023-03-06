# create
my_set = { 3,3,3,3,4,5 }
print(my_set)

# read
print( 7 in my_set )

# delete
my_set.remove(3)
print(my_set)

# update 只能移除後新增
my_set.remove(4)
my_set.add(8)
print(my_set)