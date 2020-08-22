old_str = "AABABBAABBBAB"
print("The original string is : " + str(old_str))
res_new = old_str.replace('A', '%temp%').replace('B', 'A').replace('%temp%', 'B')
print("The result after replacement of elements : " + res_new)


