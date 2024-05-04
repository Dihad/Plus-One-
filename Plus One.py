nums = [1,9,9]
string =''
for num in nums:
    num = str(num)
    string=string+num
string=int(string)
string=string+1
string=str(string)
new_string=[]
for z in string:
    new_string.append(z)
print(new_string)
