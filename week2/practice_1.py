# 取出substring
ch_num_string = "零壹貳參肆伍陸柒捌玖拾"
amount = input('請輸入金額: ')

# # 第一題 - 個位數
# idx = int(amount)
# ch_num = ch_num_string[idx]
# print(f"{ch_num}元")

# 第二題 - 十位數
ten = int(amount) // 10
single = int(amount) % 10
ten_ch_num = ch_num_string[ten]
single_ch_num = ch_num_string[single]
print(f"{ten_ch_num}拾{single_ch_num}元")
