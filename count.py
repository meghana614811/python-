s="studying"
v_count=0
c_count=0
for char in s:
    if char in "aeiouAEIOU":
        v_count+=1
    else:
        c_count+=1
print("Vowels :",v_count)
print("consonent:",c_count)
