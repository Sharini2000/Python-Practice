length = int(input("enter the length of the array "))
while length<0:
    length = int(input("Plese a positive length of the array "))
arr = []
for i in range(length):
    k=int(input(f"enter the element {i+1}: "))
    while k<0:
        print("Positive numbers only")
        k=int(input(f"enter again element {i+1}: "))
    arr.append(k)
max = arr[0]
for i in arr:
    if max < i:
        max = i
print(max)
