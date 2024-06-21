arr = [10,12,78,9,45]
for elem in arr:
    element = str(elem)
    
    sum = 0
    for i in element:
        sum = sum + int(i)
    print(f"the sum of {elem} is : ", sum)
       
        