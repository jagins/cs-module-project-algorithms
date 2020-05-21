'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #input = [0, 3, 1, 0, -2]
    #output = [3, 1, -2, 0, 0]

    #step 1 = loop through the array
    #step 2 = check if current element is 0 and next element is greater than 0
        #swap if true
    temp = 0
    for i in range(0,len(arr) - 1):
        if arr[i] == 0:
            # temp = arr[i]
            # arr[i] = arr[i + 1]
            # arr[i + 1] =  temp
            arr.append(arr.pop(i))

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")