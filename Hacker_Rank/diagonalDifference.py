# For this problem I first had to understand what a Matrix was and how to build them, and then be able to
# insert, as well as retrieve the data from them. Below are my notes on what I needed to learn and then my eventual understanding of the functionality

twoDArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Row2Col3 = twoDArray[1][2]
Row1Col1 = twoDArray[0][0]
Row1Col2 = twoDArray[0][1]
Row1Col3 = twoDArray[0][2]
Row2Col1 = twoDArray[1][0]
thirdRow = twoDArray[2]

print('This is Row 2 Col 3 =', Row2Col3)
print('This is Row 1 Col 1 =', Row1Col1)
print('This is Row 1 Col 2 =', Row1Col2)
print('This is Row 1 Col 3 =', Row1Col3)
print('This is Row 2 Col 1 =', Row2Col1)
print('This is Row 3 =', thirdRow)

print("\n")

print("This the output for traversing the Matrix with a for loop below:")
print("\n")

for Outterarray in twoDArray:
  for innerArray in Outterarray:
    print(innerArray, end=" ")
  print()

print("\n")
print("Inserting an Array into the twoDArray Matrix and then printing it out:")

arr2Add = [10, 11, 12]

twoDArray.insert(3, arr2Add)

twoDArray[1].insert(2, 5.5)
twoDArray[0].insert(1, 1.5)
twoDArray[2].insert(1, 7.5)
twoDArray[2].insert(3, 8.5)
# The below is to insert another value without looping  into the 2D Array
twoDArray[2][3] = 'Sike'

for Outterarray in twoDArray:
  for innerArray in Outterarray:
    print(innerArray, end=" ")
  print()


print("Testing the HakerRank Coding Challenge:")
print("\n")

testArray = [[1,2,3],[4,5,6],[9,8,9]]


sumAcrossLeft = 0
sumAcrossRight = 0


for i in range(len(testArray)):
  iterationCount = 0
  print(testArray[i])
  for j in testArray[i]:
    print(j)
    if iterationCount == i:
      print("This is the J that is getting added to the SumAcross",j)
      sumAcrossLeft +=j
    if iterationCount == len(testArray) - i - 1:
      print("This is the J that is getting added to sumAcrossRight:", j)
      sumAcrossRight += j
    iterationCount +=1

print("\n")
print("This is the sum of the directional Left: ",sumAcrossLeft)
print("This is the sum of the directional Right: ",sumAcrossRight)

AbsoulteDifference = abs(sumAcrossLeft - sumAcrossRight)
print("This is the AbsoulteDifference: ",AbsoulteDifference)
    # sumAcross +=j

# print("\n")
# print("This is the sum of all the values of the Matrix")
# print(AboulateDifference)



print("\n")
print("This is the  Function for submission to Hacker Rank")

def diagonalDifference(arr):
  sumAcrossLeft = 0
  sumAcrossRight = 0

  for i in range(len(arr)):
      iterationCount = 0
      for j in arr[i]:
          if iterationCount ==i:
              sumAcrossLeft +=j
          if iterationCount == len(arr) - i - 1:
              sumAcrossRight +=j
          iterationCount +=1
  AbsoulteDifference = abs(sumAcrossLeft - sumAcrossRight)
  return AbsoulteDifference

print(diagonalDifference(testArray))