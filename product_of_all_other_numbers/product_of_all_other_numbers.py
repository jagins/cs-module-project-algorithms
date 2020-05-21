'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # input of [1, 7, 3, 4]
    # output [84, 12, 28, 21]
    # needs to [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    # loop through to multiply the rest of the elements by others excluding the value of the current index
    prod = [1 for i in range(len(arr))]
    i = 1
    temp = 1
    for i in range(len(arr)):
        prod[i] = temp
        temp *= arr[i]
    
    temp = 1
    for i in range(len(arr) - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

    return prod


if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 7, 3, 4]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
