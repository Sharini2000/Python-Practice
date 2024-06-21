n=int(input("enter the size of the array: "))
while n<0:
    print("please enter positive number only!")
    n=int(input())
    
arr = []
count = 0
counted_ = []
for i in range(n):
    k = (int(input("Enter the elements: ")))
    while k<0:
        print("Enter positive numbers only!")
        k=int(input())
    arr.append(k)
    
for elem in arr:
    if elem not in counted_:
        count=0
        for i in range(0,n):
            if elem == arr[i]:
                count = count+1
        print(f"The frequency element {elem} is {count})")
        counted_.append(elem)
    ##dict_[elem] = count

 