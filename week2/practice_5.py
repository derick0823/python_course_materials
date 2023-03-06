personal_id = 'A123456789'

# Q1
# 策略:用FOR LOOP ITERATE身分證字串，在指定長度之後用*取代

result = ""
keep_char = 2 # 保留前2位

count = 1
for char in personal_id:
    if count <= keep_char:
        result += char
    else:
        result += "*"
    count += 1

print(result)

# Q2
# 策略:用FOR LOOP ITERATE身分證字串，在指定位置用*取代
result2 = ""
count2 = 1
for char in personal_id:
    if (count2 % 2) == 0:
        result2 += "*"
    else:
        result2 += char
    count2 += 1

print(result2)