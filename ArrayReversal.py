def operations(size,arr):
    if size<0:
        return "The size is not a positive number"
    if size == 1:
        return "The array doesn't need reversal as it has only one value"
    if size == 2:
        temp = arr[0]
        arr[0]=arr[1]
        arr[1]=temp
        return arr
    for elem in arr:
        if elem<0:
            return "The array is invalid"
        else:
          output=reversal(size,arr)  
          return output
          
def reversal(size,arr):
    start =0
    end = size -1
    while start < end:
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
        return arr
            
#Test case 1
result=operations(5,[1,2,3,4,5])
print("Passed. The reversed array is : " , result)
#Test Case 2
result1=operations(-1,[1,2,3,4])
print("Failed. The reason is: " , result1)
#Test Case 3
result3=operations(4,[-1,2,3,0])
print("Failed. The reason is: " , result3)
#Test case 4
result4=operations(1,[2])
print(result4)
#Test case 5
result5=operations(2,[1,2])
print(result5)
            
        
    
    
    