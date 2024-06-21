def operations(arr,target):
    size = len(arr)
    result = []
    if(size<0 or size == 0):
        return 0
    for i in range(0,size):
        if arr[i] < target:
            for j in range(i+1,size):
                if arr[i] + arr[j] == target:
                    result.append((i,j))
    return result
        
#Test Case 1
res=operations([1,4,6,8,2,3],10)
print(res)
if(res == [(1,2) , (3,4)]):
    print("Test Case Passed. Output matches the expected")
else:
    print("Test case failed")
#Test Case 2
res1=operations([],8)
if res1 == 0:
    print(res1)
    print("Test Case Passed. Output should be zero as the input array is a null array")
else:
    print("Test Case failed")
#Test Case 3
res2=operations([1,-2,6,-6,2,3],4)
print(res2)
if(res2 == [(0,5) , (1,2)]):
    print("Test Case Passed. Output matches the expected")
else:
    print("Test Case failed")
                    
                    
            
    