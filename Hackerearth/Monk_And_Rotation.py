# Problem Question

# Monk and Rotation
# Monk loves to preform different operations on arrays, and so being the 
# principal of Hackerearth School, he assigned a task to his new student Mishki. 
# Mishki will be provided with an integer array A of size N and an integer K , 
# where she needs to rotate the array in the right direction by K steps and then
#  print the resultant array. As she is new to the school, please help her to complete the task.

# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
# 1) The first line consists of two integers N and K, N being the number of elements in the array 
# and K denotes the number of steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.


# Output:
# an Array in which every last number will be appended to the beginning of the array for the amount being given in K

# Methods to consider for solution:
# append, empty array creation, array methods, concat for the space seperated numbers(so must be made into an array)


# Solution:

# input = input()

# def test_string(input):
#   return input.split(" ")

# print(test_string(input))

# array = [1,2,3,4,5,6]

# array.pop(-1)

# print(array)

# amount =  3

# for index in range(amount):
#   lastDigit = array.pop(-1)
#   array.insert(0,lastDigit)

# print(array)

# stringArray =  list(map(str,array))
# joinedStringArray = ' '.join(stringArray)

# print(joinedStringArray)

# Steps to Take
# 1. Take in all input and extract the sequence and turn the integer inputs into an array
# 2. use the sequence as the amount of times to loop through as a the number of test cases increases
# 3. ensure that we use the difference between the total amount of digits to the Kth value and this will be where we start to print the array shifting becasue these values will be moved to the beginning of the joinedStringArray
# 4. then we can start printing the remaining values from the indesx value which would mean that we shifted what we needed printed.  
# 5. Take the items that we are iterating over and append into an array. 
# 6. ensure the array is displayed as a string that is a space separated. 


t = int(input())
for test in range(t):
  display = []
  n, k = map(int, input().split())
  a = input().split(" ")
  index = n - (k % n)
  for i in range(index, n):
    display.append(a[i])
  for i in range(index):
    display.append(a[i])
  joinedStringArray = ' '.join(display)
  print(joinedStringArray)




