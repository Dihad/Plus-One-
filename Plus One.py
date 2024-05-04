num = [1,2,3]
holding_num = num[-1]
holding_num = holding_num+1
num.pop()
num.append(holding_num)
print(holding_num)