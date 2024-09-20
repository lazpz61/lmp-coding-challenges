# This serves as code which was oringally thought to be the intended requirements


T = input()  # This is not used in the function, so you can skip this unless needed

N = input()

A = input()

sequence = int(N[2])
array = A.split(" ")


def monk_and_Rotation(sequence, array):
    for index in range(sequence):
        lastDigit = array.pop(-1)  # Remove the last element
        array.insert(0, lastDigit)  # Insert it at the front
    stringArray = list(map(str, array))  # Convert all elements back to strings
    joinedStringArray = ' '.join(stringArray)  # Join the elements to a string
    return joinedStringArray  # Return the final rotated array as a string

print(monk_and_Rotation(sequence, array))