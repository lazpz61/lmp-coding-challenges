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