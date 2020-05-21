'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    dupes = {}
    for x in arr:
        if x not in dupes:
            dupes[x] += 1
        else:
            dupes[x] = 1
    for num in dupes:
        if dupes[num] == 1:
            return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")