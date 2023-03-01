# 組合字串 
first_line = "天大地大"
second_line = "台科大"

# 方法ㄧ：使用 + 
#   優點： 簡單直覺
#   缺點： 需要處理資料型別的轉換
print(first_line + second_line)  # 天大地大台科大

naughty_string = 69
# print(first_line + second_line + naughty_string) # ERROR

# 方法二： 使用format，像填空題一樣，把字串需要填空的地方換成 {}
#   優點： 自動處理資料型別的轉換
#   缺點： 不夠直覺，要一直來回查看format與挖空的位置
print( "{}{}{}".format(first_line, second_line, naughty_string) )

# 方法三： 使用f""，像填空題一樣，把字串需要填空的地方換成 {變數名稱}
#   優點： 舒服了，好看又會自動轉換資料型別
print( f"{first_line}{second_line}。{naughty_string}是很吉祥的數字" )

