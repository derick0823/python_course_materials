
ch_string = "貳佰伍拾零元"

ch_dict = {
    "貳":2,
    "伍":5,
    "零":0
}

# 取出對應(百位/十位/個位)位置的中文字
hunderd = ch_string[0]
ten = ch_string[2]
single = ch_string[4]
print(hunderd,ten,single)

# 中文字轉回阿拉伯數字
num_hunderd = ch_dict[hunderd]
num_ten = ch_dict[ten]
num_single = ch_dict[single]

result = num_hunderd*100 + num_ten*10 + num_single
print(result)

result2 = f"{num_hunderd}{num_ten}{num_single}" #string
print(int(result2) + 20)