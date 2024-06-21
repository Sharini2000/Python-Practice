size = int(input("Enter the size of the array "))
while size<0:
    print("Positve size only!")
    size = float(input("Enter the size of the array again "))

arr = []
temp = []
for i in range(size):
    elem=int(input(f"Enter array element {i+1} "))
    while elem<0:
        print("Positive elements only!")
        elem=int(input(f"Enter array element {i+1} "))
    arr.append(elem)
    
for k in range(size-1,-1,-1):
    temp.append(arr[k])

for i in range(size):
    arr[i]=temp[i]

print(arr)
    
    
    