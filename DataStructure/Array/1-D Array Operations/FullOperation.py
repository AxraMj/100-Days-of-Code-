from array import *

arr1 = array("i", [10, 20, 30, 40, 50])
my_list = [11, 22, 33]

def ArrayFunction(array, value):
    array.append(60)                    # Append 60 to the array
    array.insert(3, 80)                 # Insert 80 at index 3
    array.extend([77, 88, 99, 99, 99])  # Extend the array with more elements
    array.fromlist(my_list)             # Add elements from the list
    array.remove(22)                    # Remove the first occurrence of 22
    array.pop()                          # Pop the last element
    array_index_fetch = array.index(value)  # Find index of the value
    print(f"array index of {value} is : {array_index_fetch}")
    
    # Print array contents
    for i in array:
        print(i)
    
    array.reverse()  # Reverse the array
    print("Reversed elements are:")
    for j in array:
        print(j)
    
    # Get address and size info
    address_size = array.buffer_info()
    print(f"Address and size of array is {address_size}")
    
    # Count occurrences of a value
    count_array = array.count(value)
    print(f"Number of occurrences of {value}: {count_array} times")
    
    # Convert array to bytes
    byte_representation = array.tobytes()
    print(f"Byte representation: {byte_representation}")
    
    # Convert array to list
    new_list = array.tolist()
    print(f"Converted to list: {new_list}")
    
    # Slice the array (Valid slice example)
    new_array = array[3:5]  # A valid slice, from index 3 to 4
    print(f"Sliced array: {new_array}")

ArrayFunction(arr1, 99)
