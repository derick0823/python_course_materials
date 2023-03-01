# # iterate over a list
fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#   print(fruit)

# # iterate over a tuple
# elements = ("earth", "fire", "water", "thunder")

# for element in elements:
#   print(element)

# # iterate string
# ch_num_string = "零壹貳參肆伍陸柒捌玖拾"
# for ch_num in ch_num_string:
#     print(ch_num)

# # iterate dict
# student_profile = {
#     "name": "Grace",
#     "grade": 2,
#     "gender": "F"
# }

# for key in student_profile:
#     print(key)
#     print(student_profile[key])

# for key, val in student_profile.items():
#     print(f"Key:{key}, Value:{val}")

# # iterate set
# my_set = {"AB", "AC", "BE", "CF"}

# for word in my_set:
#     print(word)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# apple
# cherry

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
# apple

# nested loop
# 印出99乘法表
for a in range(1,10):
    for b in range(1,10):
        ans = a * b
        print(f"{a} x {b} = {ans}")
        
# 