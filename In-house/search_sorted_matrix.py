'''
    This script can be used to search for a number in a sorted 2D matrix.
    Parameters: 
        - matrix: sorted 2D list
        - target: number to be searched
'''


def searchMatrix(matrix, target: int) -> bool:
    n, m = len(matrix), len(matrix[0])

    for i in range(n):  # finding the possible row
        if target <= matrix[i][m-1]:
            break

    if target in matrix[i]:  # searching in the possible row
        return True
    else:
        return False


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 10
print(searchMatrix(matrix, target))
