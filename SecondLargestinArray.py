#Secod Largest number in the array
arr = [10,20,39,28,15]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j-1]>arr[j]:
            temp = arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp

print(arr[len(arr)-2])
            
            