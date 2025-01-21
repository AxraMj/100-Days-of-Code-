data = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]  # 3D list

def fun(m):
    v = m[0][0]  # Initialize `v` to the first element in the 2D list `m`
    for row in m:  # Loop through each row of the 2D list
        for element in row:  # Loop through each element in the current row
            if v < element:  # Compare `v` with the current element
                v = element  # Update `v` if the current element is greater
    return v  # Return the largest value in the 2D list

print(fun(data[0]))  # Call `fun` on the first 2D list in `data` and print the result

#output 4