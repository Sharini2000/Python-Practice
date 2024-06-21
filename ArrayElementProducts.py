def operations(arr):
    size=len(arr)
    product = 1
    if size <= 0:
        return 0
    
    for i in range(0,size):
        product = 1
        for j in range(0,size):
            if i != j:
                product = product * arr[j]
                
        print(f"The product of elements except the element {arr[i]} is ",product)

print(operations([1,2,3,4]))

"""
Question: 
Problem: Product of Array Except Self
The "Product of Array Except Self" problem requires you to return an array such that each element at index i of the output array is the product of all the elements in the input array except the element at index i. The solution should not use division and should run in O(n) time.

Example:
Example 1:
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation:
The product of elements except for the first element is 2 * 3 * 4 = 24.
The product of elements except for the second element is 1 * 3 * 4 = 12.
The product of elements except for the third element is 1 * 2 * 4 = 8.
The product of elements except for the fourth element is 1 * 2 * 3 = 6.
"""