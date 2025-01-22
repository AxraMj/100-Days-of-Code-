#Give an image representation by an NxN Matrix write a method to rotate the image by 90 degree
#[1, 2 3]   #[7,2,1]    #[7,4,1]
#[4,5,6]    #[4,5,6]    #[8,5,2]
#[7,8,9]    #[9,8,3]     #[9,6,3]

#algoritham
# for i=0 to n
#     temp=top[i]
#     top[i]=left[i]
#     left[i]=bottom[i]
#     right[i]=temp

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

matrix = [[1,2], [3,4]]
print(matrix)
print(rotate_matrix(matrix))