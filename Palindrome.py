str1 = "LEVEL".lower()
str2 = "level".lower()
str1_list = list(str1)
str2_list = list(str2)


start =0
end = len(str1_list)-1
while start < end:
    temp = str1_list[start]
    str1_list[start] = str1_list[end]
    str1_list[end] = temp
    start = start + 1
    end = end -1
    
if(str1_list == str2_list):
    print("The strings are palindrome")
else:
    print("the strings are not palindrome")
    
        
   
    
